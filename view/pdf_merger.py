import tkinter as tk


class PdfMerger(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("PDF Merger")
