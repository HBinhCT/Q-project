import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(sorted(
            solution.filter_mail(['lara@hackerrank.com', 'brian-23@hackerrank.com', 'britts_54@hackerrank.com'])),
                         ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com'])

    def test_case_1(self):
        self.assertEqual(sorted(solution.filter_mail(['harsh@gmail', 'iota_98@hackerrank.com'])),
                         ['iota_98@hackerrank.com'])


if __name__ == '__main__':
    unittest.main()
