import io
import unittest
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    def test_case_0(self):
        with patch('builtins.input', side_effect=['3', '1 2 3']):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
            self.assertEqual(fake_stdout.getvalue(),
                             'Array is sorted in 0 swaps.\n'
                             + 'First Element: 1\n'
                             + 'Last Element: 3\n')

    def test_case_1(self):
        with patch('builtins.input', side_effect=['3', '3 2 1']):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
                reload(solution)
            self.assertEqual(fake_stdout.getvalue(),
                             'Array is sorted in 3 swaps.\n'
                             + 'First Element: 1\n'
                             + 'Last Element: 3\n')


if __name__ == '__main__':
    unittest.main()
