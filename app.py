import PyPDF2
import sys
from controller.pdf_combiner import pdf_combiner


inputs = sys.argv[1:]

print(pdf_combiner)
pdf_combiner(inputs)