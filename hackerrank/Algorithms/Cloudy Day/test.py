import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.maximumPeople(
            [10, 100],
            [5, 100],
            [4],
            [1],
        ), 110)


if __name__ == '__main__':
    unittest.main()
