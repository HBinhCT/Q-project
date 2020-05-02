import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4), 'ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ')


if __name__ == '__main__':
    unittest.main()
