import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'Bangalore Hyderabad',
        'Bangalore Hyderabad 10000',
        'Bangalore Chennai 4000',
        'Chennai Hyderabad 4000',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Bangalore Chennai Hyderabad 8000\n' +
                         'Bangalore Hyderabad 10000\n')


if __name__ == '__main__':
    unittest.main()
