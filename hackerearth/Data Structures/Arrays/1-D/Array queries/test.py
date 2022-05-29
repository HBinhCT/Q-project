import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '2',
        '2',
        '2 4',
        '1 5',
        '1',
        '1 2 1',
        '3',
        '2',
        '3 5 1',
        '4 1',
        '3',
        '1 1 2',
        '2 1 3',
        '3 1 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '126 78\n' +
                         '134 168 168 175\n')


if __name__ == '__main__':
    unittest.main()
