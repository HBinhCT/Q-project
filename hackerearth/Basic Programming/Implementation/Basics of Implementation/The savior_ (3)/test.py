import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "4",
            "2",
            "1 1",
            "4",
            "1 2 3 4",
            "4",
            "2 4 6 8",
            "3",
            "1 3 3",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), "0\n" + "2\n" + "6\n" + "2\n")


if __name__ == "__main__":
    unittest.main()
