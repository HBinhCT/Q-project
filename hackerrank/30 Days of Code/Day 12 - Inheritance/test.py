import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'Heraldo Memelli 8135627',
        '2',
        '100 80',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Name: Memelli, Heraldo' + '\n' +
                         'ID: 8135627' + '\n' +
                         'Grade: O' + '\n')


if __name__ == '__main__':
    unittest.main()
