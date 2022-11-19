import tkinter as tk
from tkinter import ttk
from controller.pdf_combiner import pdf_combiner
from controller.greet import greet

root = tk.Tk()
root.title("Greeter")

# Here we create an instances of the StringVar() class, which is to track the content of widgets
user_name = tk.StringVar()

# We define two frames to keep the input on different lines. In the next version we will switch to grid() geometry.
# Padding accepts a tuple of up to four values. Clockwise like CSS.
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

buttons = ttk.Frame(root, padding=(20, 10))
buttons.pack(fill="both")

greet_button = ttk.Button(buttons, text="Greet",
                          command=lambda: greet(user_name.get()))
greet_button.pack(side="left", fill="x", expand=True)
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.pack(side="right", fill="x", expand=True)

root.mainloop()
