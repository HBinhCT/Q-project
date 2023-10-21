last_move = 0


def solve(Number):
    # Return character A from this function if player A is winner. Return
    # character B from this function if player B is winner. Also set the
    # value of global variable last_move to the last move number of the
    # player who is winner in the game
    global last_move
    flips = set()
    for num in Number:
        for i in range(len(num)):
            if num[i] == "1":
                flips.add(i)
    last_move = len(flips)
    if last_move % 2:
        return "A"
    return "B"


N = int(input())
Number = []
for _ in range(N):
    Number.append(input())

out_ = solve(Number)
print(out_)
print(last_move)
