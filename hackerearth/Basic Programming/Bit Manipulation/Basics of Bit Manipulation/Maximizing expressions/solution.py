n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))
x = int(pow(2, 30) - 1)
s = 0
for i in range(n):
    d = (a[i] ^ b[i] ^ x) & c[i]
    if not d:
        d = (c[i] ^ c[i] - 1) + 1 >> 1
    s += d ^ b[i] ^ a[i]
print(s)
