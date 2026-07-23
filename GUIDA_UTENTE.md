# 📖 Guida Utente Operativa - WebLogic Migration Tool (v4.0.0)

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
6. [Scheda 3: Ispezione Target, Generazione Task & Deploy Remoto](#6-scheda-3-ispezione-target-generazione-task--deploy-remoto)
7. [Modulo Provisioning Bare-Metal WebLogic 12c & Setup Nodi](#7-modulo-provisioning-bare-metal-weblogic-12c--setup-nodi)
8. [FAQ & Risoluzione Problemi](#8-faq--risoluzione-problemi)

---

## 1. Panoramica ed Avvio Applicazione

Il **WebLogic Migration Tool** è una piattaforma enterprise ideata per automatizzare l'estrazione, la ri-mappatura, la migrazione ed il provisioning di domini **Oracle WebLogic Server (11g/12c)**.

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
└── 001_Migrazione_Enterprise/
    ├── dump/          -> Dump JSON ed archivi binari (.war, .ear) estratti dal Sorgente A
    ├── deploy/        -> Task di deploy e provisioning generati (task_001/, infra_task_001/)
    ├── target_dumps/  -> Ispezioni in tempo reale del Dominio Target B
    └── prj_saves/     -> Salvataggi progetti (.wlsmap) e schermate architetturali PNG
```

---

## 3. Guida Dettagliata ai Pulsanti della Barra Superiore

- **`☑ Bypass Proxy`**: Attiva o disattiva l'uso dei proxy aziendali durante le chiamate SSH.
- **`SELEZIONA LAVORO ATTIVO` / `📁 CARICA LAVORO DI DESTINAZIONE`**: Seleziona una cartella di lavoro esistente under `works/`.
- **`➕ NUOVO LAVORO`**: Crea una nuova cartella di lavoro numerata progressivamente.
- **`🧹 PULISCI TASK E DUMP`**: Gestore visivo dei lavori per la cancellazione singola tramite icona del cestino.

---

## 4. Scheda 1: Estrazione Sorgente via SSH (Da A)

- **Menu `PROFILO CONNESSIONE SALVATO`**: Caricamento rapido credenziali sorgente e target.
- **`SALVA CONFIGURAZIONE` & `GESTORE CONNESSIONI`**: Salvataggio profili in `connections_profiles.json`.
- **`☑ Copia pacchetti applicativi fisici (.war/.ear/cartelle)`**: Scarica gli archivi applicativi e le **Librerie Condivise**.
- **`🚀 ESTRAZIONE REMOTA SSH (SERVER LINUX)`**: Scansione remota con overlay di caricamento stile Apple.
- **`📦 GENERA PACCHETTO ESTRAZIONE OFFLINE`**: Genera il pacchetto standalone `dump_tool_xxx/` per server isolati.

---

## 5. Scheda 2: Rinomina, Mappature e Gestione Avanzata Machine & Cluster

- **`VALIDA MAPPATURE`**: Risolve i target multipli separati da virgola ed apre il modal **`🔧 Correzione Mappature Non Valide`** con Ispettore Proprietà per correzione guidata.
- **`🗑️ ELIMINA RIGA SELEZIONATA`**:
  - **Machine**: Dialog **`Eliminazione Machine & Reassegnazione Risorse`**.
  - **Cluster**: Dialog **`🌐 Eliminazione Cluster & Gestione Target Risorse`** con opzione **`Smart Multi-Target Cleanup`** (rimuove il solo cluster eliminato dai target multipli senza toccare gli altri!).
- **`📉 CONSOLIDA MACHINE`**: Rinomina globale Machine via caselle per-machine.
- **`➕ AGGIUNGI MACHINE`**: Crea nuove machine target associando risorse via checkbox.
- **`📸 SALVA SCHERMATA (PNG)`**: Esporta l'immagine HD dell'architettura in formato PNG.

---

## 6. Scheda 3: Ispezione Target, Generazione Task & Deploy Remoto

- **`SCARICA ELEMENTI DI DOMINIO (WEBLOGIC TARGET)`**: Connessione ed ispezione in tempo reale del Server Target B.
- **`🚀 ESECUZIONE SSH REMOTA SU WEBLOGIC 12C`**: Deploy SSH della topologia e delle app.
- **`📦 GENERA PACCHETTO TASK NUMERATO`**: Genera cartelle standalone `task_xxx/` con partizionamento anti-64KB limit.

---

## 7. Modulo Provisioning Bare-Metal WebLogic 12c & Setup Nodi

Attivabile dal pulsante **`🛠️ PROVISIONING WEBLOGIC 12C & NODI (BARE-METAL)`** nella Scheda 3:

### Passi del Wizard:
1. **Modalità OS**:
   - `🔴 ROOT`: Creazione utenti `oracle:oinstall`, cartelle e remount `/tmp`.
   - `🟡 UTENTE ORACLE`: Setup lavorando direttamente con i permessi dell'utente `oracle`.
2. **Alberatura Target (OFA)**:
   - `STANDARD EDG (/u01/app/oracle/...)`
   - `CUSTOM` (Percorso radice personalizzabile).
3. **Binari**: Selezione JDK Linux `.tar.gz` e WLS 12c `.jar/.zip`.
4. **Dominio & AdminServer**: Nome dominio, porta `7001`, credenziali AdminServer.
5. **Nodi Secondari Machine**: Tabella per definire IP SSH, Hostname, porta NodeManager `5556` e tipo (`Plain`/`SSL`).

### Pulsanti Azione:
- **`📦 GENERA PACCHETTO TASK INFRASTRUTTURA`**: Genera il pacchetto `infra_task_001/` pronto per macchine offline.
- **`🚀 ESEGUI PROVISIONING REMOTO IN 1-CLICK (SSH)`**: Esegue l'installazione completa remota via SSH su AdminServer e Nodi Secondari, propagando il dominio via **`pack.sh` / `unpack.sh`** e mostrando i log in tempo reale nella console verde in basso.

---

## 8. FAQ & Risoluzione Problemi

### ❓ I passi del provisioning vengono mostrati nella console dell'app?
Sì! Tutti i comandi SSH, l'estrazione JDK, il silent install WLS, il `pack.sh`, l'unpack ed l'avvio del NodeManager sui nodi vengono trasmessi in tempo reale nella **Console Log verde in basso**.

---
*Nimis Consulting Information Technologies - Alessandro Caliciotti*
