import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "2",
            "4 3",
            "hgeb ",
            "ebh",
            "7 3",
            "xyzxyxx",
            "xyx",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), "1\n" + "2\n")


if __name__ == "__main__":
    unittest.main()
