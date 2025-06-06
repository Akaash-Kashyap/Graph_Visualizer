import tkinter as tk
import graph_animation
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph_algos import BFS, DFS, dijkstra
import matplotlib.animation as animation


# Global variables
global root

# Function to initialize the Tkinter window

def init_tkinter():

    root = tk.Tk()
    root.title("Graph Algorithm Animation in Tkinter")
    menubar = tk.Menu(root)

    # Adding graph Menu and commands  
    graph = tk.Menu(menubar, tearoff= 0)
    menubar.add_cascade(label='Graph', menu= graph)
    graph.add_command(label='Edit current graph', command=None)
    graph.add_command(label='New Graph', command=None)
    graph.add_separator()
    graph.add_command(label="Exit", command=root.destroy)
    root.config(menu = menubar)

    # size of window (not implemented)
    # root.geometry("1200x1000") # doesnt show buttons on mac
    # root.attributes('-fullscreen', True)
    # root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

    # Frame for graph
    #TODO Take a look at this (is it needed?)
    graph_animation.init_graph(root)

    ##################
    ### UI buttons ###
    ##################

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.RIGHT, fill=tk.Y)
    
    
    # Add buttons to the frame
    algo_mode_label = tk.Label(button_frame, text='algomode')
    algo_mode_label.pack(padx=15, pady=20)
    bfs_button = tk.Button(button_frame, text="Run BFS", command=graph_animation.start_bfs)
    bfs_button.pack(pady=10, padx=15)


    dfs_button = tk.Button(button_frame, text="Run DFS", command=graph_animation.start_dfs)
    dfs_button.pack(pady=10, padx=15)

    #! do i still need this?
    # init the main screen
    # graph_animation.initialize_plot()

    # start Tkinter event loop
    root.mainloop()

# List to store the tuples
edges = []

# old method of starting program
# init_tkinter()



# New method of starting program
# Creating a setup page

"""The setup_page function initializes the setup 
interface for the graph algorithm visualizer. It 
creates a Tkinter window, sets up the graph structure,
 and defines various helper functions for adding and 
 deleting graph edges, updating the graph visualization,
   and handling user interactions. This function serves as 
   the starting point for configuring the graph before 
   running any algorithms."""
def setup_page():

    # Global variables
    type = None
    G = nx.Graph()
    root = tk.Tk()

    # Lists to store the colors of nodes and edges
    node_colors = {node: "lightgrey" for node in G.nodes}
    edge_colors = {edge: "gray" for edge in G.edges}

    # Animation variables
    current_anim = None
    animation_running = False

    # Function to show the side panel based on the graph type
    def show_side_panel(t):
        # if t == -1, Not implemented 
        # if t == 0, undirected graph, unweighted
        # if t == 1, directed graph, unweighted
        # if t == 2, undirected, weighted
        # if t == 3, directed, weighted
        nonlocal G 

        if t == -1:
            tk.messagebox.showerror("Not implemented, try the other buttons")
            return
        

        # UI for Tuple input (side panel)
        # Entry for adding tuples
        enter_text_help = "Enter a tuple in the form (u, v)" if t == 0 or t == 1 else "Enter a tuple in the form (u, v, w)"
        entry_label = tk.Label(side_panel, text=enter_text_help)
        entry_label.pack(pady=5)
        tuple_start_label = tk.Label(side_panel, text="algorithm starts from 0, make sure you include 0 in the tuples")
        tuple_start_label.pack(pady=5)

        global entry
        entry = tk.Entry(side_panel, width=30)
        entry.pack(pady=5)

        if t == 0 or t == 1:
            add_button = tk.Button(side_panel, text="Add Tuple", command=add_tuple2)
        else:
            add_button = tk.Button(side_panel, text="Add Tuple", command=add_tuple3)
        add_button.pack(pady=5)

        # Listbox to display tuples
        listbox_label = tk.Label(side_panel, text="Tuples List:")
        listbox_label.pack(pady=5)
        global listbox
        listbox = tk.Listbox(side_panel, width=30, height=10)
        listbox.pack(pady=5)


        # Button to delete a tuple
        if t == 0 or t == 1:
            delete_button = tk.Button(side_panel, text="Delete Selected Tuple",width=25, command=delete_tuple2)
        else:
            delete_button = tk.Button(side_panel, text="Delete Selected Tuple",width=25, command=delete_tuple3)    
        delete_button.pack(pady=10)


        
        # show side panel
        side_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        # Hide old panel
        graph_choose.pack_forget()
        # we can show the graph here
        canvas_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        global type
        type = t
        # G = None     
        if t == 0:
            G = nx.Graph()
            root.title("Setting up undirected unweighted graph")
            # setup buttons for BFS DFS
            bfs_button = tk.Button(side_panel, text='BFS', command=start_bfs)
            dfs_button = tk.Button(side_panel, text='DFS', command=start_dfs)
            bfs_button.pack(side=tk.LEFT)
            dfs_button.pack(side=tk.RIGHT)

        elif t == 1:
            G = nx.DiGraph()
            root.title("Setting up directed unweighted graph")
            # setup buttons for BFS DFS
            bfs_button = tk.Button(side_panel, text='BFS', command=start_bfs)
            dfs_button = tk.Button(side_panel, text='DFS', command=start_dfs)
            bfs_button.pack(side=tk.LEFT)
            dfs_button.pack(side=tk.RIGHT)
        elif t == 2:
            G = nx.Graph()
            root.title("Setting up undirected weighted graph")
            # setup buttons for BFS DFS
            dijkstra_button = tk.Button(side_panel, text='Dijkstra', command=start_dijkstra)
            dijkstra_button.pack(side=tk.LEFT)
        elif t == 3:
            G = nx.DiGraph()
            root.title("Setting up directed weighted graph")
        else:
            tk.messagebox.showerror("Idek What happned but heres t", t)
    
    # 3 tuple functions
    # Function to add a tuple to the list
    def add_tuple3():
        entry_text = entry.get().strip()
        try:
            # Validate the input format
            new_tuple = eval(entry_text)
            if isinstance(new_tuple, tuple) and len(new_tuple) == 3:
                # Add the tuple to the list
                G.add_edge(new_tuple[0], new_tuple[1], weight=new_tuple[2]) 

                edges.append(new_tuple)
                update_listbox()
                entry.delete(0, tk.END)  # Clear the entry field
            else:
                raise ValueError
        except:
            tk.messagebox.showerror("Invalid Input", "Please enter a tuple in the form (u, v, w).")
    # Function to delete a selected tuple
    def delete_tuple3():
        selected_index = listbox.curselection()
        if selected_index:
            index = selected_index[0]
            G.remove_edge(edges[index][0], edges[index][1])
            del edges[index]
            update_listbox()
        else:
            tk.messagebox.showwarning("No Selection", "Please select a tuple to delete.")

    # 2 tuple functions
    # Function to add a tuple to the list
    def add_tuple2():
        entry_text = entry.get().strip()
        try:
            # Validate the input format
            new_tuple = eval(entry_text)
            if isinstance(new_tuple, tuple) and len(new_tuple) == 2:
                # Add the tuple to the list
                G.add_edge(new_tuple[0], new_tuple[1]) # need to change this for 3 tuples
                edges.append(new_tuple)
                update_listbox()
                entry.delete(0, tk.END)  # Clear the entry field
            else:
                raise ValueError
        except:
            tk.messagebox.showerror("Invalid Input", "Please enter a tuple in the form (u, v).")

    # Function to delete a selected tuple
    def delete_tuple2():
        selected_index = listbox.curselection()
        if selected_index:
            index = selected_index[0]
            G.remove_edge(edges[index][0], edges[index][1])
            del edges[index]
            update_listbox()
        else:
            tk.messagebox.showwarning("No Selection", "Please select a tuple to delete.")



    # Function to update the listbox
    def update_listbox():
        print(edges)

        listbox.delete(0, tk.END)  # Clear the listbox
        for item in edges:
            listbox.insert(tk.END, item)  # Add each tuple to the listbox
        update_preview()

    # Function to update the graph preview
    def update_preview():
        global pos
        global type
        ax.clear()
        ax.set_title("Graph Visualization - Setup")
        ax.axis("off")
        # Draw the graph with NetworkX
        pos = nx.spring_layout(G)  # Layout for the graph
        nx.draw(G, pos, ax=ax, with_labels=True, node_color="lightgrey", edge_color="gray", font_weight="bold", )
        # Add edge labels for weighted graphs
        # print("TYPE: ", type)
        if type == 2 or type == 3:
            # print("Adding edge labels")
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
        # Redraw the canvas
        canvas.draw()
    
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

    def start_dijkstra():
        # pass
        name = "Dijkstra"
        nodes, edges = dijkstra(G, s=0)
        run_animation(nodes, edges, name)

    # Function to run the animation
    def run_animation(v_nodes, v_edges, algorithm_name):
        nonlocal G, animation_running
        nonlocal current_anim
        # Stop any existing animation
        # print(animation_running)
        if animation_running:
            return
        animation_running = True

        # Reset the node and edge colors
        node_colors.update({node: "lightgrey" for node in G.nodes()})
        edge_colors.update({edge: "gray" for edge in G.edges()})
        
        # Define the animation step function
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
                    font_weight="bold",
                    arrowsize=15)
            global type
            if type == 2 or type == 3:
                # print("Adding edge labels")
                labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
            ax.set_title(algorithm_name + f" - Visiting Node {current_node}")
            if frame == len(v_nodes) - 1:
                on_animation_complete()
        
        # Function to run when the animation is complete
        def on_animation_complete():
            nonlocal animation_running
            animation_running = False
        # Run the animation
        current_anim = animation.FuncAnimation(fig, step, frames=len(v_nodes), repeat=False, interval=500)
        canvas.draw()
        
        

    # Code Begins here
    root.title("Graph Algo Visualizer - Setup")
    # creating the graph
    # graph_animation.init_graph(root,edges)

    # creating side panel but not shown
    side_panel = tk.Frame(root, width=800)
    
    # Creating a initial menu to choose the graph
    graph_choose = tk.Frame(root)
    graph_choose.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Choose type of graph 
    graph_choose = tk.Frame(root, bg="#333", padx=20, pady=20)
    graph_choose.pack(pady=30)

    # Label for graph selection
    graph_choose_label = tk.Label(
        graph_choose,
        text='Select the Type of Graph',
        font=("Helvetica", 16, "bold"),
    )
    graph_choose_label.pack(pady=10)

    # Style options for buttons
    button_style = {
        "font": ("Helvetica", 12),
    }

    # Buttons for graph types
    undirect_unweight_btn = tk.Button(graph_choose, text='Undirected Graph (Unweighted)', command=lambda t=0: show_side_panel(t), **button_style)
    direct_unweight_btn = tk.Button(graph_choose, text='Directed Graph (Unweighted)', command=lambda t=1: show_side_panel(t), **button_style)
    undirect_weight_btn = tk.Button(graph_choose, text='Undirected Graph (Weighted)', command=lambda t=2: show_side_panel(t), **button_style)
    direct_weight_btn = tk.Button(graph_choose, text='Directed Graph (Weighted)', command=lambda t=3: show_side_panel(t), **button_style)

    # Pack buttons with spacing
    undirect_unweight_btn.pack(pady=5)
    direct_unweight_btn.pack(pady=5)
    undirect_weight_btn.pack(pady=5)
    direct_weight_btn.pack(pady=5)

    
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.clear()
    ax.set_title("Graph Visualization - Setup")
    ax.axis("off")
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    # let us pack this when we actually have something to show
    # canvas_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    root.mainloop()
setup_page()
