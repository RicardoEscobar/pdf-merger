"""2022-11-21 13:12:14"""
import unittest
from pathlib import Path


class TestMainFrame(unittest.TestCase):
    """Unit tests for the MainFrame class"""

    def setUp(self) -> None:
        self.list_of_pdf_files = list(Path('.').glob('**/*.pdf'))
        self.test_output_file_param = Path('merge.pdf')

    def test_open_pdf_merge_file_dialog_only_when_files_to_merge_selected(self):
        """Validate the merge PDF file dialog opens when there are PDF files selected."""
        pass

    def tearDown(self) -> None:
        Path('merge.pdf').unlink(missing_ok=True)
        Path('out.pdf').unlink(missing_ok=True)


if __name__ == '__main__':
    unittest.main()
