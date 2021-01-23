import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.winningLotteryTicket([
            '129300455',
            '5559948277',
            '012334556',
            '56789',
            '123456879',
        ]), 5)


if __name__ == '__main__':
    unittest.main()
