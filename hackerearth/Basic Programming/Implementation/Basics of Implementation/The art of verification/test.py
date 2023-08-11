import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        return_value="http://www.cleartrip.com/signin/service?username=test&pwd=test&profile=developer&role=ELITE&key=manager",
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(
            text_trap.getvalue(),
            "username: test\n"
            + "pwd: test\n"
            + "profile: developer\n"
            + "role: ELITE\n"
            + "key: manager\n",
        )


if __name__ == "__main__":
    unittest.main()
