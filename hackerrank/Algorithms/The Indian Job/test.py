import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.indianJob(4, [2, 4, 2]), 'YES')
        self.assertEqual(solution.indianJob(2, [2, 4, 2]), 'NO')


if __name__ == '__main__':
    unittest.main()
