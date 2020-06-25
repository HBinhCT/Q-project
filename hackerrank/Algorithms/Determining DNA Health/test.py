import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        genes_map, subs, largest = solution.prepare_data(['a', 'b', 'c', 'aa', 'd', 'b'], [1, 2, 3, 4, 5, 6])
        healths = [
            solution.get_health('caaab', 1, 5, largest, genes_map, subs),
            solution.get_health('xyz', 0, 4, largest, genes_map, subs),
            solution.get_health('bcdybc', 2, 4, largest, genes_map, subs),
        ]
        self.assertEqual(min(healths), 0)
        self.assertEqual(max(healths), 19)


if __name__ == '__main__':
    unittest.main()
