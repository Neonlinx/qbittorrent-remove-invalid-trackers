# qbittorrent-remove-invalid-trackers
A simple (and personal) python script to remove specific tracker(s) from every torrent using qbittorrent API and fastresume files.

ENGLISH:
Especially with torrents from public trackers, it happens that many files use trackers that are now unreachable, dead or with an error. This not only wastes resources but also the user's patience, especially if you use antivirus or other security systems that analyze network traffic. In my case, for example, the antivirus sent me a notification every time a file tried to connect to trackers that used expired certificates. Hence the need to create a small and very simple script to remove these trackers from the files.
This script backs up all your .torrent and fastresume files by putting them in a special folder created in the default qbittorrent directory 'BT_backup'; it then analyzes all the files looking for the addresses of the trackers you have provided (you just have to edit the first lines of the script). At this point you can decide to do a simulation to see how many files contain the 'defective' trackers. Finally, it will ask you to continue with the real removal by saving the results in a csv file (again, if you want, you can indicate a name of your choice for the csv file).
As mentioned, the script works on fastresume files. For this reason, qbittorrent must be turned off during execution. Once finished, restart it and you will no longer have problems.

Instructions: 1. Turn off qbittorrent
2. Edit the lines at the beginning of the script under '===CONFIGURATION===' as needed and save the file
3. Open powershell as Administrator
4. Go to the folder where you downloaded the script and run it with 'python Remove_Trackers_v5_fixed.py' (obviously without the quotes)
5. Once finished, restart qbittorrent

The script has been tested on Windows 10 with Python 3.14



ITALIANO:
Soprattutto con i torrent provenienti da tracker pubblici, accade che molti files usino dei trackers che ormai sono irraggiungibili, morti o con errore. Questo non solo spreca risorse ma anche la pazienza dell'utente soprattutto se si usano antivirus o altri sistemi di sicurezza che analizzano il traffico di rete. Nel mio caso, per esempio, l'antivirus mi mandava una notifica ogni volta che che un file cercava di connettersi a trackers che usavano certificati scaduti. Da qui è nata la necessità di creare un piccolo e semplicissimo script per rimuovere questi trackers dai files.
Questo script fa un backup di tutti i vostri files .torrent e fastresume mettendoli in una cartella apposita creata nella directory predefinta di qbittorrent "BT_backup"; analizza poi tutti i file cercando gli indirizzi dei trackers che avrete fornito (bisogna semplicemente editare le prime righe dello script). A questo punto potrete decidere di fare una simulazione per vedere quanti files contengono i tracker "difettosi". Infine vi chiederà di continuare con la rimozione reale salvando i risultati in un file csv (anche in questo caso, se volete, potrete indicare un nome a vostro piacimento per il file csv). 
Come detto lo script lavora sui file fastresume. Per questo motivo qbittorrent deve essere spento durante l'esecuzione. Una volta finito riavviatelo e non avrete più noie. 

Istruzioni: 1. Spegnere qbittorrent
            2. Editare le righe all'inizio dello script sotto "===CONFIGURAZIONE===" a seconda delle vostre necessità e salvare il file
            3. Aprire powershell come Amministratore
            4. Andare nella cartella dove avete scaricato lo script e lanciatelo con "python Remove_Trackers_v5_fixed.py" (ovviamente senza le virgolette)
            5. Una volta finito ravviate qbittorrent

Lo script è stato testato su Windows 10 con Python 3.14
