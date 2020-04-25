import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.acmTeam(['10101', '11100', '11010', '00101']), (5, 2))

    def test_case_1(self):
        self.assertEqual(my_code.acmTeam(['11101', '10101', '11001', '10111', '10000', '01110']), (5, 6))


if __name__ == '__main__':
    unittest.main()
