"""Main frame that shows the app to the user."""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from pathlib import Path
import logging
from controller.pdf_combiner import pdf_combiner
from controller.str_to_path import str_to_path


class MainFrame(ttk.Frame):
    """MainFrame inherits from ttk.Frame"""

    def __init__(self, container: ttk.Frame):
        """Init method modified to accomodate user_input."""
        super().__init__(container)

        self.logger = logging.getLogger('test_main_frame.main_frame.MainFrame')
        self.source_filenames = tuple()
        self.merge_filename = Path('merge.pdf')
        self.filetypes = (
            ('PDF files', '*.pdf'),
            ('All files', '*.*')
        )
        self.pdf_listvar = tk.StringVar()

        button_open_pdf = ttk.Button(self, text="Open PDF file(s)",
                                     command=self.open_pdf_load_files_dialog, width=20)
        button_merge_pdf = ttk.Button(self, text="Merge PDF file",
                                      command=self.open_pdf_merge_file_dialog, width=20)
        button_clear_listbox = ttk.Button(self, text="Clear list",
                                          command=self.clear_list, width=20)
        button_clear_selected = ttk.Button(self, text="Clear selected",
                                           command=self.clear_selected, width=20)
        self.pdf_listbox = tk.Listbox(
            self,
            listvariable=self.pdf_listvar,
            height=5,  # len(self.source_filenames),
            selectmode='extended')

        button_open_pdf.pack(side="top", ipady=5, ipadx=80)
        button_merge_pdf.pack(side="top", ipady=5, ipadx=80)
        button_clear_listbox.pack(side="top", ipady=5, ipadx=80)
        button_clear_selected.pack(side="top", ipady=5, ipadx=80)
        self.pdf_listbox.pack(side="top", fill='both', expand=True)

    def open_pdf_load_files_dialog(self) -> None:
        tuple_selected_pdf_files = fd.askopenfilenames(
            title='Load PDF files',
            filetypes=self.filetypes,
            defaultextension='.pdf')

        if tuple_selected_pdf_files == '':
            tuple_selected_pdf_files = tuple()

        self.source_filenames = self.source_filenames + tuple_selected_pdf_files

        # Updates listbox widget after opening file list
        self.pdf_listvar.set(self.source_filenames)
        self.pdf_listbox['height'] = len(self.source_filenames)

    def open_pdf_merge_file_dialog(self) -> None:
        if len(self.source_filenames) > 0:
            self.merge_filename = Path(fd.asksaveasfilename(
                title='Save PDF merge as...',
                filetypes=self.filetypes,
                defaultextension='.pdf'))

            pdf_combiner(str_to_path(self.source_filenames),
                         Path(self.merge_filename),
                         allow_overwrite=True)
        else:
            raise ValueError('The list of PDF files is empty.')

    def clear_list(self) -> None:
        """Clear listbox of all PDF filenames."""
        self.source_filenames = tuple()
        self.pdf_listvar.set(self.source_filenames)

    def clear_selected(self) -> None:
        """Clear listbox of selected PDF filenames."""
        self.logger.debug('Clear selected ran.')
        # seleccionar items
        self.logger.debug('pdf_listbox.curselection=%s',
                          self.pdf_listbox.curselection())

        for line in self.pdf_listbox.curselection():
            self.pdf_listbox.delete(line)

        end_index = self.pdf_listbox.size() - 1
        new_tuple_pdf = self.pdf_listbox.get(0, end_index)

        self.source_filenames = new_tuple_pdf
        self.pdf_listvar.set(self.source_filenames)
