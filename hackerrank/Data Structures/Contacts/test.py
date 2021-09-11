import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertListEqual(list(solution.contacts([
            ['add', 'hack'],
            ['add', 'hackerrank'],
            ['find', 'hac'],
            ['find', 'hak'],
        ])), [2, 0])


if __name__ == '__main__':
    unittest.main()
