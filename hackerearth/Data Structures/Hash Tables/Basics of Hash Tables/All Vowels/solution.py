n = int(input())
s = input().strip()
print('YES' if set('aeiou') <= set(s) else 'NO')
