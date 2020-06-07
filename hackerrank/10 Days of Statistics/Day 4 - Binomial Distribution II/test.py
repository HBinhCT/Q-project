import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        defective, size = map(int, '12 10'.split())
        first = sum(solution.binomial(size, i, defective / 100) for i in range(3))
        second = sum(solution.binomial(size, i, defective / 100) for i in range(2, size + 1))
        self.assertEqual(round(first, 3), 0.891)
        self.assertEqual(round(second, 3), 0.342)


if __name__ == '__main__':
    unittest.main()
