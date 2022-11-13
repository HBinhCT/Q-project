n = int(input())
c = 0
x = n % 2
for i in range(2 - x, int(n ** .5) + 1, 2):
    if n % i == 0 and n / i % 2 == x:
        c += 1
print(c)
