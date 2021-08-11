import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.truckTour([
            [1, 5],
            [10, 3],
            [3, 4],
        ]), 1)


if __name__ == '__main__':
    unittest.main()
