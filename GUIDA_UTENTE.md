# 📖 Guida Utente Operativa - WebLogic Migration Tool (v3.9.0)

<p align="center">
  <b>Sviluppatore: Alessandro Caliciotti</b> | <i>Nimis Consulting Information Technologies</i>
</p>

---

## 📋 Indice dei Contenuti
1. [Panoramica ed Avvio Applicazione](#1-panoramica-ed-avvio-applicazione)
2. [Gestione Lavori e Cartella `works/`](#2-gestione-lavori-e-cartella-works)
3. [Scheda 1: Connessione, Profili & Dump Sorgente](#3-scheda-1-connessione-profili--dump-sorgente)
4. [Scheda 2: Rinomina, Mappature e Gestione Avanzata Machine & Cluster](#4-scheda-2-rinomina-mappature-e-gestione-avanzata-machine--cluster)
   - [4.1 Griglia di Mappatura (A -> B)](#41-griglia-di-mappatura-a---b)
   - [4.2 Gestione Intelligente Machine & Cluster](#42-gestione-intelligente-machine--cluster)
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

---

## 2. Gestione Lavori e Cartella `works/`

Alla prima apertura dell'applicazione, le schede operative **1, 2 e 3 sono disattivate** finché l'utente non seleziona o crea un **Lavoro di Migrazione Attivo**.

```
works/
├── 001_Migrazione_PROD_11g_12c/
│   ├── dump/             -> File JSON e dump estratti dal Server Sorgente (Server A)
│   ├── deploy/           -> Pacchetti di task numerati generati per il Target (Server B)
│   ├── target_dumps/     -> Ispezione in tempo reale del Dominio Target (Server B)
│   └── prj_saves/        -> File salvati di progetto mappatura (.wlsmap)
```

---

## 3. Scheda 1: Connessione, Profili & Dump Sorgente

- menu **PROFILO CONNESSIONE SALVATO** sincronizzato in tempo reale.
- **Estrazione SSH**: Scaricamento automatico della topologia, decifrazione password JDBC e download delle **Librerie Condivise** e delle applicazioni nella cartella `dump/`.

---

## 4. Scheda 2: Rinomina, Mappature e Gestione Avanzata Machine & Cluster

### 4.1 Griglia di Mappatura (A -> B)
Rinomina e riassegnazione dinamica per Machine, Cluster, Managed Server, DataSources JDBC e Applicazioni / Librerie.

### 4.2 Gestione Intelligente Machine & Cluster
- **`🗑️ ELIMINA RIGA SELEZIONATA` su MACHINE**: Se la macchina possiede risorse collegate (Server, NodeManager), apre la finestra **`Eliminazione Machine & Reassegnazione Risorse`**.
- **`🗑️ ELIMINA RIGA SELEZIONATA` su CLUSTER**: Se si seleziona una riga Cluster collegata a Managed Server, DataSources o Applicazioni (inclusi target multipli), il tool apre la finestra modale **`🌐 Eliminazione Cluster & Gestione Target Risorse`** con le seguenti opzioni:
  1. 🧹 **`Rimuovi solo il Cluster dai Target (Smart Multi-Target Cleanup)`**: Rimuove puntualmente il Cluster eliminato dalle stringhe di target multipli (es. `clusterA,clusterB` -> `clusterB`), lasciando intatti tutti gli altri target!
  2. 🔀 **`Riassegna tutte le risorse ad un altro Cluster`**: Sposta la destinazione delle risorse su un Cluster target selezionato da menu a tendina.
  3. 🗑️ **`Elimina anche le righe di tutte le risorse collegate`**: Rimuove dalla griglia tutte le risorse che appartenevano a quel Cluster.

---

## 5. Scheda 3: Ispezione Target, Generazione Task & Deploy Remoto

Generazione pacchetti task `task_xxx/` con partizionamento anti-64KB limit e runner per Linux (`run_migration.sh`) e Windows (`run_migration.cmd`).
