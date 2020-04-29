import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.introTutorial(4, [1, 4, 5, 7, 9, 12]), 1)


if __name__ == '__main__':
    unittest.main()
