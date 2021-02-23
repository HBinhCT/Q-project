import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.new_year_game([7, 6, 18]), 'Balsa')
        self.assertEqual(solution.new_year_game([3]), 'Koca')


if __name__ == '__main__':
    unittest.main()
