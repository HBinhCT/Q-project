import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.simpleArraySum([1, 2, 3, 4, 10, 11]), 31)


if __name__ == '__main__':
    unittest.main()
