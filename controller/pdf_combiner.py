from typing import List
import PyPDF2
from pathlib import Path


def pdf_combiner(pdf_list: List[Path], output_file: Path = Path('out.pdf')) -> None:
    if output_file.exists():
        raise FileExistsError(
            f"Can't create the {output_file} output file. It already exists.")

    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)

    merger.write(output_file)
    merger.close()


if __name__ == '__main__':
    # Create a list of pdf files to merge.
    path_to_pdf_files = Path(r'C:\Users\Jorge\git\pdf-merger')

    output_file_path = path_to_pdf_files / 'merged.pdf'

    list_of_pdf_files = list(path_to_pdf_files.glob('**/*.pdf'))

    try:
        pdf_combiner(pdf_list=list_of_pdf_files, output_file=output_file_path)
    except FileExistsError as e:
        print(e)
