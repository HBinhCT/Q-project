import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            html = '<head>\n' + \
                   '<title>HTML</title>\n' + \
                   '</head>\n' + \
                   '<object type="application/x-flash"\n' + \
                   '  data="your-file.swf"\n' + \
                   '  width="0" height="0">\n' + \
                   '  <!-- <param name="movie" value="your-file.swf" /> -->\n' + \
                   '  <param name="quality" value="high"/>\n' + \
                   '</object>'
            parser = solution.MyHTMLParser()
            parser.feed(html)
        self.assertEqual(text_trap.getvalue(),
                         'head\n' +
                         'title\n' +
                         'object\n' +
                         '-> type > application/x-flash\n' +
                         '-> data > your-file.swf\n' +
                         '-> width > 0\n' +
                         '-> height > 0\n' +
                         'param\n' +
                         '-> name > quality\n' +
                         '-> value > high\n')


if __name__ == '__main__':
    unittest.main()
