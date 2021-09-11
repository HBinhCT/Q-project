import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.libraryFine(9, 6, 2015, 6, 6, 2015), 45)


if __name__ == '__main__':
    unittest.main()
