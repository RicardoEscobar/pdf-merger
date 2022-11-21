from typing import List, Tuple
import PyPDF2
from pathlib import Path


def pdf_combiner(pdf_collection: List[Path], output_file: Path = Path('out.pdf')) -> None:
    """pdf_combiner function gets a list or tuple of Paths (pathlib.Path) pointing at PDF files, then merges
    them into a single PDF file of the name defined in output_file parameter or out.pdf if no
    argument is passed to the output_file parameter.

    Examples:
    pdf_filepaths = [Path('file1.pdf'), Path('file2.pdf'), Path('file3.pdf')]

    pdf_combiner(pdf_filepaths) # out.pdf is the merged PDF file.
    pdf_combiner(tuple(pdf_filepaths)) # Using a tuple of paths.
    pdf_combiner(pdf_filepaths, output_file=Path('merge.pdf'))
    """
    if not isinstance(pdf_collection, (List, Tuple)):
        raise TypeError("Parameter pdf_list, is not of type List or Tuple")

    for index, path in enumerate(pdf_collection):
        if not isinstance(path, Path):
            raise TypeError(
                f"Element: {index} from {type(pdf_collection)} is not of type {Path}. Value: {path}")

    if not isinstance(output_file, Path):
        raise TypeError("Parameter output_file, is not of type Path")

    if output_file.exists():
        raise FileExistsError(
            f"Can't create the {output_file} output file. It already exists.")

    merger = PyPDF2.PdfMerger()
    for pdf in pdf_collection:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()


if __name__ == '__main__':
    # Create a list of pdf files to merge.
    path_to_pdf_files = Path('c:/').joinpath(
        'Users', 'Jorge', 'git', 'pdf-merger')

    output_file_path = path_to_pdf_files / 'merged.pdf'

    list_of_pdf_files = list(path_to_pdf_files.glob('**/*.pdf'))

    try:
        pdf_combiner(pdf_collection=list_of_pdf_files,
                     output_file=output_file_path)
    except Exception as e:
        print(e)
