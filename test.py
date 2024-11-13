

# #! REFACTORED

# import tkinter as tk
# import networkx as nx
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from graph_algos import *

# # Initialize Tkinter window
# root = tk.Tk()
# root.title("Graph Algorithm Animation in Tkinter")

# # Create the NetworkX graph
# G = nx.Graph()
# edges = [(0,3),(0,2),(1,3), (1,2), (2,5), (2,6), (2,4), (5,7), (6,7), (4,7)]
# G.add_edges_from(edges)
# # color scheme
# node_colors = {node: "lightgrey" for node in G.nodes}
# edge_colors = {edge: "gray" for edge in G.edges}

# pos = nx.spring_layout(G)

# current_anim = None
# animation_running = False

# # Set up the figure and axis for Matplotlib
# fig, ax = plt.subplots()


# # Algorithm steps
# # def bfs_order():
# #     return list(nx.bfs_tree(G, source=0))

# # def dfs_order():
# #     return list(nx.dfs_tree(G, source=0))

# # Animation function
# def run_animation(v_nodes, v_edges, algorithm_name):
#     global current_anim, animation_running
#     # Stop any existing animation
#     if animation_running:
#         return
#     animation_running = True

#     node_colors.update({node: "lightgrey" for node in G.nodes()})
#     edge_colors.update({edge: "gray" for edge in G.edges()})
    
#     def step(frame):
#         # no longer need this code below
#         # ax.cla()  # Clear the axis but retain layout
#         # node = v_nodes[i]
#         # colors[node] = "red"
#         # nx.draw(G, pos, ax=ax, node_color=[colors[n] for n in G.nodes()], with_labels=True)
        
#         #########
#         # stop if all frames are used
#         # if frame >= len(v_nodes):
#         #     anim.event_source.stop()
#         #     return
        
#         # update the node and edge colors for the current frame
#         current_node = v_nodes[frame]
#         node_colors[current_node] = "orange" # Visited node

#         if frame > 0:
#             current_edge = v_edges[frame - 1]
#             edge_colors[current_edge] = "blue"

        
#         # clear the plot and redraw the graph with the new frame
#         ax.clear()
#         nx.draw(G, pos, ax=ax, with_labels= True,
#                 node_color=[node_colors[n] for n in G.nodes],
#                 edge_color=[edge_colors.get(e, "gray") for e in G.edges],
#                 node_size=700, font_size=10, font_weight="bold",
#                 arrowstyle="-|>", arrowsize=15)
#         ax.set_title(algorithm_name + f" - Visiting Node {current_node}")
#         if frame == len(v_nodes) - 1:
#             on_animation_complete()
    
#     def on_animation_complete(*args):
#         global animation_running
#         animation_running = False
    
#     current_anim = animation.FuncAnimation(fig, step, frames=len(v_nodes), repeat=False, interval=500)
#     canvas.draw()

# def initialize_plot():
#     ax.clear()
#     ax.set_title("Select an Algorithm to Run", fontsize=16)
#     nx.draw(G, pos, ax=ax, with_labels= True,
#                 node_color=[node_colors[n] for n in G.nodes],
#                 edge_color=[edge_colors.get(e, "gray") for e in G.edges],
#                 node_size=700, font_size=10, font_weight="bold",
#                 arrowstyle="-|>", arrowsize=15)
#     canvas.draw()

# # Button commands
# def start_bfs():
#     name = "BFS"
#     nodes, edges = BFS(G, s=0)
#     run_animation(nodes, edges, name)


# def start_dfs():
#     name = "DFS"
#     nodes, edges = DFS(G, s=0)
#     run_animation(nodes, edges, name)

# # Set up the Matplotlib canvas to display in Tkinter
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# # Frame for buttons
# button_frame = tk.Frame(root)
# button_frame.pack(side=tk.RIGHT, fill=tk.Y)

# # Add buttons to the frame
# bfs_button = tk.Button(button_frame, text="Run BFS", command=start_bfs)
# bfs_button.pack(pady=10)

# dfs_button = tk.Button(button_frame, text="Run DFS", command=start_dfs)
# dfs_button.pack(pady=10)

# # init the main screen
# initialize_plot()
# # Start Tkinter event loop
# root.mainloop()
