import networkx as nx
from graph_algos import BFS, DFS
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk



current_anim = None
animation_running = False

def init_graph(root,edges=[(0,3),(0,2),(1,3), (1,2), (2,5), (2,6), (2,4), (5,7), (6,7), (4,7)]):
    global G, pos, node_colors, edge_colors, fig, ax, canvas
    G = nx.Graph()
    # edges = [(0,3),(0,2),(1,3), (1,2), (2,5), (2,6), (2,4), (5,7), (6,7), (4,7)]
    G.add_edges_from(edges)
    # G = nx.balanced_tree(r=2, h=5)
    # color scheme
    node_colors = {node: "lightgrey" for node in G.nodes}
    edge_colors = {edge: "gray" for edge in G.edges}

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    pos = nx.spring_layout(G, k=2, scale=2.5, iterations=1000)


    def initialize_plot():
        # needs ax, canvas, G, pos, node and edge colors
        ax.clear()
        ax.set_title("Select an Algorithm to Run", fontsize=16)
        nx.draw(G, pos, ax=ax, with_labels= True,
                    node_color=[node_colors[n] for n in G.nodes],
                    edge_color=[edge_colors.get(e, "gray") for e in G.edges],
                    node_size=700, font_size=10, font_weight="bold",
                    arrowstyle="-|>", arrowsize=15)
        canvas.draw()

    initialize_plot()

# Button commands
def start_bfs():
    # pass
    name = "BFS"
    nodes, edges = BFS(G, s=0)
    run_animation(nodes, edges, name)


def start_dfs():
    # pass
    name = "DFS"
    nodes, edges = DFS(G, s=0)
    run_animation(nodes, edges, name)




def run_animation(v_nodes, v_edges, algorithm_name):
    global current_anim, animation_running
    # Stop any existing animation
    # print(animation_running)
    if animation_running:
        return
    animation_running = True

    node_colors.update({node: "lightgrey" for node in G.nodes()})
    edge_colors.update({edge: "gray" for edge in G.edges()})
    
    def step(frame):
        # update the node and edge colors for the current frame
        current_node = v_nodes[frame]
        node_colors[current_node] = "orange" # Visited node

        if frame > 0:
            current_edge = v_edges[frame - 1]
            edge_colors[current_edge] = "blue"

        
        # clear the plot and redraw the graph with the new frame
        ax.clear()
        nx.draw(G, pos, ax=ax, with_labels= True,
                node_color=[node_colors[n] for n in G.nodes],
                edge_color=[edge_colors.get(e, "gray") for e in G.edges],
                node_size=700, font_size=10, font_weight="bold",
                arrowstyle="-|>", arrowsize=15)
        ax.set_title(algorithm_name + f" - Visiting Node {current_node}")
        if frame == len(v_nodes) - 1:
            on_animation_complete()
    
    def on_animation_complete():
        global animation_running
        animation_running = False
    
    current_anim = animation.FuncAnimation(fig, step, frames=len(v_nodes), repeat=False, interval=500)
    canvas.draw()