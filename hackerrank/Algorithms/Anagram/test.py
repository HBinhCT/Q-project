import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.anagram('aaabbb'), 3)
        self.assertEqual(my_code.anagram('ab'), 1)
        self.assertEqual(my_code.anagram('abc'), -1)
        self.assertEqual(my_code.anagram('mnop'), 2)
        self.assertEqual(my_code.anagram('xyyx'), 0)
        self.assertEqual(my_code.anagram('xaxbbbxx'), 1)

    def test_case_1(self):
        self.assertEqual(my_code.anagram('asdfjoieufoa'), 3)
        self.assertEqual(my_code.anagram('fdhlvosfpafhalll'), 5)
        self.assertEqual(my_code.anagram('mvdalvkiopaufl'), 5)


if __name__ == '__main__':
    unittest.main()
