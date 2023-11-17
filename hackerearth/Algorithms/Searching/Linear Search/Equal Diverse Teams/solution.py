from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = input().strip().split()
    counter = Counter(a)
    m = len(counter)
    h = k * 2
    if m > h:
        print("NO")
    elif m == h:
        print("YES")
    else:
        for i in sorted(counter.values(), reverse=True):
            if i > 1:
                m += 1
            else:
                print("NO")
                break
            if m == h:
                print("YES")
                break
        else:
            print("NO")
