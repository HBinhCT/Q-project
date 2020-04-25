import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.libraryFine(9, 6, 2015, 6, 6, 2015), 45)


if __name__ == '__main__':
    unittest.main()
