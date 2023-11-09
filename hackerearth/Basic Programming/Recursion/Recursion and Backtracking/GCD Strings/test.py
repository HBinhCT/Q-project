import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "5",
            "3 1",
            "3 2",
            "5 2",
            "10 4",
            "100 3",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(
            text_trap.getvalue(), "4\n" + "5\n" + "21\n" + "546\n" + "986497880\n"
        )


if __name__ == "__main__":
    unittest.main()
