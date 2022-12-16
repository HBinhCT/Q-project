from collections import Counter


def is_prime(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(x ** .5) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


t = int(input())
for _ in range(t):
    string = input().strip()
    counter = Counter(string)
    if is_prime(len(counter)):
        print('YES' if all(is_prime(i) for i in counter.values()) else 'NO')
    else:
        print('NO')
