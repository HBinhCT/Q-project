import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.viralAdvertising(3), 9)

    def test_case_1(self):
        self.assertEqual(solution.viralAdvertising(4), 15)


if __name__ == '__main__':
    unittest.main()
