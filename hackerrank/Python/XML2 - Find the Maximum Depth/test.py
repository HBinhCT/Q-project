import unittest
import xml.etree.ElementTree as etree
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        xml = "<feed xml:lang='en'>\n"
        xml += "  <title>HackerRank</title>\n"
        xml += "  <subtitle lang='en'>Programming challenges</subtitle>\n"
        xml += "  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>\n"
        xml += "  <updated>2013-12-25T12:00:00</updated>\n"
        xml += "</feed>"
        tree = etree.ElementTree(etree.fromstring(xml))
        solution.depth(tree.getroot(), -1)
        self.assertEqual(solution.maxdepth, 1)

    def test_case_1(self):
        xml = "<feed xml:lang='en'>\n"
        xml += "  <title>HackerRank</title>\n"
        xml += "  <subtitle lang='en'>Programming challenges</subtitle>\n"
        xml += "  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>\n"
        xml += "  <updated>2013-12-25T12:00:00</updated>\n"
        xml += "  <entry>\n"
        xml += "  	<author gender='male'>Harsh</author>\n"
        xml += "    <question type='hard'>XML 1</question>\n"
        xml += "    <description type='text'>This is related to XML parsing</description>\n"
        xml += "  </entry>\n"
        xml += "</feed>"
        tree = etree.ElementTree(etree.fromstring(xml))
        solution.depth(tree.getroot(), -1)
        self.assertEqual(solution.maxdepth, 2)


if __name__ == '__main__':
    unittest.main()
