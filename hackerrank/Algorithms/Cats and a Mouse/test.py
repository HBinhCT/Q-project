import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.catAndMouse(1, 2, 3), 'Cat B')
        self.assertEqual(my_code.catAndMouse(1, 3, 2), 'Mouse C')


if __name__ == '__main__':
    unittest.main()
