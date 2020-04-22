import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.queensAttack(4, 0, 4, 4, []), 9)

    def test_case_1(self):
        self.assertEqual(my_code.queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]), 10)

    def test_case_2(self):
        self.assertEqual(my_code.queensAttack(1, 0, 1, 1, []), 0)


if __name__ == '__main__':
    unittest.main()
