import io
import unittest
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    def test_case_0(self):
        with patch('builtins.input', return_value='racecar'):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
            self.assertEqual(fake_stdout.getvalue(), 'The word, racecar, is a palindrome.\n')

    def test_case_1(self):
        with patch('builtins.input', return_value='yes'):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
                reload(solution)
            self.assertEqual(fake_stdout.getvalue(), 'The word, yes, is not a palindrome.\n')


if __name__ == '__main__':
    unittest.main()
