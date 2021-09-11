import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.encryption('haveaniceday'), 'hae and via ecy')

    def test_case_1(self):
        self.assertEqual(solution.encryption('feedthedog'), 'fto ehg ee dd')

    def test_case_2(self):
        self.assertEqual(solution.encryption('chillout'), 'clu hlt io')


if __name__ == '__main__':
    unittest.main()
