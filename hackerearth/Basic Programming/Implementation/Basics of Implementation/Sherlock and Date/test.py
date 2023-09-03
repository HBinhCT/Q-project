import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "3",
            "23 July 1914",
            "2 August 2000",
            "5 November 1999",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(
            text_trap.getvalue(),
            "22 July 1914\n" + "1 August 2000\n" + "4 November 1999\n",
        )


if __name__ == "__main__":
    unittest.main()
