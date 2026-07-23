# WebLogic Configuration & Application Migration Tool

<p align="center">
  <img src="logo.png" alt="Nimis Consulting Information Technologies" width="300"/>
</p>

<p align="center">
  <b>Version 3.9.0 (FlatLaf Gold)</b> | Sviluppatore: <i>Alessandro Caliciotti</i> | <b>Nimis Consulting Information Technologies</b>
</p>

---

## 📖 Documentazione Rapida & Link Utili

- 📖 **[Guida Utente Operativa Passo-Passo](GUIDA_UTENTE.md)** - Manuale utente completo per l'utilizzo dell'applicazione, gestione dei lavori, mappature ed eliminazione intelligente Cluster/Machine.
- 📚 **[Wiki del Progetto & Architettura Tecnica](WIKI.md)** - Documentazione approfondita sull'architettura interna, MBean WebLogic, Jython AST e partizionamento anti-64KB.

---

## 🇮🇹 Italiano

### 📌 Panoramica del Software
Il **WebLogic Migration Tool** è una soluzione software enterprise progettata per automatizzare l'estrazione, la migrazione e la replicazione della topologia e delle applicazioni fra ambienti **Oracle WebLogic Server (11g/12c)**.

#### ✨ Caratteristiche Principali (v3.9.0):
1. 🧠 **Eliminazione Intelligente Cluster & Smart Multi-Target Cleanup**:
   - Quando si elimina un **Cluster**, l'applicazione rileva tutte le risorse collegate (Server, DataSources, Applicazioni/Librerie) e permette di:
     - 🧹 **Rimuovere puntualmente il Cluster dai target** (preservando tutti gli altri target nelle liste con virgola `clusterA,clusterB` -> `clusterB`).
     - 🔀 **Riassegnare le risorse** ad un altro Cluster target.
     - 🗑️ **Eliminare le risorse collegate**.
2. 💻 **Avvio sempre a Schermo Intero**: Avvio massimizzato (`MAXIMIZED_BOTH`).
3. 🧠 **Gestione Intelligente Machine**: Eliminazione con popup di reassegnazione risorse, Consolidamento per-machine ed Aggiungi Machine.
4. 🔀 **Validazione Mappature Multi-Target & Modal Interattivo**: Modal **`🔧 Correzione Mappature Non Valide`** con Ispettore Proprietà ed aggiornamento 1-click.
5. 🔍 **Zoom & Esportazione Schermata PNG**: Zoom In (+), Zoom Out (-), 100% ed **Esportazione Schermata HD PNG** della vista architetturale.
