import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        'wcyuogmlrdfphitxjakqvzbnes',
        'jcdokai',
        'miruqopsxthzdcnvkfbglwayje',
        'wgfsyvno',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'codijak\n' +
                         'osnvfgwy\n')


if __name__ == '__main__':
    unittest.main()
