#!/bin/python3


# Complete the separateNumbers function below.
def separateNumbers(s):
    n = len(s)
    i = 1
    while i <= n // 2:
        j = i
        a = int(s[:i])
        flag = 1
        while j < n:
            b = str(a + 1)
            if s[j:j + len(b)] != b:
                flag = 0
                break
            j += len(b)
            a = int(b)
        if flag:
            print('YES ' + s[:i])
            return
        i += 1
    print('NO')
    return


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
