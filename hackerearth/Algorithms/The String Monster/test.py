import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '4',
        'hey',
        'rain',
        'day',
        'wet',
        'draaxiny',
        '4',
        'bump',
        'ud',
        'bish',
        'chau',
        'bichhusa',
    ])
    def test_case_0(self, input_mock=None, inputs_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'NO\n' +
                         'YES\n')


if __name__ == '__main__':
    unittest.main()
