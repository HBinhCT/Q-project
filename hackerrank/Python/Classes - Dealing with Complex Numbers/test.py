import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        c = solution.Complex(2, 1)
        d = solution.Complex(5, 6)
        self.assertEqual(str(c + d), '7.00+7.00i')
        self.assertEqual(str(c - d), '-3.00-5.00i')
        self.assertEqual(str(c * d), '4.00+17.00i')
        self.assertEqual(str(c / d), '0.26-0.11i')
        self.assertEqual(str(c.mod()), '2.24+0.00i')
        self.assertEqual(str(d.mod()), '7.81+0.00i')

    def test_case_1(self):
        c = solution.Complex(5.9, 6)
        d = solution.Complex(9, 10)
        self.assertEqual(str(c + d), '14.90+16.00i')
        self.assertEqual(str(c - d), '-3.10-4.00i')
        self.assertEqual(str(c * d), '-6.90+113.00i')
        self.assertEqual(str(c / d), '0.62-0.03i')
        self.assertEqual(str(c.mod()), '8.41+0.00i')
        self.assertEqual(str(d.mod()), '13.45+0.00i')


if __name__ == '__main__':
    unittest.main()
