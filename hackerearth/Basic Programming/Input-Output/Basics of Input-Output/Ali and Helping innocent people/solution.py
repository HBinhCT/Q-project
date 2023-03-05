tag = input().strip()
a, b = map(int, tag[0:2])
c = tag[2]
d, e, f = map(int, tag[3:6])
g = tag[6]
h, i = map(int, tag[7:])
if c in ('A', 'E', 'I', 'O', 'U', 'Y'):
    print('invalid')
elif (a + b) % 2 == (d + e) % 2 == (e + f) % 2 == (h + i) % 2 == 0:
    print('valid')
else:
    print('invalid')
