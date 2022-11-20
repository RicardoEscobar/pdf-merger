"""2022-11-20 11:12:43"""
import unittest
from controller.greet import greet


class TestGreet(unittest.TestCase):
    """Unit tests for the greet funtion"""

    def test_user_name_is_str(self):
        """Test user_name is str or None"""
        test_user_name_param = 1
        self.assertRaises(TypeError, greet, test_user_name_param)


if __name__ == '__main__':
    unittest.main()
