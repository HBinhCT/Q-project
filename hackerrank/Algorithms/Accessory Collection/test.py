import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.acessoryCollection(6, 5, 3, 2), '24')
        self.assertEqual(solution.acessoryCollection(2, 1, 2, 2), 'SAD')


if __name__ == '__main__':
    unittest.main()
