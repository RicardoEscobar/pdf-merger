"""2022-11-20 11:12:43"""
import unittest
import logging
from controller.greet import greet

# Configure the logging system to create a 'test_greet.log' file to test out the logging system.
logging.basicConfig(filename='test_greet.log',
                    level=logging.INFO, format='%(levelname)s:%(message)s')


class TestGreet(unittest.TestCase):
    """Unit tests for the greet funtion"""

    def test_user_name_is_str(self):
        """Test user_name is str or None"""
        test_user_name_param = 1
        self.assertRaises(TypeError, greet, test_user_name_param)
        logging.info('Test user_name is str or None')

    def test_greet_returns_str(self):
        """Test that the greet function returns a str with the message."""
        user_name = "Jorge"
        expected_result = "Hello, Jorge."
        actual_result = greet(user_name)
        self.assertEqual(expected_result, actual_result)
        logging.info('greet("Jorge") = %s', actual_result)

    def test_greet_returns_hello_world(self):
        """Test that the greet function returns 'Hello, World!' message."""
        expected_result = "Hello, World!"
        actual_result = greet()
        self.assertEqual(expected_result, actual_result)
        logging.info('greet() = %s', actual_result)

        expected_result = "Hello, World!"
        actual_result = greet(None)
        self.assertEqual(expected_result, actual_result)
        logging.info('greet(None) = %s', actual_result)


if __name__ == '__main__':
    unittest.main()
