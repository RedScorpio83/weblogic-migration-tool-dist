==========================================================================
 WEBLOGIC CONFIGURATION MIGRATION TOOL v2.0
 Sviluppatore: Alessandro Caliciotti
 Azienda: Nimis Consulting Information Technologies
==========================================================================

REQUISITI ED INSTALLAZIONE SU NUOVE POSTAZIONI:
L'applicazione viene fornita in modalità completamente PORTABILE e STANDALONE.
Include al suo interno la Java Development Kit (JDK 17) nella cartella 'jdk/',
pertanto NON richiede alcuna installazione di Java sul computer ospite.

ISTRUZIONI DI AVVIO:
1. Su Windows:
   Fare doppio click sul file: run.cmd
   (Oppure eseguire da terminale: run.cmd)

2. Su Linux:
   Aprire il terminale ed eseguire: ./run.sh

STRUTTURA DELLA CARTELLA:
- MigrationTool.jar     : Eseguibile principale della GUI
- logo.png              : Logo aziendale Nimis Consulting
- jdk/                  : Ambiente Runtime Java 17 Portabile integrato
- lib/                  : Librerie FlatLaf Dark Theme
- extractions/          : Cartella contenente i dump estratti dal server sorgente
- extractions_tools/    : Pacchetti generati per l'estrazione offline sul server sorgente
- tasks/                : Pacchetti di migrazione/deploy generati da eseguire sul target

FUNZIONALITÀ CHIAVE:
1. Estrazione remota via SSH (WebLogic 11g) e decifrazione automatica delle password JDBC.
2. Estrazione offline senza SSH tramite pulsante 'GENERA PACCHETTO ESTRAZIONE OFFLINE'.
3. Archiviazione automatica di tutti i file applicativi (.war, .ear, .jar) nella cartella apps/.
4. Mappatura ed editing dinamico di Server, Cluster, DataSources e Password DB.
5. Replicazione 100% automatica della topologia e deploy applicativo su WebLogic 12c.
6. Overlay di attesa stile Apple in tema Gold Leaf e pulsante di pulizia rapida dello storico.
