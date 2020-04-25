import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.makingAnagrams('cde', 'abc'), 4)

    def test_case_1(self):
        self.assertEqual(
            my_code.makingAnagrams('absdjkvuahdakejfnfauhdsaavasdlkj', 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'),
            19
        )


if __name__ == '__main__':
    unittest.main()
