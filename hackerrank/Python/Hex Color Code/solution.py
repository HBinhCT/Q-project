import re

for _ in range(0, int(input())):
    matches = re.findall(r'(#(?:[\da-f]{3}){1,2})(?!\w)(?=.*;)', input(), re.IGNORECASE)
    if matches:
        print(*matches, sep='\n')
