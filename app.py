from tkinter import ttk
from view.set_dpi_awareness import set_dpi_awareness
from view.pdf_merger import PdfMerger
from view.main_frame import MainFrame


set_dpi_awareness()

root = PdfMerger()
container = ttk.Frame(root)
main_frame = MainFrame(container)
container.pack(fill='both', expand=True)
main_frame.pack(fill='both', expand=True)
root.mainloop()
