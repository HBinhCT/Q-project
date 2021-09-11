import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(list(solution.design_mat(7, 21)), [
            '---------.|.---------',
            '------.|..|..|.------',
            '---.|..|..|..|..|.---',
            '-------WELCOME-------',
            '---.|..|..|..|..|.---',
            '------.|..|..|.------',
            '---------.|.---------',
        ])


if __name__ == '__main__':
    unittest.main()
