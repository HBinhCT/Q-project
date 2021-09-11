import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.hexagonalGrid('010000', '000010'), 'YES')
        self.assertEqual(solution.hexagonalGrid('00', '00'), 'YES')
        self.assertEqual(solution.hexagonalGrid('00', '10'), 'NO')
        self.assertEqual(solution.hexagonalGrid('00', '01'), 'NO')
        self.assertEqual(solution.hexagonalGrid('00', '11'), 'YES')
        self.assertEqual(solution.hexagonalGrid('10', '00'), 'NO')


if __name__ == '__main__':
    unittest.main()
