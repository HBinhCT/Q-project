import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3 4',
        'vasya',
        'petya',
        'kolya',
        'vasya errichto 21',
        'kolya petr 22',
        'petya egor 19',
        'vasya tourist 19',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'kolya\n' +
                         'petr 22\n' +
                         'petya\n' +
                         'egor 19\n' +
                         'vasya\n' +
                         'tourist 19\n' +
                         'errichto 21\n')


if __name__ == '__main__':
    unittest.main()
