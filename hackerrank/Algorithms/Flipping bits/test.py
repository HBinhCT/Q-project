import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.flippingBits(2147483647), 2147483648)
        self.assertEqual(solution.flippingBits(1), 4294967294)
        self.assertEqual(solution.flippingBits(0), 4294967295)

    def test_case_1(self):
        self.assertEqual(solution.flippingBits(4), 4294967291)
        self.assertEqual(solution.flippingBits(123456), 4294843839)

    def test_case_2(self):
        self.assertEqual(solution.flippingBits(0), 4294967295)
        self.assertEqual(solution.flippingBits(802743475), 3492223820)
        self.assertEqual(solution.flippingBits(35601423), 4259365872)


if __name__ == '__main__':
    unittest.main()
