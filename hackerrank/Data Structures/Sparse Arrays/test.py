import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertListEqual(solution.matchingStrings(
            ['aba', 'baba', 'aba', 'xzxb'],
            ['aba', 'xzxb', 'ab'],
        ), [2, 1, 0])

    def test_case_1(self):
        self.assertListEqual(solution.matchingStrings(
            ['def', 'de', 'fgh'],
            ['de', 'lmn', 'fgh'],
        ), [1, 0, 1])

    def test_case_2(self):
        self.assertListEqual(solution.matchingStrings(
            [
                'abcde',
                'sdaklfj',
                'asdjf',
                'na',
                'basdn',
                'sdaklfj',
                'asdjf',
                'na',
                'asdjf',
                'na',
                'basdn',
                'sdaklfj',
                'asdjf',
            ],
            ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn'],
        ), [1, 3, 4, 3, 2])


if __name__ == '__main__':
    unittest.main()
