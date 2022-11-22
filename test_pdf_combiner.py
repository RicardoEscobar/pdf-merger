"""2022-11-19 11:34:16 unit test file for controller code"""
import unittest
from pathlib import Path
from controller.pdf_combiner import pdf_combiner


class TestPdfCombiner(unittest.TestCase):
    """Unit tests for the pdf_combiner funtion"""

    def setUp(self) -> None:
        self.list_of_pdf_files = list(Path('.').glob('**/*.pdf'))
        self.test_output_file_param = Path('merge.pdf')

    def test_pdf_list_param_is_a_collection_of_paths(self):
        """Validates that a list or a tuple of paths(pathlib.Paths) are given to the pdf_combiner function."""

        filename_str = str(self.list_of_pdf_files[0])

        test_list_of_paths_param = list(
            map(lambda file: file.name if file.name == filename_str else file,
                self.list_of_pdf_files))

        self.assertRaises(TypeError, pdf_combiner, test_list_of_paths_param)

    def test_output_file_param_is_a_path(self):
        """Validates that the output_file parameter is actually a pathlib.Path object."""

        self.assertRaises(TypeError, pdf_combiner,
                          self.list_of_pdf_files, self.test_output_file_param.__str__())

    def test_file_already_exists(self):
        """Validate File already exists exception raised"""
        pdf_combiner(self.list_of_pdf_files, self.test_output_file_param)
        self.assertRaises(FileExistsError, pdf_combiner,
                          self.list_of_pdf_files, self.test_output_file_param)

    def test_overwrite_file(self):
        """Validate file can be overwritten if overwrite_output_file parameter is set to True."""
        pdf_combiner(self.list_of_pdf_files,
                     self.test_output_file_param, allow_overwrite=True)

        self.assertTrue(self.test_output_file_param.exists(),
                        msg=f'{self.test_output_file_param} file doesn\'t exists.')

    def tearDown(self) -> None:
        Path('merge.pdf').unlink(missing_ok=True)
        Path('out.pdf').unlink(missing_ok=True)


if __name__ == '__main__':
    unittest.main()
