import tkinter as tk
from tkinter import ttk


class PdfMerger(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("PDF Merger")

        ttk.Label(self, text="Hello, World!").pack()
