# tests/test_main.py

from src.main import main
from src.my_module import my_function
import unittest
from unittest.mock import patch
import io

class TestMain(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_output(self, mock_stdout):
        main()
        expected_output = "Hello from main!\nHello from my_module!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_my_function(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            my_function()
            expected_output = "Hello from my_module!\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()