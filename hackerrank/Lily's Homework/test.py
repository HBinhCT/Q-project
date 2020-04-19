import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.lilysHomework([2, 5, 3, 1]), 2)

    def test_case_1(self):
        self.assertEqual(my_code.lilysHomework([3, 4, 2, 5, 1]), 2)


if __name__ == '__main__':
    unittest.main()
