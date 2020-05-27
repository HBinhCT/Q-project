import re

for _ in range(int(input())):
    print('YES' if re.match(r'^[789]\d{9}$', input()) else 'NO')
