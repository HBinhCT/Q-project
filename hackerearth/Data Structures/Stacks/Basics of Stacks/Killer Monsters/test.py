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
            "3 0 3 4 1",
            "5",
            "5 4 3 2 1",
            "7",
            "1 2 3 3 4 4 0",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(
            text_trap.getvalue(), "1 2 1 1 2\n" + "1 2 3 4 5\n" + "1 1 1 1 1 1 2\n"
        )


if __name__ == "__main__":
    unittest.main()
