==========================================================================
 WEBLOGIC CONFIGURATION MIGRATION TOOL v4.0.0
 Sviluppatore: Alessandro Caliciotti
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
- MigrationTool.jar : Eseguibile principale della GUI
- run.cmd           : Script di avvio automatico per Windows
- run.sh            : Script di avvio automatico per Linux / macOS
- README.md         : Documentazione generale del repository
- GUIDA_UTENTE.md    : Guida utente operativa con catalogo di tutte le funzioni
- WIKI.md           : Wiki tecnica dell'architettura MBean e pack/unpack
- jdk/              : Java Runtime portabile integrato (JDK 17)
- works/            : Directory dei lavori e dei task esportati
