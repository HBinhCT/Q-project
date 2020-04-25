import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.circularArrayRotation([1, 2, 3], 2, [0, 1, 2]), [2, 3, 1])


if __name__ == '__main__':
    unittest.main()
