# graph_algos (unweighted)
# BFS
# DFS
from collections import deque
import heapq

# BFS algorithm
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

# graph_algos (weighted)
# Dijkstra
# def dijkstra(G, s):
#     """Performs Dijkstra's algorithm on a graph and returns the order of visited nodes and edges."""
#     visited_nodes = []
#     visited_edges = []
#     distances = {node: float("inf") for node in G.nodes}
#     distances[s] = 0
#     queue = deque([s])

#     while queue:
#         current = queue.popleft()
#         visited_nodes.append(current)
#         for neighbor in G.neighbors(current):
#             if distances[current] + G[current][neighbor]["weight"] < distances[neighbor]:
#                 distances[neighbor] = distances[current] + G[current][neighbor]["weight"]
#                 visited_edges.append((current, neighbor))
#                 queue.append(neighbor)
#     return visited_nodes, visited_edges

def dijkstra(G, s):
    """Performs Dijkstra's algorithm on a graph and returns the order of visited nodes and edges."""
    visited_nodes = []
    visited_edges = []
    visited = set()
    distances = {node: float("inf") for node in G.nodes}
    distances[s] = 0
    priority_queue = [(0, s)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue

        visited.add(current_node)
        visited_nodes.append(current_node)
        
        for neighbor in G.neighbors(current_node):
            # default weight to 1 if not specified on the edge
            edge_weight = G[current_node][neighbor].get("weight", 1)
            new_distance = current_distance + edge_weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
                visited_edges.append((current_node, neighbor))

    return visited_nodes, visited_edges
