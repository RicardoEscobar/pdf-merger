from typing import List
import PyPDF2


def pdf_combiner(pdf_list: List[str], output_file: str = 'out.pdf') -> None:
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write(output_file)

if __name__ == '__main__':
    print('Executing from module: pdf_combiner.py')