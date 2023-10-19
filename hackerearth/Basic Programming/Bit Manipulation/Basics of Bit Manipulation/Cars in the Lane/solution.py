def f(n, ar):
    # write your code here
    for a in ar:
        print(2 ** int(bin(a)[2:].count("1")))


ar = []
t = int(input())
for _ in range(t):
    n = int(input())
    ar.append(n)
f(t, ar)
