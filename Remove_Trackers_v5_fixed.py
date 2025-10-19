import os
import shutil
import datetime
import csv
import re
import bencodepy

# === CONFIGURAZIONE ===
QBITTORRENT_PATH = r"C:\Users\User\AppData\Local\qBittorrent"  # <-- Modifica se serve. Questa è la cartella predefinita
BT_BACKUP_PATH = os.path.join(QBITTORRENT_PATH, "BT_backup")  # <-- Viene usata la cartella predefinita per i files .torrent e fastresume
TRACKER_PATTERN = r"chihaya\.de|pybittrack\.retiolus\.net"  # <-- Indirizzi trackers usati come esempio
LOG_FILE = os.path.join(QBITTORRENT_PATH, "tracker_removal_log.csv")  # <-- Edita il nome del file CSV a piacimento

# === FUNZIONE DI ELABORAZIONE ===
def process_files(dry_run=True):
    removed_files = []
    matched_files = []

    for filename in os.listdir(BT_BACKUP_PATH):
        if not filename.endswith(".fastresume"):
            continue

        file_path = os.path.join(BT_BACKUP_PATH, filename)
        try:
            with open(file_path, "rb") as f:
                data = bencodepy.decode(f.read())  # decode direttamente

            modified = False

            # Cerca tracker corrispondenti
            for key in (b"trackers", b"announce-list"):
                if key in data:
                    for group in data[key]:
                        for tracker in group:
                            if re.search(TRACKER_PATTERN, tracker.decode(errors="ignore")):
                                modified = True

            if modified:
                matched_files.append(filename)

                if not dry_run:
                    # Rimuove i tracker corrispondenti
                    for key in (b"trackers", b"announce-list"):
                        if key in data:
                            new_list = []
                            for group in data[key]:
                                clean_group = [t for t in group if not re.search(TRACKER_PATTERN, t.decode(errors="ignore"))]
                                new_list.append(clean_group)
                            data[key] = new_list

                    with open(file_path, "wb") as f:
                        f.write(bencodepy.encode(data))  # encode direttamente
                    removed_files.append(filename)
                    print(f"🧹 Tracker rimosso da: {filename}")
                else:
                    print(f"🔍 (Simulazione) Tracker da rimuovere in: {filename}")

        except Exception as e:
            print(f"⚠️ Errore con {filename}: {e}")

    # === RISULTATI ===
    if dry_run:
        if matched_files:
            print(f"\n📋 {len(matched_files)} file contengono tracker da rimuovere.")
        else:
            print("\nℹ️ Nessun file contiene tracker corrispondenti al pattern.")
    else:
        if removed_files:
            with open(LOG_FILE, "w", newline="", encoding="utf-8") as log:
                writer = csv.writer(log)
                writer.writerow(["Nome file fastresume", "Data e ora"])
                for f in removed_files:
                    writer.writerow([f, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
            print(f"\n📜 Log salvato in: {LOG_FILE}")
        else:
            print("\nℹ️ Nessun file modificato: nessun tracker corrispondente trovato.")


# === INIZIO SCRIPT ===
print("\n=== RIMOZIONE TRACKER NON DESIDERATI - QBittorrent ===\n")

# 1️⃣ Backup (solo una volta)
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = os.path.join(QBITTORRENT_PATH, f"BT_backup_full_{timestamp}")

print(f"🔄 Creazione backup completo di '{BT_BACKUP_PATH}' in '{backup_folder}'...")
try:
    shutil.copytree(BT_BACKUP_PATH, backup_folder)
    print("✅ Backup completato!\n")
except FileExistsError:
    print("ℹ️ Backup già esistente, nessuna nuova copia creata.\n")

# 2️⃣ Simulazione iniziale
choice = input("Vuoi eseguire prima una simulazione (senza modificare nulla)? [S/N]: ").strip().lower()
dry_run = (choice != "n")

print("\n🚀 Avvio in modalità: " + ("🔍 SIMULAZIONE" if dry_run else "🧹 MODIFICA REALE"))
process_files(dry_run=dry_run)

# 3️⃣ Se era simulazione, chiedi se procedere con la rimozione reale
if dry_run:
    again = input("\nVuoi ora eseguire davvero la rimozione dei tracker? [S/N]: ").strip().lower()
    if again == "s":
        print("\n⚠️ Verranno applicate le modifiche. Il backup NON verrà ricreato.\n")
        process_files(dry_run=False)
    else:
        print("\n✅ Operazione terminata senza modifiche.")
else:
    print("\n✅ Operazione completata.")

