def parse_int(s):
    return int(s.replace('9', '8'), 9)


def to_string(n):
    digits = '012345679'
    s = ''
    while n:
        s = digits[n % 9] + s
        n = n // 9
    return s or '0'


t = int(input())
for _ in range(t):
    calc = input().strip()
    if '+' in calc:
        a, b = map(parse_int, calc.split('+'))
        print(to_string(a + b))
    elif '-' in calc:
        a, b = map(parse_int, calc.split('-'))
        print(to_string(a - b))
    elif '*' in calc:
        a, b = map(parse_int, calc.split('*'))
        print(to_string(a * b))
    elif '/' in calc:
        a, b = map(parse_int, calc.split('/'))
        print(to_string(a // b))
