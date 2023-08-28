def find_winner(players, res):
    size = len(players)
    if 2 == size:
        p1, p2 = players
        if p1 > p2:
            return p1 if 1 == res[p1 - 2][p2 - 1] else p2
        return p2 if 1 == res[p2 - 2][p1 - 1] else p1
    mid = size // 2
    return find_winner(
        [find_winner(players[:mid], res), find_winner(players[mid:], res)], res
    )


n = int(input())
m = 2**n
a = []
for _ in range(m - 1):
    a.append(list(map(int, input().strip().split())))
p = [i for i in range(1, m + 1)]
print(find_winner(p, a))
