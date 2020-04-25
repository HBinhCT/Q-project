import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.biggerIsGreater('ab'), 'ba')
        self.assertEqual(my_code.biggerIsGreater('bb'), 'no answer')
        self.assertEqual(my_code.biggerIsGreater('hefg'), 'hegf')
        self.assertEqual(my_code.biggerIsGreater('dhck'), 'dhkc')
        self.assertEqual(my_code.biggerIsGreater('dkhc'), 'hcdk')

    def test_case_1(self):
        self.assertEqual(my_code.biggerIsGreater('lmno'), 'lmon')
        self.assertEqual(my_code.biggerIsGreater('dcba'), 'no answer')
        self.assertEqual(my_code.biggerIsGreater('dcbb'), 'no answer')
        self.assertEqual(my_code.biggerIsGreater('abdc'), 'acbd')
        self.assertEqual(my_code.biggerIsGreater('abcd'), 'abdc')
        self.assertEqual(my_code.biggerIsGreater('fedcbabcd'), 'fedcbabdc')


if __name__ == '__main__':
    unittest.main()
