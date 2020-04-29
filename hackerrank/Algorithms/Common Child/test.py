import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.commonChild('HARRY', 'SALLY'), 2)

    def test_case_1(self):
        self.assertEqual(solution.commonChild('AA', 'BB'), 0)

    def test_case_2(self):
        self.assertEqual(solution.commonChild('SHINCHAN', 'NOHARAAA'), 3)


if __name__ == '__main__':
    unittest.main()
