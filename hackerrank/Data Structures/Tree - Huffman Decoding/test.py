import io
import unittest
from contextlib import redirect_stdout
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', return_value='ABACA')
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'ABACA')

    @patch('builtins.input', return_value='Rumpelstiltskin')
    def test_case_1(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
            reload(solution)
        self.assertEqual(text_trap.getvalue(), 'Rumpelstiltskin')

    @patch('builtins.input', return_value='howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood?')
    def test_case_2(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
            reload(solution)
        self.assertEqual(text_trap.getvalue(), 'howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood?')


if __name__ == '__main__':
    unittest.main()
