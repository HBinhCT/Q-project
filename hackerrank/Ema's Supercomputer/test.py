import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.twoPluses(['GGGGGG', 'GBBBGB', 'GGGGGG', 'GGBBGB', 'GGGGGG']), 5)

    def test_case_1(self):
        self.assertEqual(my_code.twoPluses(['BGBBGB', 'GGGGGG', 'BGBBGB', 'GGGGGG', 'BGBBGB', 'BGBBGB']), 25)


if __name__ == '__main__':
    unittest.main()
