import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.encryption('haveaniceday'), 'hae and via ecy')

    def test_case_1(self):
        self.assertEqual(my_code.encryption('feedthedog'), 'fto ehg ee dd')

    def test_case_2(self):
        self.assertEqual(my_code.encryption('chillout'), 'clu hlt io')


if __name__ == '__main__':
    unittest.main()
