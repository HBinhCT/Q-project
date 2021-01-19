import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.theGreatXor(2), 1)
        self.assertEqual(solution.theGreatXor(10), 5)

    def test_case_1(self):
        self.assertEqual(solution.theGreatXor(5), 2)
        self.assertEqual(solution.theGreatXor(100), 27)


if __name__ == '__main__':
    unittest.main()
