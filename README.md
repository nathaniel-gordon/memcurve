# MemCurve — Temporal Memory for AI Assistants with Ebbinghaus Decay & MCP Server

MemCurve implements human-like temporal memory for LLM agents using the **Ebbinghaus Forgetting Curve**. Instead of treating all memories as permanent or relying on fixed vector search windows, MemCurve models memory retention as a function of elapsed time and reinforcement frequency:

$$R(t) = e^{-rac{t}{S}}$$

Where $R$ is memory retention probability, $t$ is elapsed time, and $S$ is memory stability (increased upon each memory reinforcement).

## Key Features

- **Dynamic Decay & Reinforcement**: Memories naturally fade unless accessed or reinforced in subsequent conversations.
- **Model Context Protocol (MCP) Server**: Exposes standard MCP tools (`record_memory`, `retrieve_active_memories`, `reinforce_memory`) for native integration into Claude Desktop, Cursor, and custom agent runtimes.
- **Memory Consolidation**: Periodic background consolidation merges related transient memories into high-stability semantic knowledge.

## Running the MCP Server

```bash
# Start the MemCurve Model Context Protocol server over stdio
python -m memcurve --mcp
```

## Tests

```bash
pytest tests/ -v
```
