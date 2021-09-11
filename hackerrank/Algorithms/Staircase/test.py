import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.staircase(6)
        self.assertEqual(text_trap.getvalue(), "     #\n    ##\n   ###\n  ####\n #####\n######\n")
        #      #
        #     ##
        #    ###
        #   ####
        #  #####
        # ######


if __name__ == '__main__':
    unittest.main()
