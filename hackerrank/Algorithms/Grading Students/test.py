import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.gradingStudents([73, 67, 38, 33]), [75, 67, 40, 33])


if __name__ == '__main__':
    unittest.main()
