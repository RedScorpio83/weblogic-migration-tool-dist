# WebLogic Configuration & Application Migration Tool - Technical Wiki

<p align="center">
  <b>Versione Documentata: 4.0.0 (FlatLaf Gold Enterprise)</b> | Autore: <i>Alessandro Caliciotti</i>
</p>

---

## 📚 Documentazione Correlata & Link
- 📖 **[Guida Utente Operativa (GUIDA_UTENTE.md)](GUIDA_UTENTE.md)** - Guida passo-passo per gli operatori.
- 🏠 **[README Principale del Progetto (README.md)](README.md)** - Presentazione generale del repository.

---

## 📐 Architettura di Sistema e Modello MBean (v4.0.0)

### 1. Flusso di Provisioning Bare-Metal & Migrazione End-to-End

```
+------------------------------------------------------------------------------------------------+
| PHASE 0: PROVISIONING INFRASTRUTTURA BARE-METAL WEBLOGIC 12C (ProvisioningExporter)            |
| - Setup OS Mode (ROOT vs ORACLE) & Alberatura OFA (/u01/app/oracle/...)                        |
| - Silent Install JDK & WLS 12c (silent_install.rsp + oraInst.loc)                              |
| - WLST Offline Domain Creation (createDomain) & boot.properties Setup                          |
| - Domain Packing: pack.sh -domain=... -template=domain_managed.jar -managed=true              |
| - AdminServer Start & Secondary Nodes Unpacking (unpack.sh) + NodeManager Start (Port 5556)    |
+------------------------------------------------------------------------------------------------+
                                              |
                                              v
+--------------------------+        SSH / Offline Dump         +---------------------------+
| WebLogic 11g (Sorgente)  | --------------------------------> | WebLogic Migration Tool   |
| IP: 192.168.1.10         |                                   | (GUI FlatLaf Gold v4.0.0) |
+--------------------------+                                   +---------------------------+
                                                                             |
                                                                             | Deploy Remoto / Task (task_xxx)
                                                                             v
                                                               +---------------------------+
                                                               | WebLogic 12c (Target)     |
                                                               | IP: 192.168.1.20          |
                                                               +---------------------------+
```

### 2. Struttura della Cartella `works/`
Dalla versione 3.7.0+, l'applicazione gestisce i dati di lavoro in cartelle isolate numerate sotto `works/`:
```
works/
└── 001_NomeLavoro/
    ├── dump/          -> Dump JSON estratti dal sorgente A e pacchetti applicativi (.war, .ear)
    ├── deploy/        -> Task di migrazione (task_001/) e task di infrastruttura (infra_task_001/)
    ├── target_dumps/  -> Ispezione in tempo reale del Dominio Target B
    └── prj_saves/     -> File salvati di progetto mappatura (.wlsmap) e schermate architetturali PNG
```

---

## 🛠️ Moduli Interni del Tool

### 1. `ProvisioningExporter.java` & Workflow `pack/unpack`
- Generatore autonomo degli script di installazione infrastruttura:
  - `00_setup_system.sh`: Creazione directory, utente `oracle`, gruppo `oinstall` e remount `/tmp`.
  - `silent_install.rsp` & `oraInst.loc`: Risposte per l'installazione silent di WebLogic Server 12c.
  - `01_create_domain_offline.py`: Script WLST offline per la creazione del dominio base.
  - `boot.properties`: Configurazione delle credenziali cifrate dell'AdminServer.
  - `pack.sh`: Impacchettamento del dominio in `domain_managed.jar` eseguito **ad AdminServer spento**.
  - `03_setup_secondary_node.sh`: Trasferimento ed esecuzione di `unpack.sh` sui nodi secondari Machine e configurazione/avvio del NodeManager.
  - `02_create_nodes_online.py`: Registrazione WLST Online delle Machine e dei NodeManager nel dominio.

### 2. `WebLogicModel.java` & `WebLogicConnector.java`
- Rappresentazione in-memory della topologia (`DomainConfig`, `MachineConfig`, `ClusterConfig`, `ServerConfig`, `DataSourceConfig`, `AppConfig`).
- Decifrazione automatica delle password dei DataSources JDBC cifrate con `XMLEncryptionSecret`.

### 3. `TaskExporter.java` & Generazione Script WLST
- **Gestione Multi-Target**: Risoluzione dinamica dei target multipli separati da virgola (`target.split(',')`).
- **Partizionamento Anti-64KB**: Suddivisione degli script Python generati in lotti da 15 elementi per prevenire il limite di bytecode JVM su domini complessi.
- **Supporto Nativo Shared Libraries**: Rilevamento delle Librerie Condivise (`libraryModule='true'`).

---

*Alessandro Caliciotti*
