import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.hurdleRace(4, [1, 6, 3, 5, 2]), 2)

    def test_case_1(self):
        self.assertEqual(my_code.hurdleRace(7, [2, 5, 4, 5, 2]), 0)


if __name__ == '__main__':
    unittest.main()
