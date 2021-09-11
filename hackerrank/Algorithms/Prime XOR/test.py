import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.primeXor([3511, 3511, 3511, 3511]), 2)


if __name__ == '__main__':
    unittest.main()
