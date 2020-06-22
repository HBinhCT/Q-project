import io
import unittest
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    def test_case_0(self):
        with patch('builtins.input', side_effect=['3', '12', '5', '7']):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
            self.assertEqual(fake_stdout.getvalue(),
                             'Not prime\n'
                             + 'Prime\n'
                             + 'Prime\n')

    def test_case_1(self):
        with patch('builtins.input', side_effect=['2', '31', '33']):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
                reload(solution)
            self.assertEqual(fake_stdout.getvalue(),
                             'Prime\n'
                             + 'Not prime\n')


if __name__ == '__main__':
    unittest.main()
