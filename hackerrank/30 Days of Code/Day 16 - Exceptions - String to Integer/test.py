import io
import unittest
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    def test_case_0(self):
        with patch('builtins.input', return_value='3'):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
            self.assertEqual(fake_stdout.getvalue(), '3\n')

    def test_case_1(self):
        with patch('builtins.input', return_value='za'):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
                reload(solution)
            self.assertEqual(fake_stdout.getvalue(), 'Bad String\n')

    def test_case_2(self):
        with patch('builtins.input', return_value='3134'):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
                reload(solution)
            self.assertEqual(fake_stdout.getvalue(), '3134\n')

    def test_case_3(self):
        with patch('builtins.input', return_value='abc'):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
                reload(solution)
            self.assertEqual(fake_stdout.getvalue(), 'Bad String\n')


if __name__ == '__main__':
    unittest.main()
