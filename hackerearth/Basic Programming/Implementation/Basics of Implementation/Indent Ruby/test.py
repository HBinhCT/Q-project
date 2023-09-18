import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "class YabbaDabbaDoo",
            "        def foo",
            "        if foo == 42",
            "        puts 'world hello'",
            "          elsif foo == 24",
            "          puts 'bk201'",
            "        else",
            "        puts 'congrats!'",
            "          end",
            "  end",
            "end",
        ],
    )
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(
            text_trap.getvalue(),
            "class YabbaDabbaDoo\n"
            + " def foo\n"
            + "  if foo == 42\n"
            + "   puts 'world hello'\n"
            + "  elsif foo == 24\n"
            + "   puts 'bk201'\n"
            + "  else\n"
            + "   puts 'congrats!'\n"
            + "  end\n"
            + " end\n"
            + "end\n",
        )


if __name__ == "__main__":
    unittest.main()
