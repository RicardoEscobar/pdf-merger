"""Main frame that shows the app to the user."""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


class MainFrame(ttk.Frame):
    """MainFrame inherits from ttk.Frame"""

    def __init__(self, container: ttk.Frame):
        """Init method modified to accomodate user_input."""
        super().__init__(container)

        self.user_input = tk.StringVar()
        self.source_filename = tk.StringVar()
        self.merge_filename = tk.StringVar()
        self.filetypes = (
            ('PDF files', '*.pdf'),
            ('All files', '*.*')
        )

        label = ttk.Label(self, text="Select PDF files to merge: ")
        button = ttk.Button(self, text="Open PDF file(s)",
                            command=self.open_pdf_file_dialog)

        label.pack(side="left")
        button.pack(side="left")

    def greet(self):
        """Prints a customized greet to the console."""
        print(f"Hello, {self.user_input.get()}!")

    def open_pdf_file_dialog(self):
        self.source_filename.set(fd.askopenfilenames(
            title='Open PDF files',
            filetypes=self.filetypes,
            defaultextension='pdf'))

        self.open_pdf_merge_file_dialog()

    def open_pdf_merge_file_dialog(self):
        self.merge_filename.set(fd.asksaveasfilename(
            title='Save PDF merge as...',
            filetypes=self.filetypes,
            defaultextension='pdf'))
