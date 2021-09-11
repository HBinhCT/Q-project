import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.gradingStudents([73, 67, 38, 33]), [75, 67, 40, 33])


if __name__ == '__main__':
    unittest.main()
