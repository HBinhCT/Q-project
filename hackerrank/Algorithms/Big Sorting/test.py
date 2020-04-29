import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(
            solution.bigSorting(['31415926535897932384626433832795', '1', '3', '10', '3', '5']),
            ['1', '3', '3', '5', '10', '31415926535897932384626433832795']
        )

    def test_case_1(self):
        self.assertEqual(
            solution.bigSorting(
                ['1', '2', '100', '12303479849857341718340192371', '3084193741082937', '3084193741082938', '111', '200']
            ),
            ['1', '2', '100', '111', '200', '3084193741082937', '3084193741082938', '12303479849857341718340192371']
        )


if __name__ == '__main__':
    unittest.main()
