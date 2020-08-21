import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.gridChallenge([
            'eabcd',
            'fghij',
            'olkmn',
            'trpqs',
            'xywuv',
        ]), 'YES')

    def test_case_1(self):
        self.assertEqual(solution.gridChallenge([
            'abc',
            'lmp',
            'qrt',
        ]), 'YES')
        self.assertEqual(solution.gridChallenge([
            'mpxz',
            'abcd',
            'wlmf',
        ]), 'NO')
        self.assertEqual(solution.gridChallenge([
            'abc',
            'hjk',
            'mpq',
            'rtv',
        ]), 'YES')


if __name__ == '__main__':
    unittest.main()
