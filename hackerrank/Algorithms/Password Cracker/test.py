import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.passwordCracker(
            [
                'because',
                'can',
                'do',
                'must',
                'we',
                'what',
            ],
            'wedowhatwemustbecausewecan'
        ), 'we do what we must because we can')
        self.assertEqual(solution.passwordCracker(
            [
                'hello',
                'planet',
            ],
            'helloworld'
        ), 'WRONG PASSWORD')
        self.assertEqual(solution.passwordCracker(
            [
                'ab',
                'abcd',
                'cd',
            ],
            'abcd'
        ), 'ab cd')

    def test_case_1(self):
        self.assertEqual(solution.passwordCracker(
            [
                'ozkxyhkcst',
                'xvglh',
                'hpdnb',
                'zfzahm',
            ],
            'zfzahm'
        ), 'zfzahm')
        self.assertEqual(solution.passwordCracker(
            [
                'gurwgrb',
                'maqz',
                'holpkhqx',
                'aowypvopu',
            ],
            'gurwgrb'
        ), 'gurwgrb')
        self.assertEqual(solution.passwordCracker(
            [
                'a',
                'aa',
                'aaa',
                'aaaa',
                'aaaaa',
                'aaaaaa',
                'aaaaaaa',
                'aaaaaaaa',
                'aaaaaaaaa',
                'aaaaaaaaaa',
            ],
            'aaaaaaaaaab'
        ), 'WRONG PASSWORD')


if __name__ == '__main__':
    unittest.main()
