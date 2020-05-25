s = input()
assert 0 < len(s) < 1000
output = sorted(s, key=lambda x: (x.isdigit() and int(x) % 2 == 0, x.isdigit(), x.isupper(), x.islower(), x))
print(*output, sep='')
