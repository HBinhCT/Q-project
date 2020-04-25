import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.findMedian([0, 1, 2, 4, 6, 5, 3]), 3)


if __name__ == '__main__':
    unittest.main()
