from math import gcd


def fighting(p1, p2, turn=0):
    if p1 == 1:
        return 1
    elif p2 == 1:
        return 0
    elif p1 == p2:
        return turn
    x = gcd(p1, p2)
    y = x > 1
    if turn:
        return (y and (fighting(p1 // x, p2, not turn) == turn)) or (fighting(p1 - 1, p2, not turn) == turn)
    else:
        return not ((y and (fighting(p1, p2 // x, not turn) == turn)) or (fighting(p1, p2 - 1, not turn) == turn))


players = {
    0: 'Arjit',
    1: 'Chandu Don',
}
t = int(input())
for _ in range(t):
    a, b = map(int, input().strip().split())
    if a == 1 and b == 1:
        print('Draw')
    else:
        print(players[fighting(a, b)])
