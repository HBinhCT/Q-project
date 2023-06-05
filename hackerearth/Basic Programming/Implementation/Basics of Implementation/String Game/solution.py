t = int(input())
for _ in range(t):
    s = set(input())
    print('Player1' if len(s) % 2 else 'Player2')
