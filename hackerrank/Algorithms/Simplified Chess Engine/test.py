import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.simplifiedChessEngine(
            [['N', 'B', '2'], ['Q', 'B', '1']],
            [['Q', 'A', '4']],
            1,
        ), 'YES')


if __name__ == '__main__':
    unittest.main()
