"""2022-11-21 13:12:14"""
import unittest
from pathlib import Path
import logging
from view.main_frame import MainFrame
from view.pdf_merger import PdfMerger

# Crates a logging system for this unit test file
logger = logging.getLogger('test_main_frame')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler_debug = logging.FileHandler('test_main_frame.log')
file_handler_debug.setLevel(logging.DEBUG)
file_handler_debug.setFormatter(formatter)

logger.addHandler(file_handler_debug)


class TestMainFrame(unittest.TestCase):
    """Unit tests for the MainFrame class"""

    def setUp(self) -> None:
        self.list_of_pdf_files = list(Path('.').glob('**/*.pdf'))
        self.test_output_file_param = Path('merge.pdf')
        self.pdf_merger = PdfMerger()
        self.main_frame = MainFrame(self.pdf_merger)
        self.main_frame.pdf_listvar.set(tuple(self.list_of_pdf_files))

    def test_open_pdf_merge_file_dialog(self):
        """Validate that there is a list of PDF files to merge."""
        self.assertRaises(
            ValueError, MainFrame.open_pdf_merge_file_dialog, self.main_frame)

    def test_clear_list_pdf_files(self):
        """Validate that the clear list button works as intended."""
        logger.debug('pdf_listvar=%s', self.main_frame.pdf_listvar.get())
        clear_list = self.main_frame.clear_list
        clear_list()
        logger.debug('Cleared pdf_listvar %s',
                     self.main_frame.pdf_listvar.get())
        self.assertEqual(self.main_frame.pdf_listvar.get(), '')

    def test_clear_selected(self):
        """Validate that clear_selected method deletes selected PDF files from listbox"""
        clear_selected = self.main_frame.clear_selected
        logger.debug('self.main_frame.listbox=%s',
                     self.main_frame.pdf_listvar.get())
        # get selected file(s), index
        # delete from list_of_pdf_files
        # delete from pdf_listvar
        clear_selected()

    def tearDown(self) -> None:
        Path('merge.pdf').unlink(missing_ok=True)
        Path('out.pdf').unlink(missing_ok=True)


if __name__ == '__main__':
    unittest.main()
