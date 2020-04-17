import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.permutationEquation([2, 3, 1]), [2, 3, 1])

    def test_case_1(self):
        self.assertEqual(my_code.permutationEquation([4, 3, 5, 1, 2]), [1, 3, 5, 4, 2])


if __name__ == '__main__':
    unittest.main()
