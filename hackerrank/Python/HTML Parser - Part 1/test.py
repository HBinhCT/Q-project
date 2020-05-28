import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            parser = solution.MyHTMLParser()
            parser.feed('<html><head><title>HTML Parser - I</title></head>')
            parser.feed("<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>")
        self.assertEqual(text_trap.getvalue(),
                         'Start : html\n' +
                         'Start : head\n' +
                         'Start : title\n' +
                         'End   : title\n' +
                         'End   : head\n' +
                         'Start : body\n' +
                         '-> data-modal-target > None\n' +
                         '-> class > 1\n' +
                         'Start : h1\n' +
                         'End   : h1\n' +
                         'Empty : br\n' +
                         'End   : body\n' +
                         'End   : html\n')


if __name__ == '__main__':
    unittest.main()
