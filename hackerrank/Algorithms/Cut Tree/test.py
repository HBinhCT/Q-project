import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.cuttree(3, 1, [[2, 1], [2, 3]]), 6)


if __name__ == '__main__':
    unittest.main()
