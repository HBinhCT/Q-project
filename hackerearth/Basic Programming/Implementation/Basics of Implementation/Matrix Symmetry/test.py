import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "3",
            "4",
            "*.*.",
            ".*.*",
            "*.*.",
            ".*.*",
            "3",
            ".*.",
            "*.*",
            ".*.",
            "3",
            "..*",
            "**.",
            "..*",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), "NO\n" + "BOTH\n" + "HORIZONTAL\n")


if __name__ == "__main__":
    unittest.main()
