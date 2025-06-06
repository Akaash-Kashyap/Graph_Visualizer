# Graph_Visualizer

- [Graph\_Visualizer](#graph_visualizer)
  - [Requirements](#requirements)
  - [Unweighted graphs](#unweighted-graphs)
    - [BFS](#bfs)
    - [DFS](#dfs)
  - [Weighted Graphs](#weighted-graphs)
    - [Dijkstra's algorithm](#dijkstras-algorithm)
    - [Bellman-Ford](#bellman-ford)
    - [Floyd-Warshall](#floyd-warshall)
  - [Upcoming Features](#upcoming-features)


Visualizes various algorithms on a given input graph and animates them to show node traversal and edge traversal paths.


## Requirements

Must have Tkinter installed. You can install Tk via pip or your system
package manager:

```bash
pip install tk  # or install the python3-tk package for your OS
```

## Unweighted graphs

### BFS

Breadth-First Search (BFS) is a graph traversal algorithm used to explore nodes and edges in a graph systematically. Starting from a given node (known as the source node), BFS explores all neighboring nodes at the current depth level before moving on to nodes at the next depth level. This "level-by-level" approach makes BFS especially suitable for finding the shortest path in an unweighted graph, as it guarantees reaching the nearest nodes first.

### DFS

Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. Starting from a specified node (called the source node), DFS dives deep into a graph, following one path until it reaches a dead end or an already visited node, then backtracks to explore other paths. This "depth-first" approach allows DFS to explore all nodes in a connected component or in a graph.

## Weighted Graphs

Algorithms on weighted graphs determine the lowest-cost paths between
nodes. The visualizer currently supports Dijkstra's algorithm.

### Dijkstra's algorithm

This algorithm is implemented and animated in the application.
It finds the shortest path from a source node to all other nodes in a
graph with non-negative edge weights.

### Bellman-Ford

(not yet implemented)\
(add description)

### Floyd-Warshall

(not yet implemented)\
(add description)

## Upcoming Features

- [x]  Easier graph input method
- [x]  Nicer UI for selecting algorithm
- [x] Weighted graph support
  - [ ] including the weighted graph algorithms
- [ ] Directed graph support
- [ ] Example graphs
