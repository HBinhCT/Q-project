import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.andProduct(12, 15), 12)
        self.assertEqual(solution.andProduct(2, 3), 2)
        self.assertEqual(solution.andProduct(8, 13), 8)

    def test_case_1(self):
        self.assertEqual(solution.andProduct(17, 23), 16)
        self.assertEqual(solution.andProduct(11, 15), 8)


if __name__ == '__main__':
    unittest.main()
