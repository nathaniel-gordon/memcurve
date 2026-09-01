<div align="center">

# 🧠 MemCurve

**Persistent memory for AI assistants — with forgetting curves, decay, and graph clustering.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![MCP](https://img.shields.io/badge/Protocol-MCP%20Server-6366f1?style=for-the-badge)](https://modelcontextprotocol.io)
[![Domain](https://img.shields.io/badge/Domain-Agent%20Memory-f97316?style=for-the-badge)](https://github.com/nathaniel-gordon/memcurve)

<br/>

*CortexGraph MCP server. Stores memories as a weighted knowledge graph, decays stale nodes via configurable half-life, clusters related memories, and surfaces the right context at the right time through activation-pattern retrieval.*

</div>

---

## 🧠 What Is This?

> **For non-technical readers:** Most AI assistants have no persistent memory — every conversation starts completely blank. MemCurve gives an AI assistant long-term memory that works like human memory: important things are remembered more strongly, rarely-accessed memories fade over time, and related memories are grouped together so that recalling one makes nearby ones more accessible. It exposes this memory system to AI tools via a standard protocol (MCP), so any compatible assistant can use it.

---

## 🏗️ CortexGraph Architecture

MemCurve implements the **CortexGraph** memory system — a weighted knowledge graph where nodes are memory entities, edges encode semantic relationships, and node weights decay over time according to configurable half-life schedules. Retrieval uses activation spreading: querying one node activates its neighbors with diminishing strength, surfacing contextually related memories.

```
💬 Conversation / Tool Call
         │
         ▼
🔍 Entity Extraction & Message Analysis
   Detects entities, topics, facts, and relationships
   worth persisting in the memory graph
         │
         ▼
🧠 CortexGraph (Weighted Knowledge Graph)
   ├── Nodes: memories, facts, entities
   ├── Edges: semantic relations + co-occurrence weights
   └── Node weights: decay via half-life schedule
         │
         ├── ⏱️  Background Decay Process
         │       Stale memory weights decay exponentially
         │       GC prunes nodes below activation threshold
         │
         └── 🔗 Memory Clustering
                 Related nodes grouped into clusters
                 for efficient neighborhood retrieval
         │
         ▼
🔎 Activation-Pattern Retrieval
   Query activates seed nodes, spreads to neighbors
   Returns ranked memory context for generation
```

---

## 🔬 Technical Design

**Half-Life Decay** — Memory node weights decay exponentially over time: `w(t) = w₀ × (½)^(t/τ)` where `τ` is the configurable half-life. Frequently accessed memories are "touched" (weight refreshed) on each recall, preventing useful information from decaying. The decay function is calculated by `cortexgraph.core.decay.calculate_halflife` and runs on a background scheduler.

**MCP Tool Surface** — CortexGraph exposes memory operations as MCP tools that any compatible AI client can call:

| Tool | Purpose |
|---|---|
| `save` | Persist a new memory entity to the graph |
| `search` | Semantic search over memory nodes |
| `search_unified` | Combined graph traversal + semantic search |
| `auto_recall_tool` | Context-aware memory retrieval based on current conversation |
| `analyze_message` | Extract entities and facts worth saving from a message |
| `cluster` | Group related memories into topic clusters |
| `consolidate` | Merge redundant or contradictory memory nodes |
| `gc` | Prune decayed nodes below activation threshold |
| `promote` | Boost a memory node's weight (mark as important) |
| `touch` | Refresh a node's decay timer without modifying weight |

**Activation Spreading** — On `search_unified`, queried seed nodes activate their graph neighbors with weight proportional to edge strength × query relevance. This surfaces associated memories without requiring exact semantic match — related context emerges from graph structure.

**Security Layer** — The server includes secret scanning on config files (`should_warn_about_secrets`) and enforces secure storage paths (`ensure_secure_storage`) before starting — preventing accidental exposure of API keys in the memory store.

---

## 🚀 Getting Started

```bash
git clone https://github.com/nathaniel-gordon/memcurve
cd memcurve
pip install -e .
```

### Start the MCP Server

```bash
python -m cortexgraph
```

### Visualize the Memory Graph

```bash
python scripts/visualize_graph.py
```

### Convert to MCP Memory Format

```bash
python scripts/convert_to_memory_mcp.py
```

---

## 📁 Project Structure

```
memcurve/
├── src/cortexgraph/
│   ├── server.py           # MCP server entrypoint & tool registration
│   ├── context.py          # Shared db & mcp context
│   ├── config.py           # Half-life and decay configuration
│   ├── background.py       # Background decay scheduler
│   ├── performance.py      # Performance monitoring
│   ├── activation/         # Activation spreading & entity extraction
│   │   ├── detectors.py
│   │   ├── entity_extraction.py
│   │   └── patterns.py
│   ├── tools/              # All MCP tool implementations
│   └── security/           # Secret scanning & secure storage enforcement
└── scripts/
```

---

<div align="center">

*Built by [Nathaniel Gordon](https://github.com/nathaniel-gordon)*

</div>
