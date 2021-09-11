import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.alternate('beabeefeab'), 5)

    def test_case_1(self):
        self.assertEqual(solution.alternate('asdcbsdcagfsdbgdfanfghbsfdab'), 8)

    def test_case_2(self):
        self.assertEqual(solution.alternate('asvkugfiugsalddlasguifgukvsa'), 0)


if __name__ == '__main__':
    unittest.main()
