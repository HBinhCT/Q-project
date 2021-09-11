import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(
            solution.fightingPits(2,
                                  [
                                      [1, 1],
                                      [2, 1],
                                      [1, 1],
                                      [1, 2],
                                      [1, 2],
                                      [1, 2],
                                      [2, 2],
                                  ],
                                  [
                                      [2, 1, 2],
                                      [2, 2, 1],
                                      [1, 2, 1],
                                      [1, 2, 1],
                                      [2, 1, 2],
                                      [2, 2, 1],
                                  ]),
            [1, 2, 1, 1])


if __name__ == '__main__':
    unittest.main()
