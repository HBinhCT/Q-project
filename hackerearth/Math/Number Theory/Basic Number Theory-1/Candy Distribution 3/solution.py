from sys import stdin

mod = 1000000007
toffees = []
t = int(stdin.readline())
for _ in range(t):
    toffees.append(int(stdin.readline()))
size = max(toffees) + 2
comb_x2 = [1, 2]
comb_x3 = [1, 3]
for i in range(2, size):
    comb_x2.append(comb_x2[i - 1] * 2 % mod)
    comb_x3.append(comb_x3[i - 1] * 3 % mod)
for n in toffees:
    print(0 if n == 1 else (comb_x2[n] * comb_x2[n] % mod - 2 * comb_x3[n] % mod + comb_x2[n]) % mod)
