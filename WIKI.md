# WebLogic Configuration & Application Migration Tool - Technical Wiki

<p align="center">
  <img src="logo.png" alt="Nimis Consulting Information Technologies" width="320"/>
</p>

<p align="center">
  <b>Versione Documentata: 3.8.0 (FlatLaf Gold)</b> | Autore: <i>Alessandro Caliciotti</i>
</p>

---

## 📚 Documentazione Correlata & Link
- 📖 **[Guida Utente Operativa (GUIDA_UTENTE.md)](GUIDA_UTENTE.md)** - Guida passo-passo per gli operatori.
- 🏠 **[README Principale del Progetto (README.md)](README.md)** - Presentazione generale del repository.

---

## 📐 Architettura di Sistema e Modello MBean (v3.8.0)

### 1. Flusso di Migrazione End-to-End

```
+--------------------------+        SSH / Offline Dump         +---------------------------+
| WebLogic 11g (Sorgente)  | --------------------------------> | WebLogic Migration Tool   |
| IP: 192.168.10.240       |                                   | (GUI FlatLaf Gold v3.8.0) |
+--------------------------+                                   +---------------------------+
                                                                             |
                                                                             | Deploy Remoto / Task (task_xxx)
                                                                             v
                                                               +---------------------------+
                                                               | WebLogic 12c (Target)     |
                                                               | IP: 192.168.10.197       |
                                                               +---------------------------+
```

### 2. Struttura della Cartella `works/`
Dalla versione 3.7.0+, l'applicazione gestisce i dati di lavoro in cartelle isolate numerate sotto `works/`:
```
works/
└── 001_NomeLavoro/
    ├── dump/          -> Dump JSON estratti dal sorgente A e pacchetti applicativi (.war, .ear)
    ├── deploy/        -> Task di migrazione generati (task_001/ con deploy_topology.py, deploy_apps.py)
    ├── target_dumps/  -> Ispezione in tempo reale del Dominio Target B
    └── prj_saves/     -> File salvati di progetto mappatura (.wlsmap) e schermate architetturali PNG
```

---

## 🛠️ Moduli Interni del Tool

### 1. `WebLogicModel.java` & `WebLogicConnector.java`
- Rappresentazione in-memory della topologia (`DomainConfig`, `MachineConfig`, `ClusterConfig`, `ServerConfig`, `DataSourceConfig`, `AppConfig`).
- Decifrazione automatica delle password dei DataSources JDBC cifrate con `XMLEncryptionSecret`.

### 2. `TaskExporter.java` & Generazione Script WLST
- **Gestione Multi-Target**: Risoluzione dinamica dei target multipli separati da virgola (`target.split(',')`) per DataSources ed Applicazioni.
- **Partizionamento Anti-64KB**: Suddivisione degli script Python generati in lotti da 15 elementi per prevenire il limite di bytecode JVM su domini complessi.
- **Supporto Nativo Shared Libraries**: Rilevamento delle Librerie Condivise (`libraryModule='true'`).

### 3. `MigrationTool.java` (Interfaccia Grafica Swing FlatLaf)
- **Avvio Massimizzato**: Window state impostato su `JFrame.MAXIMIZED_BOTH`.
- **Gestione Intelligente Machine**: Eliminazione con popup modale di reassegnazione risorse, Consolidamento globale con caselle per-machine, Aggiungi Machine con checkbox di associazione.
- **Validazione Mappature Multi-Target & Modal Interattivo**: Modal `🔧 Correzione Mappature Non Valide` con tabella delle righe errate ed Ispettore Proprietà per correzione guidata.
- **Viste Architetturali Grafiche**: Diagramma 2D Draw.io, Vista Architetturale a Blocchi (con Zoom +, Zoom -, 100% ed esportazione schermata HD in formato PNG) ed Albero di Gerarchia Target.

---

*Nimis Consulting Information Technologies - Alessandro Caliciotti*
