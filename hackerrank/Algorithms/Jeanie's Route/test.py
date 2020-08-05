import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(
            solution.jeanisRoute(
                5,
                3,
                [
                    [1, 2, 1],
                    [2, 3, 2],
                    [2, 4, 2],
                    [3, 5, 3],
                ],
                [1, 3, 4]
            ), 6)


if __name__ == '__main__':
    unittest.main()
