# Maze & Puzzle Search Suite

A pure‐Python implementation of classical graph‐search algorithms applied to two domains:
1. **Grid‐world mazes** (Pacman‐style navigation)  
2. **Eight‐tile sliding puzzle**

---

## Features

- **Core Search Algorithms**  
  - Depth-First Search (DFS)  
  - Breadth-First Search (BFS)  
  - Uniform-Cost Search (UCS)  
  - A\* Search with pluggable heuristics  

- **Demo Domains**  
  - **Maze Navigator**  
    - Move a “Pacman” agent through custom layouts  
    - Support for cost‐weighted and corner‐visiting problems  
  - **Eight-Puzzle Solver**  
    - Random instance generator  
    - Breadth‐first solution finder with step‐by‐step playback  

- **Utilities**  
  - Generic `Stack`, `Queue`, `PriorityQueue`  
  - CLI wrappers for quick experimentation  
  - Configurable problem & heuristic interfaces  

---

## Tech Stack

- **Language:** Python 3.7+  
- **Dependencies:** None (standard library only)  
- **Testing:** `unittest` suites under `tests/`

---
