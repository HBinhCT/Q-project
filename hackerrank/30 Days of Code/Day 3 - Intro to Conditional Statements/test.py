import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.main(3), 'Weird')

    def test_case_1(self):
        self.assertEqual(solution.main(24), 'Not Weird')


if __name__ == '__main__':
    unittest.main()
