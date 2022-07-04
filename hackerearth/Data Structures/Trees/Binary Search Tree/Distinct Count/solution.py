t = int(input())
for _ in range(t):
    n, x = map(int, input().strip().split())
    count = len(set(input().strip().split()))
    if x < count:
        print('Average')
    elif x > count:
        print('Bad')
    else:
        print('Good')
