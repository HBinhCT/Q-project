from collections import Counter


def Minimum_Operations(n, s):
    # Write your code here
    counter = Counter(s)
    count = 0
    for i in counter:
        count += counter[i] // 2
    return count


T = int(input())
for _ in range(T):
    n = int(input())
    s = input()

    out_ = Minimum_Operations(n, s)
    print(out_)
