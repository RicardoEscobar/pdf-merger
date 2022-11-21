from view.set_dpi_awareness import set_dpi_awareness
from view.pdf_merger import PdfMerger
from view.main_frame import MainFrame


set_dpi_awareness()

root = PdfMerger()
main_frame = MainFrame(root).pack()
root.mainloop()
