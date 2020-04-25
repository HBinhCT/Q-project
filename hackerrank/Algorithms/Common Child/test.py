import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.commonChild('HARRY', 'SALLY'), 2)

    def test_case_1(self):
        self.assertEqual(my_code.commonChild('AA', 'BB'), 0)

    def test_case_2(self):
        self.assertEqual(my_code.commonChild('SHINCHAN', 'NOHARAAA'), 3)


if __name__ == '__main__':
    unittest.main()
