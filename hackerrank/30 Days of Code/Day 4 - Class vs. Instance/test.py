import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        '-1',
        '10',
        '16',
        '18',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Age is not valid, setting age to 0.' + '\n' +
                         'You are young.' + '\n' +
                         'You are young.' + '\n' +
                         '\n' +
                         'You are young.' + '\n' +
                         'You are a teenager.' + '\n' +
                         '\n' +
                         'You are a teenager.' + '\n' +
                         'You are old.' + '\n' +
                         '\n' +
                         'You are old.' + '\n' +
                         'You are old.' + '\n' +
                         '\n')


if __name__ == '__main__':
    unittest.main()
