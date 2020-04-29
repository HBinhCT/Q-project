import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.catAndMouse(1, 2, 3), 'Cat B')
        self.assertEqual(solution.catAndMouse(1, 3, 2), 'Mouse C')


if __name__ == '__main__':
    unittest.main()
