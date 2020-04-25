import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.twoStrings('hello', 'world'), 'YES')
        self.assertEqual(my_code.twoStrings('hi', 'world'), 'NO')

    def test_case_1(self):
        self.assertEqual(my_code.twoStrings('wouldyoulikefries', 'abcabcabcabcabcabc'), 'NO')
        self.assertEqual(my_code.twoStrings('hackerrankcommunity', 'cdecdecdecde'), 'YES')
        self.assertEqual(my_code.twoStrings('jackandjill', 'wentupthehill'), 'YES')
        self.assertEqual(my_code.twoStrings('writetoyourparents', 'fghmqzldbc'), 'NO')

    def test_case_2(self):
        self.assertEqual(my_code.twoStrings('aardvark', 'apple'), 'YES')
        self.assertEqual(my_code.twoStrings('beetroot', 'sandals'), 'NO')


if __name__ == '__main__':
    unittest.main()
