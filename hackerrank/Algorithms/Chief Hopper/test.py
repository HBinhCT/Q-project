import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.chiefHopper([3, 4, 3, 2, 4]), 4)

    def test_case_1(self):
        self.assertEqual(solution.chiefHopper([4, 4, 4]), 4)

    def test_case_2(self):
        self.assertEqual(solution.chiefHopper([1, 6, 4]), 3)


if __name__ == '__main__':
    unittest.main()
