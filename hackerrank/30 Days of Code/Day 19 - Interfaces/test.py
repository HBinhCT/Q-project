import io
import unittest
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    def test_case_0(self):
        with patch('builtins.input', return_value='6'):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
            self.assertEqual(fake_stdout.getvalue(),
                             'I implemented: AdvancedArithmetic\n'
                             + '12\n')

    def test_case_1(self):
        with patch('builtins.input', return_value='1'):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
                reload(solution)
            self.assertEqual(fake_stdout.getvalue(),
                             'I implemented: AdvancedArithmetic\n'
                             + '1\n')

    def test_case_2(self):
        with patch('builtins.input', return_value='20'):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
                reload(solution)
            self.assertEqual(fake_stdout.getvalue(),
                             'I implemented: AdvancedArithmetic\n'
                             + '42\n')


if __name__ == '__main__':
    unittest.main()
