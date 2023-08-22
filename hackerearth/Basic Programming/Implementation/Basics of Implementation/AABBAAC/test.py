import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "2",
            "3 7",
            "a",
            "b",
            "c",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "2 6",
            "ty",
            "qwe",
            "0",
            "2",
            "3",
            "4",
            "6",
            "1",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), "aabbaac\n" + "tytqey\n")


if __name__ == "__main__":
    unittest.main()
