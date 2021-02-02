#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#

def passwordCracker(passwords, loginAttempt):
    # Write your code here
    from collections import defaultdict
    sys.setrecursionlimit(2000)

    def _password_cracker(keys, word, cur, cached):
        if word == '':
            return cur
        if word in cached:
            return ''
        if word[0] in d:
            for i in d[word[0]]:
                if word[:len(i)] == i:
                    cur_ans = _password_cracker(keys, word[len(i):], cur + i + ' ', cached)
                    if cur_ans != '':
                        return cur_ans
        cached.add(word)
        return ''

    password_set = set(''.join(passwords))
    word_set = set(loginAttempt)
    if not password_set >= word_set:
        return 'WRONG PASSWORD'
    list_set = set(passwords)
    if word_set <= list_set:
        return ' '.join(list(loginAttempt))
    d = defaultdict(list)
    mem_cache = set()
    for password in passwords:
        d[password[0]].append(password)
    ans = _password_cracker(d, loginAttempt, '', mem_cache)
    return 'WRONG PASSWORD' if ans == '' else ans.rstrip()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        result = passwordCracker(passwords, loginAttempt)

        fptr.write(result + '\n')

    fptr.close()
