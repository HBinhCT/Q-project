import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.anagram('aaabbb'), 3)
        self.assertEqual(solution.anagram('ab'), 1)
        self.assertEqual(solution.anagram('abc'), -1)
        self.assertEqual(solution.anagram('mnop'), 2)
        self.assertEqual(solution.anagram('xyyx'), 0)
        self.assertEqual(solution.anagram('xaxbbbxx'), 1)

    def test_case_1(self):
        self.assertEqual(solution.anagram('asdfjoieufoa'), 3)
        self.assertEqual(solution.anagram('fdhlvosfpafhalll'), 5)
        self.assertEqual(solution.anagram('mvdalvkiopaufl'), 5)


if __name__ == '__main__':
    unittest.main()
