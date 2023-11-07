import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "3",
            "5",
            "3 2 0 7 -1",
            "8",
            "3",
            "-1 3 3",
            "4",
            "3",
            "4 -5 1",
            "5",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), "YES\n" + "NO\n" + "YES\n")


if __name__ == "__main__":
    unittest.main()
