"""Main frame that shows the app to the user."""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from controller.pdf_combiner import pdf_combiner
from controller.str_to_path import str_to_path
from pathlib import Path


class MainFrame(ttk.Frame):
    """MainFrame inherits from ttk.Frame"""

    def __init__(self, container: ttk.Frame):
        """Init method modified to accomodate user_input."""
        super().__init__(container)

        self.user_input = tk.StringVar()
        self.source_filenames = tuple()
        self.merge_filename = Path('merge.pdf')
        self.filetypes = (
            ('PDF files', '*.pdf'),
            ('All files', '*.*')
        )

        label = ttk.Label(self, text="Select PDF files to merge: ")
        button = ttk.Button(self, text="Open PDF file(s)",
                            command=self.open_pdf_load_files_dialog)

        label.pack(side="left")
        button.pack(side="left")

    def greet(self) -> None:
        """Prints a customized greet to the console."""
        print(f"Hello, {self.user_input.get()}!")

    def open_pdf_load_files_dialog(self) -> None:
        self.source_filenames = fd.askopenfilenames(
            title='Load PDF files',
            filetypes=self.filetypes,
            defaultextension='.pdf')

        if len(self.source_filenames) > 0:
            self.open_pdf_merge_file_dialog()

    def open_pdf_merge_file_dialog(self) -> None:
        self.merge_filename = Path(fd.asksaveasfilename(
            title='Save PDF merge as...',
            filetypes=self.filetypes,
            defaultextension='.pdf'))

        pdf_combiner(str_to_path(self.source_filenames),
                     Path(self.merge_filename),
                     allow_overwrite=True)
