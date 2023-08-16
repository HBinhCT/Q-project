import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "3",
            "3",
            "2 1",
            "1 2",
            "2 9",
            "1",
            "8 1",
            "3",
            "2 5",
            "1 4",
            "1 5",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), "4\n" + "8\n" + "1\n")


if __name__ == "__main__":
    unittest.main()
