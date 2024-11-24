import tkinter as tk
from tkinter import messagebox
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def setup_page():
    # Create the main window
    root = tk.Tk()
    root.title("Graph Algo Visualizer - Setup")
    G = nx.Graph()
    edges = []  # List to store graph edges

    # Functions for adding, deleting, and visualizing tuples
    def add_tuple():
        entry_text = entry.get().strip()
        try:
            new_tuple = eval(entry_text)  # Validate the input format
            if isinstance(new_tuple, tuple) and len(new_tuple) == 2:
                G.add_edge(new_tuple[0], new_tuple[1])
                edges.append(new_tuple)
                update_listbox()
                entry.delete(0, tk.END)  # Clear the entry field
            else:
                raise ValueError
        except:
            messagebox.showerror("Invalid Input", "Please enter a tuple in the form (x, y).")

    def delete_tuple():
        selected_index = listbox.curselection()
        if selected_index:
            index = selected_index[0]
            edge = edges[index]
            G.remove_edge(edge[0], edge[1])
            del edges[index]
            update_listbox()
        else:
            messagebox.showwarning("No Selection", "Please select a tuple to delete.")

    def update_listbox():
        listbox.delete(0, tk.END)
        for item in edges:
            listbox.insert(tk.END, item)
        update_graph()

    def update_graph():
        # Clear the current figure
        ax.clear()
        ax.set_title("Graph Visualization")
        ax.axis("off")
        
        # Draw the graph with NetworkX
        pos = nx.spring_layout(G)  # Layout for the graph
        nx.draw(G, pos, ax=ax, with_labels=True, node_color="lightblue", edge_color="gray", font_weight="bold")
        
        # Redraw the canvas
        canvas.draw()

    def show_side_panel(t):
        side_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        graph_choose.pack_forget()

    # Create the side panel
    side_panel = tk.Frame(root, width=800)

    # Initial menu to choose the graph
    graph_choose = tk.Frame(root)
    graph_choose.pack()

    # Graph selection buttons
    undirect_unweight_btn = tk.Button(graph_choose, text='Undirected Graph, unweighted', command=lambda t=0: show_side_panel(t))
    undirect_unweight_btn.pack(pady=5)

    # Entry for adding tuples
    entry_label = tk.Label(side_panel, text="Enter Tuple (x, y):")
    entry_label.pack(pady=5)

    entry = tk.Entry(side_panel, width=30)
    entry.pack(pady=5)

    add_button = tk.Button(side_panel, text="Add Tuple", command=add_tuple)
    add_button.pack(pady=5)

    # Listbox to display tuples
    listbox_label = tk.Label(side_panel, text="Tuples List:")
    listbox_label.pack(pady=5)

    listbox = tk.Listbox(side_panel, width=30, height=10)
    listbox.pack(pady=5)

    # Button to delete a tuple
    delete_button = tk.Button(side_panel, text="Delete Selected Tuple", command=delete_tuple)
    delete_button.pack(pady=10)

    # Matplotlib figure and canvas
    fig, ax = plt.subplots(figsize=(5, 5))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    root.mainloop()

setup_page()
