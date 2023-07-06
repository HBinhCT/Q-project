n, k = map(int, input().strip().split())
digits = list(str(n))
i = 0
while i < n and k > 0:
    if '9' != digits[i]:
        digits[i] = '9'
        k -= 1
    i += 1
print(''.join(digits))
