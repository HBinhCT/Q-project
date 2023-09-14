import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "8",
            "-1 -4  4 -2 0 1 4 -5",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), "7\n")


if __name__ == "__main__":
    unittest.main()
