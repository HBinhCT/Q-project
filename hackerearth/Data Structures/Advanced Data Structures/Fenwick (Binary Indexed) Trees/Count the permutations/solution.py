from collections import Counter

mod = 1000000007


def get_total(array, index):
    total = 0
    while index > 0:
        total += array[index]
        index -= index & -index
    return total


def update(array, length, index, value):
    while index < length:
        array[index] += value
        index += index & -index


n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
facts = [1] * (n + 1)
x = 1
for i in range(2, n + 1):
    x = x * i % mod
    facts[i] = x
freq = Counter(a)
size = max(*a, *b)
tree = [0] * (size + 1)
comb = facts[n]
ans = 0
for x in freq.keys():
    comb = comb * pow(facts[freq[x]], mod - 2, mod) % mod
    update(tree, size, x, freq[x])
for i in range(n):
    comb = comb * pow(n - i, mod - 2, mod) % mod
    ans = (ans + comb * get_total(tree, b[i] - 1)) % mod
    comb = comb * freq[b[i]] % mod
    freq[b[i]] -= 1
    if freq[b[i]] < 0:
        break
    update(tree, size, b[i], -1)
print(ans)
