import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.sansaXor([1, 2, 3]), 2)
        self.assertEqual(solution.sansaXor([4, 5, 7, 5]), 0)

    def test_case_1(self):
        self.assertEqual(solution.sansaXor([98, 74, 12]), 110)
        self.assertEqual(solution.sansaXor([50, 13, 2]), 48)


if __name__ == '__main__':
    unittest.main()
