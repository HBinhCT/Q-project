import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "2",
            "4",
            "4 5 10 3",
            "5",
            "1 3 5 4 5",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), "44\n" + "0\n")


if __name__ == "__main__":
    unittest.main()
