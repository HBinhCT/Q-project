import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        input_stdin = ('1234', '91011', '99100', '101103', '010203', '13', '1')
        output_stdout = ('YES 1', 'YES 9', 'YES 99', 'NO', 'NO', 'NO', 'NO')
        for i in range(len(input_stdin)):
            text_trap = io.StringIO()
            with redirect_stdout(text_trap):
                solution.separateNumbers(input_stdin[i])
            self.assertEqual(text_trap.getvalue(), output_stdout[i] + "\n")

    def test_case_1(self):
        input_stdin = ('99910001001', '7891011', '9899100', '999100010001')
        output_stdout = ('YES 999', 'YES 7', 'YES 98', 'NO')
        for i in range(len(input_stdin)):
            text_trap = io.StringIO()
            with redirect_stdout(text_trap):
                solution.separateNumbers(input_stdin[i])
            self.assertEqual(text_trap.getvalue(), output_stdout[i] + "\n")


if __name__ == '__main__':
    unittest.main()
