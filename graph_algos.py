# graph_algos (unweighted)
# BFS
# DFS
from collections import deque

# BFS aglorithm
def BFS(G, s):
    """Performs BFS on a graph and returns the order of visited nodes and edges."""
    visited_nodes = []
    visited_edges = []
    queue = deque([s])
    visited = {s}

    while queue:
        current = queue.popleft()
        visited_nodes.append(current)
        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                visited_edges.append((current, neighbor))
    return visited_nodes, visited_edges

def DFS(G, s):
    """Performs DFS on a graph and returns the order of visited nodes and edges"""
    visited_nodes = []
    visited_edges = []
    stack = [(s, None)]
    visited = {s}
    while stack:
        current, parent = stack.pop()
        # print(parent)
        visited_nodes.append(current)

        if parent is not None:
            visited_edges.append((parent, current))

        for neighbor in G.neighbors(current):
            if neighbor not in visited:

                visited.add(neighbor)
                stack.append((neighbor, current))
    return visited_nodes, visited_edges