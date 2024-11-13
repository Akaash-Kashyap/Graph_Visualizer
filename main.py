import tkinter as tk
import graph_animation

global root

def init_tkinter():
    root = tk.Tk()
    '''
    widgets are added here
    '''
    root.title("Graph Algorithm Animation in Tkinter")
    root.geometry("1200x1000")
    # root.attributes('-fullscreen', True)
    # root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

    graph_animation.init_graph(root)

    

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.RIGHT, fill=tk.Y)

    # Add buttons to the frame
    bfs_button = tk.Button(button_frame, text="Run BFS", command=graph_animation.start_bfs)
    bfs_button.pack(pady=10)

    dfs_button = tk.Button(button_frame, text="Run DFS", command=graph_animation.start_dfs)
    dfs_button.pack(pady=10)

    # init the main screen
    # graph_animation.initialize_plot()

    # start Tkinter event loop
    root.mainloop()



init_tkinter()