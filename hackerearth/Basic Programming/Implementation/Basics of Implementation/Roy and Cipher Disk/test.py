import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "3",
            "aeiou",
            "hackerearth",
            "correct",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(
            text_trap.getvalue(),
            "0 4 4 6 6 \n"
            + "7 -7 2 8 -6 13 13 -4 -9 2 -12 \n"
            + "2 12 3 0 13 -2 -9 \n",
        )


if __name__ == "__main__":
    unittest.main()
