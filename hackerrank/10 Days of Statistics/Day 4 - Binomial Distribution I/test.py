import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        boys, girls = map(float, '1.09 1'.split())
        odds = boys / girls
        result = sum(solution.binomial(6, i, odds / (1 + odds)) for i in range(3, 7))
        self.assertEqual(round(result, 3), 0.696)


if __name__ == '__main__':
    unittest.main()
