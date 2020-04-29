import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.biggerIsGreater('ab'), 'ba')
        self.assertEqual(solution.biggerIsGreater('bb'), 'no answer')
        self.assertEqual(solution.biggerIsGreater('hefg'), 'hegf')
        self.assertEqual(solution.biggerIsGreater('dhck'), 'dhkc')
        self.assertEqual(solution.biggerIsGreater('dkhc'), 'hcdk')

    def test_case_1(self):
        self.assertEqual(solution.biggerIsGreater('lmno'), 'lmon')
        self.assertEqual(solution.biggerIsGreater('dcba'), 'no answer')
        self.assertEqual(solution.biggerIsGreater('dcbb'), 'no answer')
        self.assertEqual(solution.biggerIsGreater('abdc'), 'acbd')
        self.assertEqual(solution.biggerIsGreater('abcd'), 'abdc')
        self.assertEqual(solution.biggerIsGreater('fedcbabcd'), 'fedcbabdc')


if __name__ == '__main__':
    unittest.main()
