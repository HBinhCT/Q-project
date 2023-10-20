import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "5 3",
            "3 5 1 12 7",
            "1 3",
            "2 3",
            "1 5",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), "1\n" + "0\n" + "3\n")


if __name__ == "__main__":
    unittest.main()
