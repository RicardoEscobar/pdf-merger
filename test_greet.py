"""2022-11-20 11:12:43"""
import unittest
import logging
from controller.greet import greet

# Crates a logging system for this unit test file
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler_debug = logging.FileHandler('error.log')
file_handler_debug.setLevel(logging.ERROR)
file_handler_debug.setFormatter(formatter)

logger.addHandler(file_handler_debug)


class TestGreet(unittest.TestCase):
    """Unit tests for the greet funtion"""

    def test_user_name_is_str(self):
        """Test user_name is str or None"""
        test_user_name_param = 1
        self.assertRaises(TypeError, greet, test_user_name_param)
        logger.info('Test INFO user_name is str or None')

    def test_greet_returns_str(self):
        """Test that the greet function returns a str with the message."""
        user_name = "Jorge"
        expected_result = "Hello, Jorge."
        actual_result = greet(user_name)
        self.assertEqual(expected_result, actual_result)
        logger.debug('greet("Jorge") = %s', actual_result)

    def test_greet_returns_hello_world(self):
        """Test that the greet function returns 'Hello, World!' message."""
        expected_result = "Hello, World!"
        actual_result = greet()
        self.assertEqual(expected_result, actual_result)
        logger.debug('greet() = %s', actual_result)

        expected_result = "Hello, World!"
        actual_result = greet(None)
        self.assertEqual(expected_result, actual_result)
        logger.debug('greet(None) = %s', actual_result)


if __name__ == '__main__':
    unittest.main()
