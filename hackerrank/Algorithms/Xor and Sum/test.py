import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.xorAndSum('10', '1010'), 489429555)


if __name__ == '__main__':
    unittest.main()
