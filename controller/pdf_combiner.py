from typing import List, Tuple
import PyPDF2
from pathlib import Path


def pdf_combiner(pdf_collection: List[Path] | Tuple[Path],
                 output_file: Path = Path('out.pdf'),
                 allow_overwrite:  bool = False) -> None:
    """pdf_combiner function gets a list or tuple of Paths (pathlib.Path) pointing at PDF files,
    then merges them into a single PDF file of the name defined in output_file parameter or out.pdf
    if no argument is passed to the output_file parameter.

    Use allow_overwrite parameter (default=False) to set if you'd like to overwrite an existing file
    during merge.

    Examples:
    pdf_filepaths = [Path('file1.pdf'), Path('file2.pdf'), Path('file3.pdf')]

    pdf_combiner(pdf_filepaths) # out.pdf is the merged PDF file.
    pdf_combiner(tuple(pdf_filepaths)) # Using a tuple of paths.
    pdf_combiner(pdf_filepaths, output_file=Path('merge.pdf'))
    pdf_combiner(pdf_filepaths, output_file=Path('merge.pdf'), allow_overwrite=True)
    """
    if not isinstance(pdf_collection, (List, Tuple)):
        raise TypeError("Parameter pdf_list, is not of type List or Tuple")

    for index, path in enumerate(pdf_collection):
        if not isinstance(path, Path):
            raise TypeError(
                f"Element: {index} from {type(pdf_collection)} is not of type {Path}. Value: {path}")

    if not isinstance(output_file, Path):
        raise TypeError("Parameter output_file, is not of type Path")

    if output_file.exists() and not allow_overwrite:
        raise FileExistsError(
            f"Can't create the {output_file} output file. It already exists.")

    merger = PyPDF2.PdfMerger()
    for pdf in pdf_collection:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()


if __name__ == '__main__':
    pass
