import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.makingAnagrams('cde', 'abc'), 4)

    def test_case_1(self):
        self.assertEqual(
            solution.makingAnagrams('absdjkvuahdakejfnfauhdsaavasdlkj', 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'),
            19
        )


if __name__ == '__main__':
    unittest.main()
