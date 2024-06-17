import unittest
from unittest.mock import patch
from io import StringIO
import sys
import argparse

# Assuming the process_message function is in a file named 
from script import process_message

class TestProcessMessage(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_process_message_with_argument(self, mock_stdout):
        # Test with a direct message argument
        process_message("Hello, World!")
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, World!")
    
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(message="Hello from argparse"))
    @patch('sys.stdout', new_callable=StringIO)
    def test_process_message_with_argparse(self, mock_stdout, mock_parse_args):
        # Test with argparse
        process_message()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello from argparse")

if __name__ == '__main__':
    unittest.main()
