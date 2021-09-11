import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(list(solution.name_format(
            [
                ['Mike', 'Thomson', '20', 'M'],
                ['Robert', 'Bustle', '32', 'M'],
                ['Andria', 'Bustle', '30', 'F'],
            ]
        )), ['Mr. Mike Thomson', 'Ms. Andria Bustle', 'Mr. Robert Bustle'])

    def test_case_1(self):
        self.assertEqual(list(solution.name_format(
            [
                ['Laura', 'Moser', '50', 'F'],
                ['Ted', 'Moser', '50', 'M'],
                ['Yena', 'Dixit', '50', 'F'],
                ['Diya', 'Mirza', '50', 'F'],
                ['Rex', 'Dsouza', '51', 'M'],
            ]
        )), ['Ms. Laura Moser', 'Mr. Ted Moser', 'Ms. Yena Dixit', 'Ms. Diya Mirza', 'Mr. Rex Dsouza'])


if __name__ == '__main__':
    unittest.main()
