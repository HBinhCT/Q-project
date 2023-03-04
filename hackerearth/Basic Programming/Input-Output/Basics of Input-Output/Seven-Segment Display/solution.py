d = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}
t = int(input())
for _ in range(t):
    n = input().strip()
    cnt = sum(d[i] for i in n)
    if cnt % 2:
        print('7' + ((cnt - 3) // 2) * '1')
    else:
        print((cnt // 2) * '1')
