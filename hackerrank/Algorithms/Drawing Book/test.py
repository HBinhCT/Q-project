import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.pageCount(6, 2), 1)

    def test_case_1(self):
        self.assertEqual(my_code.pageCount(5, 4), 0)


if __name__ == '__main__':
    unittest.main()
