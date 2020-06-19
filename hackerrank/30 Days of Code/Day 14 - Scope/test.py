import io
import unittest
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    def test_case_0(self):
        with patch('builtins.input', side_effect=['3', '1 2 5']):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
            self.assertEqual(fake_stdout.getvalue(), '4\n')

    def test_case_1(self):
        with patch('builtins.input', side_effect=['5', '8 19 3 2 7']):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
                reload(solution)
        self.assertEqual(fake_stdout.getvalue(), '17\n')

    def test_case_2(self):
        with patch('builtins.input', side_effect=['5', '8 8 8 8 8']):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
                reload(solution)
        self.assertEqual(fake_stdout.getvalue(), '0\n')


if __name__ == '__main__':
    unittest.main()
