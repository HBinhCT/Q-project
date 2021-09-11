import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.timeConversion('07:05:45PM'), '19:05:45')


if __name__ == '__main__':
    unittest.main()
