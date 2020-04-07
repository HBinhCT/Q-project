import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.timeConversion('07:05:45PM'), '19:05:45')


if __name__ == '__main__':
    unittest.main()
