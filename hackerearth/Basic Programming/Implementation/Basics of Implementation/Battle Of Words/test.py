import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "3",
            "i will win",
            "will i",
            "today or tomorrow",
            "today or tomorrow and yesterday",
            "i dare you",
            "bad day",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(
            text_trap.getvalue(),
            "You win some.\n" + "You lose some.\n" + "You draw some.\n",
        )


if __name__ == "__main__":
    unittest.main()
