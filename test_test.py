import unittest
from unittest.mock import patch, MagicMock
import io
import sys

# Prevent the input prompt from blocking our tests
with patch('builtins.input', return_value='TestUser'):
    import test

class TestDoSomething(unittest.TestCase):
    """Tests for DoSomething function"""

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_with_none_input(self, mock_stdout):
        """Test DoSomething with None as first parameter"""
        test.DoSomething(None, 5)
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid value for x")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_with_valid_division(self, mock_stdout):
        """Test DoSomething with valid division case"""
        test.DoSomething(10, 2)
        self.assertEqual(mock_stdout.getvalue().strip(), "5.0")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_with_zero_divisor(self, mock_stdout):
        """Test DoSomething when y is zero"""
        test.DoSomething(10, 0)
        self.assertEqual(mock_stdout.getvalue().strip(), "y is not zero")


class TestSampleClass(unittest.TestCase):
    """Tests for sampleClass"""

    def test_constructor(self):
        """Constructor sets Name attribute correctly"""
        instance = test.sampleClass("TestName")
        self.assertEqual(instance.Name, "TestName")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_printname(self, mock_stdout):
        """printname prints the Name attribute"""
        instance = test.sampleClass("TestName")
        instance.printname()
        self.assertEqual(mock_stdout.getvalue().strip(), "TestName")


class TestModuleImport(unittest.TestCase):
    """Tests for module import behavior"""

    @patch('builtins.input', return_value='TestUser')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_greeting_on_import(self, mock_stdout, mock_input):
        """Greeting is printed based on the patched input on import"""
        import importlib
        importlib.reload(test)
        # Ensure input() was called exactly once
        self.assertEqual(mock_input.call_count, 1)
        # Ensure the greeting contains the patched name
        self.assertIn("Hello TestUser", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
