import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.deforestation(
            5,
            [
                [1, 2],
                [3, 1],
                [3, 4],
                [5, 4]
            ]
        ), 'Alice')


if __name__ == '__main__':
    unittest.main()
