import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.mutate_string('abracadabra', 5, 'k'), 'abrackdabra')


if __name__ == '__main__':
    unittest.main()
