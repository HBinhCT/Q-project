import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.closestNumbers(
            [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
        ), [-20, 30])

    def test_case_1(self):
        self.assertEqual(my_code.closestNumbers([-5, 15, 25, 71, 63]), [63, 71])


if __name__ == '__main__':
    unittest.main()
