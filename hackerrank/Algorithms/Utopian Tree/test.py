import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.utopianTree(0), 1)
        self.assertEqual(my_code.utopianTree(1), 2)

    def test_case_1(self):
        self.assertEqual(my_code.utopianTree(4), 7)
        self.assertEqual(my_code.utopianTree(3), 6)


if __name__ == '__main__':
    unittest.main()
