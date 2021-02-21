#!/bin/python3

import os
import sys


#
# Complete the permutationGame function below.
#
def permutationGame(arr):
    #
    # Write your code here.
    #
    from functools import lru_cache

    def renumber(array):
        sorted_array = sorted(array)
        return [sorted_array.index(x) + 1 for x in array]

    @lru_cache(maxsize=None)
    def _permutation_game(nums):
        if nums == tuple(sorted(nums)):
            return 0
        else:
            ans = set()
            for x in nums:
                temp = list(nums)
                temp.remove(x)
                temp = renumber(temp)
                ans.add(_permutation_game(tuple(temp)))
            res = 0
            while res in ans:
                res += 1
            return res

    return 'Alice' if _permutation_game(tuple(arr)) else 'Bob'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = permutationGame(arr)

        fptr.write(result + '\n')

    fptr.close()
