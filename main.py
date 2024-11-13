import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
from graph_algos import *
# tkinter libs + matplotlib extension
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# tkinter window setup


# Create a directed graph and add edges
G = nx.Graph()
edges = [(0,3),(0,2),(1,3), (1,2), (2,5), (2,6), (2,4), (5,7), (6,7), (4,7)]
G.add_edges_from(edges)


# ##################
# #### run algo ####
# ##################
# start = 0
# v_nodes, v_edges = DFS(G, start)
# title = "DFS Animation on Graph"
# # print(v_nodes)
# # print(v_edges)

# # set up figure for animation
# fig, ax = plt.subplots(figsize=(8,6))
# pos = nx.spring_layout(G, k=1, seed=42)

# # initialize node colors
# node_colors = {node: "lightgrey" for node in G.nodes}
# edge_colors = {edge: "gray" for edge in G.edges}

# # update function for the animation
# def update(frame):
#     # stop if all frames are used
#     if frame >= len(v_nodes):
#         ani.event_source.stop()
#         return
    
#     # update the node and edge colors for the current frame
#     current_node = v_nodes[frame]
#     node_colors[current_node] = "orange" # Visited node

#     if frame > 0:
#         current_edge = v_edges[frame - 1]
#         edge_colors[current_edge] = "blue"

    
#     # clear the plot and redraw the graph with the new frame
#     ax.clear()
#     nx.draw(G, pos, with_labels= True,
#             node_color=[node_colors[n] for n in G.nodes],
#             edge_color=[edge_colors.get(e, "gray") for e in G.edges],
#             node_size=700, font_size=10, font_weight="bold",
#             arrowstyle="-|>", arrowsize=15)
#     ax.set_title(title + f" - Visiting Node {current_node}")


# # Create animation
# ani = animation.FuncAnimation(fig, update, frames=len(G.nodes), repeat=False, interval=1000)

# # Display the animation
# plt.show()

def plot_algo(func, G, start):

    v_nodes, v_edges = func(G, start)
    title = "Need to be set!!"

    # set up figure for animation
    fig, ax = plt.subplots(figsize=(8,6))
    # spacing
    pos = nx.spring_layout(G, k=1, seed=42)

    # initialize node colors
    node_colors = {node: "lightgrey" for node in G.nodes}
    edge_colors = {edge: "gray" for edge in G.edges}

    # update function for the animation
    def update(frame):
        # stop if all frames are used
        if frame >= len(v_nodes):
            ani.event_source.stop()
            return
        
        # update the node and edge colors for the current frame
        current_node = v_nodes[frame]
        node_colors[current_node] = "orange" # Visited node

        if frame > 0:
            current_edge = v_edges[frame - 1]
            edge_colors[current_edge] = "blue"

        
        # clear the plot and redraw the graph with the new frame
        ax.clear()
        nx.draw(G, pos, with_labels= True,
                node_color=[node_colors[n] for n in G.nodes],
                edge_color=[edge_colors.get(e, "gray") for e in G.edges],
                node_size=700, font_size=10, font_weight="bold",
                arrowstyle="-|>", arrowsize=15)
        ax.set_title(title + f" - Visiting Node {current_node}")


    # Create animation
    ani = animation.FuncAnimation(fig, update, frames=len(G.nodes), repeat=False, interval=1000)

    # Display the animation
    plt.show()

plot_algo(DFS, G, start=0)