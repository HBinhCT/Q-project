import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.designerPdfViewer(
            [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            'abc'
        ), 9)

    def test_case_1(self):
        self.assertEqual(solution.designerPdfViewer(
            [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7],
            'zaba'
        ), 28)


if __name__ == '__main__':
    unittest.main()
