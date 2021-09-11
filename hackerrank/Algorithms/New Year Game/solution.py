#!/bin/python3


def new_year_game(arr):
    new_arr = [x % 3 for x in arr]
    n_1 = new_arr.count(1)
    n_2 = new_arr.count(2)
    return 'Balsa' if (n_1 & 1) | (n_2 & 1) else 'Koca'


if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        # Write Your Code Here
        res = new_year_game(a)
        print(res)
