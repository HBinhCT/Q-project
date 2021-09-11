import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.twoStrings('hello', 'world'), 'YES')
        self.assertEqual(solution.twoStrings('hi', 'world'), 'NO')

    def test_case_1(self):
        self.assertEqual(solution.twoStrings('wouldyoulikefries', 'abcabcabcabcabcabc'), 'NO')
        self.assertEqual(solution.twoStrings('hackerrankcommunity', 'cdecdecdecde'), 'YES')
        self.assertEqual(solution.twoStrings('jackandjill', 'wentupthehill'), 'YES')
        self.assertEqual(solution.twoStrings('writetoyourparents', 'fghmqzldbc'), 'NO')

    def test_case_2(self):
        self.assertEqual(solution.twoStrings('aardvark', 'apple'), 'YES')
        self.assertEqual(solution.twoStrings('beetroot', 'sandals'), 'NO')


if __name__ == '__main__':
    unittest.main()
