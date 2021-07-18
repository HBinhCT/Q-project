import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertListEqual(solution.getMax([
            '1 97',
            '2',
            '1 20',
            '2',
            '1 26',
            '1 20',
            '2',
            '3',
            '1 91',
            '3',
        ]), [26, 91])


if __name__ == '__main__':
    unittest.main()
