import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.stringTransmission(0, '00000'), 0)
        self.assertEqual(solution.stringTransmission(1, '001'), 3)
        self.assertEqual(solution.stringTransmission(3, '101'), 6)


if __name__ == '__main__':
    unittest.main()
