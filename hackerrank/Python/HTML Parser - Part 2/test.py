import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            html = '<!--[if IE 9]>IE9-specific content\n' + \
                   '<![endif]-->\n' + \
                   '<div> Welcome to HackerRank</div>\n' + \
                   '<!--[if IE 9]>IE9-specific content<![endif]-->'
            parser = solution.MyHTMLParser()
            parser.feed(html)
        self.assertEqual(text_trap.getvalue(),
                         '>>> Multi-line Comment\n' +
                         '[if IE 9]>IE9-specific content\n' +
                         '<![endif]\n' +
                         '>>> Data\n' +
                         ' Welcome to HackerRank\n' +
                         '>>> Single-line Comment\n' +
                         '[if IE 9]>IE9-specific content<![endif]\n')


if __name__ == '__main__':
    unittest.main()
