# 📖 Guida Utente Operativa - WebLogic Migration Tool (v3.9.0)

<p align="center">
  <b>Sviluppatore: Alessandro Caliciotti</b> | <i>Nimis Consulting Information Technologies</i>
</p>

---

## 📋 Indice dei Contenuti
1. [Panoramica ed Avvio Applicazione](#1-panoramica-ed-avvio-applicazione)
2. [Gestione Lavori e Cartella `works/`](#2-gestione-lavori-e-cartella-works)
3. [Guida Dettagliata ai Pulsanti della Barra Superiore](#3-guida-dettagliata-ai-pulsanti-della-barra-superiore)
4. [Scheda 1: Estrazione Sorgente via SSH (Da A)](#4-scheda-1-estrazione-sorgente-via-ssh-da-a)
5. [Scheda 2: Rinomina, Mappature e Gestione Avanzata Machine & Cluster](#5-scheda-2-rinomina-mappature-e-gestione-avanzata-machine--cluster)
   - [5.1 Pulsanti della Toolbar di Mappatura](#51-pulsanti-della-toolbar-di-mappatura)
   - [5.2 Pulsanti dell'Ispettore Proprietà e delle Viste Grafiche](#52-pulsanti-dellispettore-proprieta-e-delle-viste-grafiche)
   - [5.3 Pulsanti della Barra Inferiore (Eliminazione Intelligente & Conferma)](#53-pulsanti-della-barra-inferiore)
6. [Scheda 3: Ispezione Target, Generazione Task & Deploy Remoto](#6-scheda-3-ispezione-target-generazione-task--deploy-remoto)
7. [FAQ & Risoluzione Problemi](#7-faq--risoluzione-problemi)

---

## 1. Panoramica ed Avvio Applicazione

Il **WebLogic Migration Tool** è una piattaforma enterprise ideata per automatizzare l'estrazione, la ri-mappatura ed il deploy di domini **Oracle WebLogic Server (11g/12c)**.

### 🚀 Avvio
- **Windows**: Eseguire `run.cmd` (o fare doppio click su `MigrationTool.jar`).
- **Linux / macOS**: Eseguire `./run.sh` da terminale.

> [!NOTE]
> L'applicazione si avvia automaticamente **a schermo intero (massimizzata)** per facilitare la gestione di griglie complesse e viste architetturali.

---

## 2. Gestione Lavori e Cartella `works/`

All'avvio, le schede **1, 2 e 3 sono disattivate** finché l'utente non seleziona un lavoro attivo dalla cartella `works/`.

```
works/
└── 001_Migrazione_PROD_11g_12c/
    ├── dump/          -> Dump JSON ed archivi binari (.war, .ear) estratti dal Sorgente A
    ├── deploy/        -> Task di deploy generati (task_001/ con script WLST)
    ├── target_dumps/  -> Ispezioni in tempo reale del Dominio Target B
    └── prj_saves/     -> Salvataggi progetti (.wlsmap) e schermate architetturali PNG
```

---

## 3. Guida Dettagliata ai Pulsanti della Barra Superiore

In alto a destra nell'interfaccia principale sono sempre presenti i seguenti pulsanti di controllo globale:

- **`☑ Bypass Proxy`**: Checkbox per attivare o disattivare l'uso dei proxy di rete aziendali durante le chiamate SSH e le connessioni esterne.
- **`SELEZIONA LAVORO ATTIVO` / `📁 CARICA LAVORO DI DESTINAZIONE`** *(Pulsante Verde)*: Apre la finestra di dialogo per scegliere una cartella di lavoro esistente presente sotto `works/`. Abilita istantaneamente le Schede 1, 2 e 3.
- **`➕ NUOVO LAVORO`**: Permette di creare una nuova cartella di lavoro numerata progressivamente (es. `002_Collaudo_12c`) inizializzando le sotto-cartelle operative.
- **`🧹 PULISCI TASK E DUMP`** *(Pulsante Rosso in alto a destra)*: Apre il gestore dei lavori per visualizzare l'elenco delle cartelle in `works/` ed eliminarle definitivamente con un click sull'icona del cestino.

---

## 4. Scheda 1: Estrazione Sorgente via SSH (Da A)

### 🔘 Pulsanti e Controlli della Scheda 1:
- **Menu a tendina `PROFILO CONNESSIONE SALVATO`**: Permette di selezionare un profilo di connessione precedentemente salvato. Popola istantaneamente sia i campi sorgente della Scheda 1 sia quelli target della Scheda 3.
- **`SALVA CONFIGURAZIONE`**: Salva le credenziali ed i parametri SSH/WebLogic inseriti nel file locale `connections_profiles.json`.
- **`GESTORE CONNESSIONI`**: Apre la finestra modale per modificare, rinominare ed eliminare i profili di connessione salvati.
- **`☑ Copia pacchetti applicativi fisici (.war/.ear/cartelle)`**: Se spuntato, durante l'estrazione SSH oltre alla topologia WebLogic verranno scaricati sul disco locale anche gli archivi binari `.war`, `.ear` e le **Librerie Condivise**.
- **`🚀 ESTRAZIONE REMOTA SSH (SERVER LINUX)`** *(Pulsante Oro)*: Connette l'applicazione al server sorgente via SSH, esegue lo script WLST di estrazione in background e mostra un overlay di caricamento stile Apple.
- **`📦 GENERA PACCHETTO ESTRAZIONE OFFLINE`**: Genera nella cartella `extractions_tools/dump_tool_xxx/` un pacchetto standalone pronto per essere eseguito su server sorgente isolati.

---

## 5. Scheda 2: Rinomina, Mappature e Gestione Avanzata Machine & Cluster

La Scheda 2 consente di ridefinire nomi, porte, machine e target prima della migrazione.

### 5.1 Pulsanti della Toolbar di Mappatura
- **`💾 SALVA PROGETTO`**: Esporta la configurazione ed i nomi mappati in un file `.wlsmap` all'interno della cartella `prj_saves/`.
- **`📂 CARICA PROGETTO`**: Importa un file `.wlsmap` precedentemente salvato per ripristinare le mappature.
- **`VALIDA MAPPATURE`**: Esegue il motore di validazione per verificare coerenza di porte e target. Supporta i target multipli separati da virgola (es. `cluster1,cluster2`). Se rileva errori, apre la finestra modale **`🔧 Correzione Mappature Non Valide`** con tabella delle righe errate ed Ispettore Proprietà per la correzione e sincronizzazione in 1-click.
- **`PORTE DUPLICATE`**: Analizza le porte di ascolto dei Managed Server e segnala eventuali conflitti o duplicazioni.
- **`📉 CONSOLIDA MACHINE`**: Apre la finestra modale contenente una casella di testo precompilata per ciascuna Machine rilevata. Modificando i nomi e confermando, l'intera griglia viene aggiornata.
- **`➕ AGGIUNGI MACHINE`**: Apre il popup per creare una nuova Machine target (UnixMachine / Machine) e selezionare tramite checkbox quali risorse associarvi.
- **`🔄 CAMBIA OCCORRENZE`**: Apre la finestra di Trova & Sostituisci globale per cercare e sostituire stringhe di testo in tutta la griglia.
- **`.. ADATTA COLONNE`**: Auto-ridimensiona le larghezze delle colonne della griglia in base alla lunghezza del testo contenuto.

---

### 5.2 Pulsanti dell'Ispettore Proprietà e delle Viste Grafiche

#### ⚙️ Sotto-scheda Ispettore Proprietà (Pannello Destro)
- **`💾 APPLICA MODIFICHE PROPRIETÀ`**: Applica i valori inseriti nei campi dell'ispettore (Nuovo Nome, Porta/Pass DB, Machine, Cluster) alla riga attualmente selezionata nella tabella.

#### 🎨 Sotto-scheda Diagramma Draw.io (Interattivo)
- **`🔍 Zoom +`**: Ingrandisce il canvas 2D vettoriale.
- **`🔍 Zoom -`**: Rimpicciolisce il canvas del diagramma.
- **`🎯 100%`**: Ripristina il livello di zoom standard al 100%.
- **`📐 ADATTA A SCHERMATA`**: Adatta automaticamente la scala del diagramma alle dimensioni della finestra.
- **`📊 ALLINEA TOP-DOWN CENTRATO`**: Ridispone automaticamente tutte le card (Machine, Cluster, Server, App) secondo una gerarchia top-down centrata.

#### 🧩 Sotto-scheda Vista Architetturale (Blocchi)
- **`🔍 Zoom +`**: Aumenta le dimensioni dei blocchi architetturali.
- **`🔍 Zoom -`**: Diminuisce le dimensioni dei blocchi architetturali.
- **`🎯 100%`**: Resetta lo zoom dei blocchi.
- **`📸 SALVA SCHERMATA (PNG)`** *(Pulsante Oro)*: Cattura l'intero canvas architetturale e lo salva come file immagine ad alta definizione `.png`.

---

### 5.3 Pulsanti della Barra Inferiore
- **`🗑️ ELIMINA RIGA SELEZIONATA`** *(Pulsante Rosso)*:
  - **Eliminazione Intelligente Machine**: Se la machine eliminata possiede risorse collegate, apre il dialog **`Eliminazione Machine & Reassegnazione Risorse`** per selezionare la nuova machine di destinazione.
  - **Eliminazione Intelligente Cluster**: Se il cluster possiede risorse collegate (Server, DataSources, Applicazioni), apre il dialog **`🌐 Eliminazione Cluster & Gestione Target Risorse`** offrendo 3 opzioni:
    1. 🧹 **Smart Multi-Target Cleanup**: Rimuove puntualmente il Cluster dalle stringhe target mantenendo gli altri target intact (es. `clusterA,clusterB` -> `clusterB`).
    2. 🔀 **Riassegna ad un altro Cluster**: Permette di selezionare un altro Cluster di destinazione.
    3. 🗑️ **Elimina righe risorse collegate**: Rimuove anche le righe delle risorse collegate.
- **`CONFERMA MAPPATURE E RINOMINE`** *(Pulsante Oro)*: Salva tutte le modifiche della griglia nel modello in memoria ed effettua l'autosalvataggio in `prj_saves/progetto_migrazione.wlsmap`.

---

## 6. Scheda 3: Ispezione Target, Generazione Task & Deploy Remoto

### 🔘 Pulsanti e Controlli della Scheda 3:
- **`SCARICA ELEMENTI DI DOMINIO (WEBLOGIC TARGET)`** *(Pulsante Oro)*: Si connette via SSH al Server B (Target), estrae la configurazione in tempo reale del dominio di destinazione e la visualizza nell'albero ad espansione a destra.
- **`☑ Esegui Deploy Applicativi (WAR, EAR, Librerie Condivise)`**: Se spuntato, include le applicazioni e le librerie condivise nel deploy remoto e nei pacchetti task.
- **`🚀 ESECUZIONE SSH REMOTA SU WEBLOGIC 12C`** *(Pulsante Oro)*: Esegue in sequenza via SSH gli script `deploy_topology.py` e `deploy_apps.py` sul server target WebLogic 12c.
- **`📦 GENERA PACCHETTO TASK NUMERATO`** *(Pulsante Oro)*: Crea nella sotto-cartella `deploy/` un pacchetto standalone (es. `task_001/`) contenente gli script WLST partizionati anti-64KB, la cartella `apps/` ed i runner `run_migration.sh` / `run_migration.cmd`.

---

## 7. FAQ & Risoluzione Problemi

### ❓ Come si utilizzano le funzioni di Zoom e Screenshot?
Andare nella Scheda 2, selezionare la sotto-scheda `🧩 Vista Architetturale (Blocchi)` o `🎨 Diagramma Draw.io` ed utilizzare i pulsanti **Zoom +, Zoom -, 100%** e **`📸 SALVA SCHERMATA (PNG)`**.

---
*Nimis Consulting Information Technologies - Alessandro Caliciotti*
