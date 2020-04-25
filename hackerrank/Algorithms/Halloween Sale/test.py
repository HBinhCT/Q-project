import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.howManyGames(20, 3, 6, 80), 6)

    def test_case_1(self):
        self.assertEqual(my_code.howManyGames(20, 3, 6, 85), 7)


if __name__ == '__main__':
    unittest.main()
