"""2022-11-19 11:34:16 unit test file for controller code"""
import unittest
from pathlib import Path
from controller.pdf_combiner import pdf_combiner


class TestPdfCombiner(unittest.TestCase):
    """Unit tests for the pdf_combiner funtion"""

    def setUp(self) -> None:
        self.list_of_pdf_files = list(Path('.').glob('**/*.pdf'))

    def test_pdf_list_param_is_a_list_of_paths(self):
        """Test that validates that the List of paths given to the pdf_combiner function is actually
        a list of pathlib.Paths objects"""
        test_tuple_of_paths_param = tuple(self.list_of_pdf_files)

        test_list_of_paths_param = list(
            map(lambda file: file.name if file.name == 'twopage.pdf' else file,
                self.list_of_pdf_files))

        self.assertRaises(TypeError, pdf_combiner, test_tuple_of_paths_param)
        self.assertRaises(TypeError, pdf_combiner, test_list_of_paths_param)

    def test_output_file_param_is_a_path(self):
        """Test that validates that the output_file parameter is actually a pathlib.Path object."""
        test_output_file_param = 'merge.pdf'

        self.assertRaises(TypeError, pdf_combiner,
                          self.list_of_pdf_files, test_output_file_param)

    def tearDown(self) -> None:
        Path('merge.pdf').unlink(missing_ok=True)
        Path('out.pdf').unlink(missing_ok=True)


if __name__ == '__main__':
    unittest.main()
