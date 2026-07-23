# 📖 Guida Utente Operativa - WebLogic Migration Tool (v3.8.0)

<p align="center">
  <b>Sviluppatore: Alessandro Caliciotti</b> | <i>Nimis Consulting Information Technologies</i>
</p>

---

## 📋 Indice dei Contenuti
1. [Panoramica ed Avvio Applicazione](#1-panoramica-ed-avvio-applicazione)
2. [Gestione Lavori e Cartella `works/`](#2-gestione-lavori-e-cartella-works)
3. [Scheda 1: Connessione, Profili & Dump Sorgente](#3-scheda-1-connessione-profili--dump-sorgente)
4. [Scheda 2: Rinomina, Mappature e Gestione Avanzata Machine](#4-scheda-2-rinomina-mappature-e-gestione-avanzata-machine)
   - [4.1 Griglia di Mappatura (A -> B)](#41-griglia-di-mappatura-a---b)
   - [4.2 Gestione Intelligente Machine (Elimina, Consolida, Aggiungi)](#42-gestione-intelligente-machine)
   - [4.3 Validazione Multi-Target e Modal Interattivo di Correzione](#43-validazione-multi-target-e-modal-interattivo-di-correzione)
   - [4.4 Visualizzazioni Grafiche & Esportazione PNG](#44-visualizzazioni-grafiche--esportazione-png)
5. [Scheda 3: Ispezione Target, Generazione Task & Deploy Remoto](#5-scheda-3-ispezione-target-generazione-task--deploy-remoto)
6. [FAQ & Risoluzione Problemi](#6-faq--risoluzione-problemi)

---

## 1. Panoramica ed Avvio Applicazione

Il **WebLogic Migration Tool** è una piattaforma professionale disegnata per semplificare ed automatizzare la migrazione di ambienti **Oracle WebLogic Server (11g/12c)**.

### 🚀 Avvio
- **Windows**: Eseguire il file `run.cmd` (o fare doppio click su `MigrationTool.jar` se Java 8+ è configurato nel sistema).
- **Linux / macOS**: Eseguire `./run.sh` da terminale.

> [!NOTE]
> L'applicazione si avvia automaticamente **a schermo intero (massimizzata)** per offrire una fruizione ottimale delle griglie di mappatura e delle viste architetturali grafiche.

---

## 2. Gestione Lavori e Cartella `works/`

Alla prima apertura dell'applicazione, le schede operative **1, 2 e 3 sono disattivate** finché l'utente non seleziona o crea un **Lavoro di Migrazione Attivo**.

### 📁 Struttura della Cartella `works/`
Ogni lavoro viene salvato all'interno della cartella locale `works/` con una numerazione progressiva ed un nome descrittivo:
```
works/
├── 001_Migrazione_PROD_11g_12c/
│   ├── dump/             -> File JSON e dump estratti dal Server Sorgente (Server A)
│   ├── deploy/           -> Pacchetti di task numerati generati per il Target (Server B)
│   ├── target_dumps/     -> Ispezione in tempo reale del Dominio Target (Server B)
│   └── prj_saves/        -> File salvati di progetto mappatura (.wlsmap)
```

### 🛠️ Pulsanti Gestione Lavoro (Toolbar Superiore)
- **`📁 CARICA LAVORO DI DESTINAZIONE`** (Pulsante Verde): Apre il popup di selezione tra i lavori esistenti nella cartella `works/`.
- **`➕ NUOVO LAVORO`**: Crea una nuova cartella lavoro numerata ed inizializza i sotto-percorsi.
- **`🧹 PULISCI TASK E DUMP`**: Apre una finestra di gestione per visualizzare ed eliminare i lavori non più necessari con un click sul cestino.

Non appena un lavoro viene selezionato o creato, il badge in alto a sinistra si illumina in verde (es. `📁 LAVORO ATTIVO: 001_se`) e **tutte le 3 schede dell'interfaccia si abilitano istantaneamente**.

---

## 3. Scheda 1: Connessione, Profili & Dump Sorgente

La Scheda 1 consente di collegarsi al server sorgente via SSH ed estrarre la topologia reale.

### 📋 Caricamento & Sincronizzazione Bidirezionale Profili
- Dal menu a tendina **PROFILO CONNESSIONE SALVATO**, selezionando un profilo salvato verranno popolati automaticamente sia i campi del Server Sorgente (Scheda 1) che quelli del Server Target (Scheda 3).
- Qualsiasi modifica o salvataggio di un profilo si sincronizza in tempo reale su tutta l'applicazione.

### 📥 Estrazione Remota SSH
1. Compilare IP, porta SSH (22), credenziali di sistema (`root`/`oracle`) e porta/credenziali WebLogic (`t3://host:7001`).
2. Cliccare su **`ESTRAZIONE REMOTA SSH (SERVER LINUX)`**.
3. Il tool estrae l'intera topologia MBean, decifrando automaticamente le password JDBC e scaricando i file `.war` / `.ear` e le **Librerie Condivise** nella cartella `dump/`.

---

## 4. Scheda 2: Rinomina, Mappature e Gestione Avanzata Machine

Questa scheda rappresenta il cuore logico della migrazione.

### 4.1 Griglia di Mappatura (A -> B)
Consente di ridefinire ogni singolo elemento estratto dal sorgente:
- **MACHINE**: Nome delle macchine di destinazione e tipo OS (`UnixMachine` / `Machine`).
- **CLUSTER**: Rinomina dei Cluster target.
- **SERVER**: Rinomina dei Managed Server, modifica delle porte di ascolto e riassegnazione alle Machine/Cluster.
- **JDBC DATASOURCE**: Aggiornamento delle credenziali DB, URL e target di assegnazione.
- **APPLICAZIONI & LIBRERIA CONDIVISA**: Definizione del percorso di staging e dei target di deploy.

### 4.2 Gestione Intelligente Machine
- **`🗑️ ELIMINA RIGA SELEZIONATA`**: Se si elimina una riga Machine che possiede risorse collegate (Managed Server, NodeManager), l'applicazione apre la finestra modale **`Eliminazione Machine & Reassegnazione Risorse`**. È possibile selezionare su quale Machine target rimanente riassegnare le risorse prima dell'eliminazione.
- **`📉 CONSOLIDA MACHINE`**: Mostra un popup con una casella di testo precompilata per ciascuna Machine rilevata nella griglia. Modificando i nomi e confermando, viene aggiornata l'intera griglia e tutte le risorse collegate.
- **`➕ AGGIUNGI MACHINE`**: Apre la finestra per creare una nuova Machine target e selezionare tramite checkbox quali risorse del dominio associarvi immediatamente.

### 4.3 Validazione Multi-Target e Modal Interattivo di Correzione
Cliccando su **`VALIDA MAPPATURE`**:
1. Il motore verifica la coerenza di porte, nomi e target. Per i DataSources e le Applicazioni con target multipli separati da virgola (es. `cluster1,cluster2,server1`), ogni elemento viene controllato ed approvato **senza falsi positivi**.
2. In caso di incongruenze reali, si apre il popup modale **`🔧 Correzione Mappature Non Valide`**:
   - **Tabella a sinistra**: Elenca **solo le righe che contengono errori** con la descrizione puntuale dell'incongruenza.
   - **Ispettore Proprietà a destra**: Permette di modificare il Nuovo Nome Target, le Porte, la Machine ed i Cluster/Server tramite menu a tendina e pulsante **`💾 APPLICA MODIFICA A QUESTA RIGA`**.
   - Cliccando su **`💾 SALVA E SINCRONIZZA CON GRIGLIA PRINCIPALE`**, tutte le correzioni vengono applicate automaticamente alla griglia principale.

### 4.4 Visualizzazioni Grafiche & Esportazione PNG
La sezione di destra della Scheda 2 offre 4 viste dinamiche aggiornate in tempo reale:
- ⚙️ **Ispettore Proprietà**: Pannello di modifica rapida del singolo elemento selezionato.
- 🎨 **Diagramma Draw.io (Interattivo)**: Vista 2D vettoriale con drag & drop libero delle card ed unione tramite frecce di Bézier.
- 🧩 **Vista Architetturale (Blocchi)**: Contenitori visuali di Machine e Cluster con supporto **Zoom In (+)**, **Zoom Out (-)**, **100%** e pulsante **`📸 SALVA SCHERMATA (PNG)`** per esportare l'immagine dell'architettura.
- 🌳 **Gerarchia Target**: Albero ad espansione dinamica dell'intera struttura del dominio target.

---

## 5. Scheda 3: Ispezione Target, Generazione Task & Deploy Remoto

### 🔍 Ispezione Target in Tempo Reale
Il pulsante **`SCARICA ELEMENTI DI DOMINIO (WEBLOGIC TARGET)`** permette di connettersi via SSH al Server B (Target) ed estrarerne la configurazione in tempo reale per visualizzarla nell'albero di destra.

### 📦 Generazione Pacchetti Task Offline
Cliccando su **`GENERA PACCHETTO TASK NUMERATO`**, il tool crea nella cartella `deploy/` una sotto-cartella standalone (es. `task_001/`) contenente:
- `deploy_topology.py`: Script WLST per la creazione di Machine, Cluster, Managed Server e DataSources JDBC (partizionato in lotti da 15 elementi anti-64KB limit).
- `deploy_apps.py`: Script WLST per il deploy applicativo e delle Librerie Condivise (`libraryModule='true'`).
- `apps/`: Cartella contenente i file binari `.war`, `.ear`, `.jar`.
- `run_migration.sh` / `run_migration.cmd`: Esecutori automatici per ambienti Linux e Windows.

---

## 6. FAQ & Risoluzione Problemi

### ❓ Perché le schede 1, 2 e 3 sono disattivate all'avvio?
All'avvio occorre prima selezionare un lavoro esistente o crearne uno nuovo usando i pulsanti verdi in alto a sinistra.

### ❓ Come si esporta la schermata dell'architettura?
Andare nella Scheda 2 -> sotto-scheda `🧩 Vista Architetturale (Blocchi)` e cliccare sul pulsante **`📸 SALVA SCHERMATA (PNG)`**.

---
*Per ulteriore documentazione tecnica sull'architettura e sugli MBean WebLogic, consultare la [📚 Wiki del Progetto](WIKI.md).*
