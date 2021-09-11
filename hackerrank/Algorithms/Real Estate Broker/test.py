import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.realEstateBroker([[5, 110], [9, 500], [20, 400]], [[10, 100], [2, 200], [30, 300]]),
                         2)


if __name__ == '__main__':
    unittest.main()
