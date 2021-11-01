import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        'abccab',
        '1 3',
        '2 3',
        '3 3',
        '3 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Impossible\n' +
                         'Impossible\n' +
                         'Possible\n' +
                         'Possible\n')


if __name__ == '__main__':
    unittest.main()
