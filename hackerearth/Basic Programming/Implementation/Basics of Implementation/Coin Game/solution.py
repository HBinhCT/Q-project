t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    turn = 0
    for i in a:
        while not i % 2:
            turn += 1
            i //= 2
    print('Charlie' if turn % 2 else 'Alan')
