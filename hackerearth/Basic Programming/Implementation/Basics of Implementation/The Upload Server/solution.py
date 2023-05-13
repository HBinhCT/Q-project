n = int(input())
for _ in range(n):
    strings = input().strip().split()
    ln = len(strings)
    names = integers = 0
    for string in strings:
        flag = False
        for c in string:
            if c.isalpha():
                names += 1
                break
        else:
            if string[0] != '0':
                integers += 1
    if ln == 2 and names == integers == 1:
        print('M')
    elif ln == 3 and names == 1 and integers == 2:
        print('V')
    else:
        print('N')
