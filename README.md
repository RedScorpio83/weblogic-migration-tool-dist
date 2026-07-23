# WebLogic Configuration & Application Migration Tool

<p align="center">
  <img src="logo.png" alt="Nimis Consulting Information Technologies" width="300"/>
</p>

<p align="center">
  <b>Version 3.9.0 (FlatLaf Gold)</b> | Sviluppatore: <i>Alessandro Caliciotti</i> | <b>Nimis Consulting Information Technologies</b>
</p>

---

## 📖 Documentazione Rapida & Link Utili

- 📖 **[Guida Utente Operativa Passo-Passo (GUIDA_UTENTE.md)](GUIDA_UTENTE.md)** - Guida esaustiva con spiegazione di tutti i pulsanti ed i comandi dell'applicazione.
- 📚 **[Wiki del Progetto & Architettura Tecnica (WIKI.md)](WIKI.md)** - Documentazione approfondita sull'architettura interna, MBean WebLogic, Jython AST e partizionamento anti-64KB.

---

## 🌐 Language / Lingua

- 🇮🇹 [Italiano](#-italiano)
- 🇬🇧 [English](#-english)

---

## 🇮🇹 Italiano

### 📌 Panoramica del Software
Il **WebLogic Migration Tool** è una soluzione software enterprise progettata per automatizzare l'estrazione, la migrazione e la replicazione della topologia e delle applicazioni fra ambienti **Oracle WebLogic Server (11g/12c)**.

---

### ✨ Funzionalità Operative e Strumenti (Catalogo Features)

#### 1. 💻 Gestione Schermo Intero & Lavori Standalone (`works/`)
- **Avvio Massimizzato**: Avvio automatico a schermo intero (`MAXIMIZED_BOTH`).
- **Pulsante `📁 CARICA LAVORO DI DESTINAZIONE`**: Seleziona un lavoro attivo dalla cartella `works/` sbloccando le schede 1, 2 e 3.
- **Pulsante `➕ NUOVO LAVORO`**: Crea un lavoro numerato progressivamente (es. `001_NomeLavoro`).
- **Pulsante `🧹 PULISCI TASK E DUMP`**: Gestore grafico dei lavori con possibilità di eliminazione singola tramite icona del cestino.

#### 2. 🔌 Estrazione SSH, Profili Bidirezionali & Dump Offline (Scheda 1)
- **Menu Profili Sincronizzati**: Sincronizzazione automatica bidirezionale dei profili di connessione sorgente e target.
- **Pulsante `SALVA CONFIGURAZIONE` & `GESTORE CONNESSIONI`**: Salva e gestisce i profili in `connections_profiles.json`.
- **Pulsante `🚀 ESTRAZIONE REMOTA SSH`**: Scansione remota del server sorgente, decifrazione automatica password JDBC e download delle **Librerie Condivise** e delle app.
- **Pulsante `📦 GENERA PACCHETTO ESTRAZIONE OFFLINE`**: Genera script ed esecutori per server sorgente isolati.

#### 3. 🧠 Gestione Intelligente Machine & Cluster (Scheda 2)
- **Pulsante `🗑️ ELIMINA RIGA SELEZIONATA`**:
  - **Smart Machine Deletion**: Se la Machine possiede risorse collegate, apre il popup per riassegnarle prima della cancellazione.
  - **Smart Cluster Deletion**: Per i Cluster con risorse collegate, offre la funzione **`Smart Multi-Target Cleanup`** (rimuove il cluster dai target multipli senza toccare gli altri target), la riassegnazione ad un altro cluster o l'eliminazione delle risorse.
- **Pulsante `📉 CONSOLIDA MACHINE`**: Popup con caselle di testo precompilate per ciascuna Machine per la rinomina globale in 1-click.
- **Pulsante `➕ AGGIUNGI MACHINE`**: Popup per definire una nuova Machine target e selezionare le risorse da associarvi tramite checkbox.

#### 4. 🔀 Validazione Multi-Target & Modal Interattivo di Correzione (Scheda 2)
- **Pulsante `VALIDA MAPPATURE`**: Verificatore di coerenza con supporto ai target multipli separati da virgola (es. `cluster1,cluster2`).
- **Modal Modale `🔧 Correzione Mappature Non Valide`**: In caso di errori, mostra la tabella delle righe errate a sinistra e l'**Ispettore Proprietà Elemento** a destra per la correzione guidata e la sincronizzazione in 1-click.
- **Pulsante `PORTE DUPLICATE`**: Identifica e segnala conflitti sulle porte dei Managed Server.
- **Pulsante `🔄 CAMBIA OCCORRENZE`**: Trova & Sostituisci globale di testo nella griglia.
- **Pulsante `.. ADATTA COLONNE`**: Auto-ridimensiona la larghezza delle colonne della tabella.

#### 5. 🎨 Viste Grafiche, Zoom & Esportazione PNG (Scheda 2)
- **Sotto-scheda `⚙️ Ispettore Proprietà`**: Modifica rapida dell'elemento con pulsante `💾 APPLICA MODIFICHE PROPRIETÀ`.
- **Sotto-scheda `🎨 Diagramma Draw.io`**: Diagramma 2D vettoriale con pulsanti `🔍 Zoom +`, `🔍 Zoom -`, `🎯 100%`, `📐 ADATTA A SCHERMATA` e `📊 ALLINEA TOP-DOWN CENTRATO`.
- **Sotto-scheda `🧩 Vista Architetturale (Blocchi)`**: Contenitori visuali con pulsanti `🔍 Zoom +`, `🔍 Zoom -`, `🎯 100%` e **`📸 SALVA SCHERMATA (PNG)`** per esportare l'immagine dell'architettura in alta definizione.
- **Sotto-scheda `🌳 Gerarchia Target`**: Albero ad espansione dinamica del dominio.

#### 6. 📦 Ispezione Target, Generatore Task & Deploy Remoto (Scheda 3)
- **Pulsante `SCARICA ELEMENTI DI DOMINIO (WEBLOGIC TARGET)`**: Connessione ed ispezione in tempo reale del server target B.
- **Pulsante `🚀 ESECUZIONE SSH REMOTA SU WEBLOGIC 12C`**: Esecuzione remota via SSH degli script topology ed applicativi.
- **Pulsante `📦 GENERA PACCHETTO TASK NUMERATO`**: Genera cartelle standalone `task_xxx/` con partizionamento anti-64KB limit, cartella `apps/` e runner `run_migration.sh` / `run_migration.cmd`.

---

### 🚀 Istruzioni per l'Installazione ed Avvio

1. **Clonare il Repository**:
   ```bash
   git clone https://github.com/RedScorpio83/weblogic-migration-tool-dist.git
   cd weblogic-migration-tool-dist
   ```
2. **Avvio su Windows**:
   Fare doppio click su `run.cmd`.
3. **Avvio su Linux / macOS**:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

---

## 🇬🇧 English

### 📌 Software Overview
**WebLogic Migration Tool** is an enterprise software platform designed to extract, migrate, and replicate topology and applications between **Oracle WebLogic Server (11g/12c)** environments.

- **Complete User Guide**: Refer to **[GUIDA_UTENTE.md](GUIDA_UTENTE.md)** for a detailed walkthrough of all GUI buttons and operational controls.

---
*Developed by Alessandro Caliciotti - Nimis Consulting Information Technologies*
