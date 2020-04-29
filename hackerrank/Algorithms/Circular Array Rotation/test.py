import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.circularArrayRotation([1, 2, 3], 2, [0, 1, 2]), [2, 3, 1])


if __name__ == '__main__':
    unittest.main()
