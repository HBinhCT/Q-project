import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "sys.stdin.readline",
        side_effect=[
            "2",
            "zazaz",
            "goodarjit",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), "Palindrome\n" + "204120000\n")


if __name__ == "__main__":
    unittest.main()
