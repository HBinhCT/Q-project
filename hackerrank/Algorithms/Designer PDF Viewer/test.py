import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.designerPdfViewer(
            [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            'abc'
        ), 9)

    def test_case_1(self):
        self.assertEqual(my_code.designerPdfViewer(
            [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7],
            'zaba'
        ), 28)


if __name__ == '__main__':
    unittest.main()
