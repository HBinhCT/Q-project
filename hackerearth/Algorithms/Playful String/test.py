import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.read', return_value=' '.join([
        '3',
        'abta',
        'aba',
        'oley',
        'le',
        'tereo',
        're',
    ]))
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'GOOD STRING\n' +
                         'BAD STRING\n' +
                         'GOOD STRING\n')


if __name__ == '__main__':
    unittest.main()
