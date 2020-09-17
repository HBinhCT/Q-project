import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.fibonacciModified(0, 1, 5), 5)

    def test_case_1(self):
        self.assertEqual(solution.fibonacciModified(0, 1, 10), 84266613096281243382112)


if __name__ == '__main__':
    unittest.main()
