import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '9',
        'BANANA FRIES 12',
        'POTATO CHIPS 30',
        'APPLE JUICE 10',
        'CANDY 5',
        'APPLE JUICE 10',
        'CANDY 5',
        'CANDY 5',
        'CANDY 5',
        'POTATO CHIPS 30',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'BANANA FRIES 12\n'
                         + 'POTATO CHIPS 60\n'
                         + 'APPLE JUICE 20\n'
                         + 'CANDY 20\n')


if __name__ == '__main__':
    unittest.main()
