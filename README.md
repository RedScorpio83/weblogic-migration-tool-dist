# WebLogic Configuration & Application Migration Tool

<p align="center">
  <img src="logo.png" alt="Nimis Consulting Information Technologies" width="300"/>
</p>

<p align="center">
  <b>Version 2.0 (FlatLaf Gold)</b> | Sviluppatore: <i>Alessandro Caliciotti</i> | <b>Nimis Consulting Information Technologies</b>
</p>

---

## 🌐 Language / Lingua

- 🇮🇹 [Italiano](#-italiano)
- 🇬🇧 [English](#-english)

---

## 🇮🇹 Italiano

### 📌 Panoramica del Software
Il **WebLogic Migration Tool** è una soluzione software enterprise progettata per automatizzare l'estrazione, la migrazione e la replicazione della topologia e delle applicazioni fra ambienti **Oracle WebLogic Server (11g/12c)**.

Il tool gestisce l'intero ciclo di vita della migrazione: dall'estrazione remota via SSH con decifrazione automatica delle password dei DataSources JDBC, alla ri-mappatura grafica di nomi, porte e credenziali, fino all'installazione remota dei pacchetti applicativi (`.war`, `.ear`, `.jar`).

#### ✨ Caratteristiche Principali:
1. **Estrazione Completa MBean (SSH & Offline)**:
   - Estrae il 100% degli attributi di Server (argomenti JVM, ClassPath, JavaHome, SSLPort, AutoRestart) e Applicazioni (target, staging mode, deployment order).
   - **Decifrazione Password JDBC**: Decifra automaticamente le password offuscate `XMLEncryptionSecret` direttamente dai file `config.xml` sorgente.
2. **Harvesting Applicativo Automatico**:
   - Scarica automaticamente i pacchetti fisici (`.war`, `.ear`) dai percorsi sorgente (`getSourcePath()`) nella cartella `apps/`.
3. **Pannello di Rinomina & Mappatura Dinamica (A -> B)**:
   - Tabella interattiva per rinominare Cluster e Server, cambiare porte di ascolto e sostituire le password del database.
4. **Deploy Remoto Automatico su WebLogic 12c**:
   - Carica i file `.war` nella cartella `/tmp/apps/` del server target ed esegui gli script WLST di attivazione senza intervento manuale.
5. **Architettura 100% Portabile e Standalone**:
   - Include un runtime OpenJDK 17 integrato (`run.cmd` / `run.sh`). Non richiede Java preinstallato sul sistema.

---

### 🖥️ Guida all'Interfaccia Grafica ed Utilizzo

#### 1. Scheda 1: Estrazione Sorgente via SSH (Da A)
Permette di inserire le credenziali SSH e WebLogic del server sorgente (11g) ed avviare l'estrazione automatica del dominio. In alternativa, permette di generare un pacchetto di estrazione offline (`dump_tool_xxx/`) per server isolati.

![Estrazione Sorgente SSH](docs/images/tab1_extraction.png)

- **Form Sinistro**: Inserimento IP sorgente, porta SSH, credenziali di sistema `root` e credenziali WebLogic.
- **Pulsante "ESTRAI CONFIGURAZIONE DOMINIO (SSH)"**: Avvia lo script WLST remoto in background con **Loading Overlay stile Apple in tema Gold Leaf**.
- **Albero del Dominio (Destra)**: Visualizza la topologia estratta (Cluster, Managed Server, Porte SSL, DataSources JDBC).
- **Console Log (Basso)**: Mostra in tempo reale lo scaricamento delle applicazioni nella cartella `apps/`.

---

#### 2. Scheda 2: Rinomina & Mappature (A -> B)
Consente di modificare ed adattare la configurazione sorgente prima del deploy nel nuovo ambiente.

![Rinomina e Mappature](docs/images/tab2_mapping.png)

- **Modifica dei Nomi**: Cambia il nome dei Cluster e dei Managed Server target.
- **Porte e Credenziali DB**: Sostituisci la porta di ascolto dei server gestiti ed aggiorna la password reale del database per i DataSources JDBC.
- **Riassegnazione Target**: Associa ogni applicazione o server al Cluster di destinazione desiderato.
- **Pulsante "CONFERMA MAPPATURE E RINOMINE"**: Applica le modifiche al modello in memoria.

---

#### 3. Scheda 3: Generatore Task & Deploy Remoto (Verso B)
Genera il pacchetto di deploy numerato (`task_xxx/`) oppure esegue direttamente l'installazione remota via SSH su WebLogic 12c.

![Generazione ed Esecuzione Task](docs/images/tab3_execution.png)

- **Pulsante "GENERA PACCHETTO TASK NUMERATO"**: Crea una cartella standalone pronta per l'esecuzione su macchine offline.
- **Pulsante "ESECUZIONE SSH REMOTA SU WEBLOGIC 12C"**:
  1. Carica automaticamente gli applicativi `.war` / `.ear` in `/tmp/apps/` sul target.
  2. Esegue lo script WLST `deploy_topology.py` per creare Cluster, Server e DataSources.
  3. Esegue `deploy_apps.py` per installare ed attivare le applicazioni sul target.

---

### 🚀 Istruzioni per l'Installazione ed Avvio

1. **Clonare il Repository**:
   ```bash
   git clone https://github.com/RedScorpio83/weblogic-migration-tool-dist.git
   cd weblogic-migration-tool-dist
   ```
2. **Avvio su Windows**:
   Fare doppio click sul file `run.cmd` (oppure eseguire da terminale: `run.cmd`).
3. **Avvio su Linux**:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

*Nota: Al primo avvio, i file binari della JDK integrata (`jdk_part1.bin` + `jdk_part2.bin`) verranno decompressi ed attivati automaticamente.*

---

<br/>

## 🇬🇧 English

### 📌 Software Overview
The **WebLogic Migration Tool** is an enterprise software solution designed to automate topology extraction, configuration renaming, and application migration between **Oracle WebLogic Server (11g/12c)** environments.

The tool handles the entire migration lifecycle: from remote SSH extraction with automatic decryption of JDBC DataSource passwords, to graphical renaming/mapping of ports and credentials, up to physical deployment of application archives (`.war`, `.ear`, `.jar`).

#### ✨ Key Features:
1. **Exhaustive MBean Extraction (SSH & Offline)**:
   - Extracts 100% of MBean attributes for Servers (JVM startup args, ClassPath, JavaHome, SSLPort, AutoRestart) and Applications (targets, staging modes, deployment orders).
   - **JDBC Password Decryption**: Automatically decrypts obfuscated `XMLEncryptionSecret` passwords directly from source `config.xml` files.
2. **Automatic Application File Harvesting**:
   - Automatically downloads physical `.war` / `.ear` binaries from WebLogic source paths (`getSourcePath()`) into `apps/`.
3. **Dynamic Renaming & Mapping Panel (A -> B)**:
   - Interactive data table to rename Clusters and Servers, change listen ports, and update database passwords.
4. **Automatic Remote Deploy to WebLogic 12c**:
   - Uploads `.war` archives into `/tmp/apps/` on target servers and runs automated WLST deployment scripts.
5. **100% Portable Standalone Architecture**:
   - Bundles a portable OpenJDK 17 runtime (`run.cmd` / `run.sh`). No system Java installation required.

---

### 🖥️ User Interface & Workflow Guide

#### 1. Tab 1: Source Extraction via SSH (From A)
Allows entering SSH and WebLogic credentials for the source 11g server and starting automated domain extraction. Alternatively, generates an offline extraction package (`dump_tool_xxx/`) for isolated environments.

![Source SSH Extraction](docs/images/tab1_extraction.png)

- **Left Form**: Input source IP, SSH port, `root` credentials, and WebLogic admin credentials.
- **"ESTRAI CONFIGURAZIONE DOMINIO (SSH)" Button**: Triggers remote WLST extraction in the background featuring an **Apple-style Gold Leaf loading overlay**.
- **Domain Tree (Right)**: Displays the extracted topology hierarchy (Clusters, Managed Servers, SSL Ports, JDBC DataSources).
- **Console Log (Bottom)**: Real-time progress output showing application file downloads into `apps/`.

---

#### 2. Tab 2: Renaming & Mapping (A -> B)
Allows customizing and adapting the source configuration before deploying to the target environment.

![Renaming and Mapping](docs/images/tab2_mapping.png)

- **Name Editing**: Modify Cluster and Managed Server target names.
- **Ports & DB Credentials**: Reassign listen ports and update real database passwords for JDBC DataSources.
- **Target Remapping**: Map applications and servers to their designated target Cluster.
- **"CONFERMA MAPPATURE E RINOMINE" Button**: Applies changes to the in-memory migration model.

---

#### 3. Tab 3: Task Generator & Remote Execution (To B)
Generates a standalone migration package (`task_xxx/`) or executes direct remote SSH deployment to target WebLogic 12c.

![Task Generation and Execution](docs/images/tab3_execution.png)

- **"GENERA PACCHETTO TASK NUMERATO" Button**: Exports a self-contained package for air-gapped target servers.
- **"ESECUZIONE SSH REMOTA SU WEBLOGIC 12C" Button**:
  1. Uploads `.war` / `.ear` application packages to `/tmp/apps/` on target server.
  2. Runs `deploy_topology.py` WLST script to create Clusters, Servers, and DataSources.
  3. Runs `deploy_apps.py` WLST script to install and activate applications.

---

### 🚀 Installation & Quick Start

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RedScorpio83/weblogic-migration-tool-dist.git
   cd weblogic-migration-tool-dist
   ```
2. **Launch on Windows**:
   Double click `run.cmd` (or execute `run.cmd` in Command Prompt).
3. **Launch on Linux**:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

*Note: On first launch, the bundled OpenJDK 17 volume files (`jdk_part1.bin` + `jdk_part2.bin`) will be uncompressed and initialized automatically.*
