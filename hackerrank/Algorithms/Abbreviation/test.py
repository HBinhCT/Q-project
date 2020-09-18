import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.abbreviation('daBcd', 'ABC'), 'YES')

    def test_case_1(self):
        self.assertEqual(solution.abbreviation('Pi', 'P'), 'YES')
        self.assertEqual(solution.abbreviation('AfPZN', 'APZNC'), 'NO')
        self.assertEqual(solution.abbreviation('LDJAN', 'LJJM'), 'NO')
        self.assertEqual(solution.abbreviation('UMKFW', 'UMKFW'), 'YES')
        self.assertEqual(solution.abbreviation('KXzQ', 'K'), 'NO')
        self.assertEqual(solution.abbreviation('LIT', 'LIT'), 'YES')
        self.assertEqual(solution.abbreviation('QYCH', 'QYCH'), 'YES')
        self.assertEqual(solution.abbreviation('DFIQG', 'DFIQG'), 'YES')
        self.assertEqual(solution.abbreviation('sYOCa', 'YOCN'), 'NO')
        self.assertEqual(solution.abbreviation('JHMWY', 'HUVPW'), 'NO')

    def test_case_bonus(self):
        self.assertEqual(solution.abbreviation('AbCdE', 'AFE'), 'NO')
        self.assertEqual(solution.abbreviation('beFgH', 'EFG'), 'NO')
        self.assertEqual(solution.abbreviation('beFgH', 'EFH'), 'YES')


if __name__ == '__main__':
    unittest.main()
