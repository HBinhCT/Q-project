import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.cavityMap(['1112', '1912', '1892', '1234']), ['1112', '1X12', '18X2', '1234'])

    def test_case_1(self):
        self.assertEqual(solution.cavityMap(['12', '12']), ['12', '12'])


if __name__ == '__main__':
    unittest.main()
