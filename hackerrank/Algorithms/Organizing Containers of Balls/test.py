import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.organizingContainers([[1, 1], [1, 1]]), 'Possible')
        self.assertEqual(my_code.organizingContainers([[0, 2], [1, 1]]), 'Impossible')

    def test_case_1(self):
        self.assertEqual(my_code.organizingContainers([[1, 3, 1], [2, 1, 2], [3, 3, 3]]), 'Impossible')
        self.assertEqual(my_code.organizingContainers([[0, 2, 1], [1, 1, 1], [2, 0, 0]]), 'Possible')


if __name__ == '__main__':
    unittest.main()
