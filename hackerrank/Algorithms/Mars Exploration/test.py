import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.marsExploration('SOSSPSSQSSOR'), 3)

    def test_case_1(self):
        self.assertEqual(my_code.marsExploration('SOSSOT'), 1)

    def test_case_2(self):
        self.assertEqual(my_code.marsExploration('SOSSOSSOS'), 0)


if __name__ == '__main__':
    unittest.main()
