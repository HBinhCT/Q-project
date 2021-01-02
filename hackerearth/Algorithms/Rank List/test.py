import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        'arun 8 28',
        'harshit 10 30',
        'surya 7 26',
        'satyam 27 6',
        'arun 1 28',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'harshit 10 30\n' +
                         'arun 1 28\n' +
                         'arun 8 28\n' +
                         'surya 7 26\n' +
                         'satyam 27 6\n')


if __name__ == '__main__':
    unittest.main()
