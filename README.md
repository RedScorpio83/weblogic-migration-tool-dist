# WebLogic Configuration & Application Migration Tool

<p align="center">
  <img src="logo.png" alt="Nimis Consulting Information Technologies" width="320"/>
</p>

<p align="center">
  <b>Version 4.0.0 (FlatLaf Gold Enterprise)</b> | Sviluppatore: <i>Alessandro Caliciotti</i> | <b>Nimis Consulting Information Technologies</b>
</p>

---

## 📖 Documentazione Rapida & Link Utili

- 📖 **[Guida Utente Operativa Passo-Passo (GUIDA_UTENTE.md)](GUIDA_UTENTE.md)** - Manuale utente completo con catalogo esaustivo di tutti i pulsanti e le schermate dell'applicazione.
- 📚 **[Wiki del Progetto & Architettura Tecnica (WIKI.md)](WIKI.md)** - Documentazione approfondita sull'architettura interna, MBean WebLogic, Jython AST, partizionamento anti-64KB e workflow `pack/unpack`.

---

## 🌐 Language / Lingua

- 🇮🇹 [Italiano](#-italiano)
- 🇬🇧 [English](#-english)

---

## 🇮🇹 Italiano

### 📌 Panoramica del Software
Il **WebLogic Migration Tool** è una soluzione software enterprise progettata per automatizzare l'estrazione, la ri-mappatura, la migrazione e la replicazione della topologia e delle applicazioni fra ambienti **Oracle WebLogic Server (11g/12c)**.

Dalla versione **4.0.0**, la piattaforma integra il nuovo modulo di **Provisioning Bare-Metal Zero-to-Hero**, consentendo di trasformare server Linux totalmente puliti in cluster WebLogic 12c operativi in 1-Click via SSH o tramite pacchetti task esportabili.

---

### ✨ Catalogo Completo delle Funzionalità Enterprise (v4.0.0)

#### 1. 🛠️ Modulo Provisioning Bare-Metal WebLogic 12c & Setup Nodi (Fase 0)
- **Doppia Modalità di Esecuzione (ROOT vs ORACLE)**:
  - 🔴 **Modalità ROOT**: Crea automaticamente la struttura di directory, il gruppo `oinstall`, l'utente `oracle`, assegna i permessi `chown -R oracle:oinstall` e gestisce l'eventuale remount di `/tmp` (con flag `exec`).
  - 🟡 **Modalità UTENTE ORACLE**: Esegue il setup lavorando con i permessi dell'utente `oracle` senza richiedere comandi root di sistema.
- **Preset Alberatura Target (OFA Standard)**:
  - **STANDARD EDG (`/u01/app/oracle/...`)**: Rispetta al 100% l'Enterprise Deployment Guide ufficiale Oracle.
  - **CUSTOM**: Consente la personalizzazione completa di tutti i percorsi radice.
- **Installazione Silenziosa JDK & WLS**:
  - Trasferimento SFTP ed estrazione automatica del JDK Linux e silent install di WebLogic Server 12c (`silent_install.rsp` + `oraInst.loc`).
- **Creazione Dominio & Security `boot.properties`**:
  - Generazione WLST Offline del dominio base ed autocomposizione del file `servers/AdminServer/security/boot.properties` per consentire l'avvio in background dell'AdminServer senza prompt password.
- **Propagazione del Dominio sui Nodi Secondari (`pack` & `unpack`)**:
  - Generazione automatica del template `domain_managed.jar` tramite **`pack.sh`** prima dell'avvio dell'AdminServer.
  - Trasferimento SFTP ed esecuzione di **`unpack.sh`** su ciascun nodo secondario Machine per la ricreazione dinamica del dominio.
- **Setup & Avvio NodeManager sui Nodi**:
  - Configurazione automatica di `nodemanager.properties` (porta 5556, `Plain`/`SSL`) e `nodemanager.domains` con avvio in background su tutti i nodi.
- **Esecuzione 1-Click SSH con Log in Tempo Reale**:
  - Pulsante **`🚀 ESEGUI PROVISIONING REMOTO IN 1-CLICK (SSH)`** con overlay di caricamento stile Apple e diretta nella console verde delle attività.

#### 2. 🧠 Gestione Intelligente Machine & Cluster (Multi-Target Cleanup)
- **Eliminazione Intelligente Machine**: Rileva le risorse collegate (Server, NodeManager) alla Machine in eliminazione proponendo la finestra modale per la riassegnazione prima della cancellazione.
- **Eliminazione Intelligente Cluster & Smart Multi-Target Cleanup**: Se si elimina un Cluster con risorse collegate (DataSources, App con target multipli come `clusterA,clusterB`), offre l'opzione per **rimuovere puntualmente il solo cluster eliminato** mantenendo intatti gli altri target!
- **Consolida Machine**: Caselle di testo precompilate per ciascuna Machine per la rinomina globale in 1-click.
- **Aggiungi Machine**: Popup per definire una nuova Machine target e selezionare le risorse da associarvi tramite checkbox.

#### 3. 🔀 Validazione Multi-Target & Modal Interattivo di Correzione
- **Validatore Coerenza Mappature**: Riconosce i target multipli separati da virgola senza generare falsi errori.
- **Modal Modale `🔧 Correzione Mappature Non Valide`**: Mostra la tabella delle sole righe errate a sinistra e l'**Ispettore Proprietà Elemento** a destra per la correzione guidata e la sincronizzazione in 1-click sulla griglia principale.

#### 4. 🎨 Viste Architetturali Grafiche, Zoom & Esportazione HD PNG
- **Diagramma 2D Draw.io**: Rendering vettoriale con Zoom +, Zoom -, 100%, Adatta a Schermata ed Allineamento Top-Down Centrato.
- **Vista Architetturale a Blocchi**: Visualizzazione moderna dei blocchi contenitori con pulsante **`📸 SALVA SCHERMATA (PNG)`** per esportare l'immagine dell'architettura in alta definizione.

#### 5. 📂 Gestione Lavori Standalone (`works/`)
- Organizzazione automatica in sotto-cartelle isolate (`works/001_xxx`) contenenti `dump/`, `deploy/`, `target_dumps/` e `prj_saves/`.
- Pulsante **`🧹 PULISCI TASK E DUMP`** per la gestione ed eliminazione visiva dei lavori.

#### 6. 🔒 Hardening di Sicurezza & Protezione Bytecode
- Partizionamento degli script Python in lotti da 15 elementi per evitare il limite di 64KB bytecode della JVM.
- Decifrazione automatica delle password dei DataSources JDBC cifrate con `XMLEncryptionSecret`.

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
- **Technical Architecture**: Refer to **[WIKI.md](WIKI.md)** for internally used MBeans, Jython AST partitioning, and `pack/unpack` workflow details.

---
*Developed by Alessandro Caliciotti - Nimis Consulting Information Technologies*
