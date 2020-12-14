import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        'a 12 c d',
        'b 13 d e',
        'd 12 f k',
        'zz 13 m co',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2\n' +
                         '1 3\n' +
                         '2 4\n')


if __name__ == '__main__':
    unittest.main()
