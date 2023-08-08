def get_survivors(strengths, strongest, nominee, init=1, step=1):
    survivors = []
    while strengths[init] != strongest:
        if strengths[init] > nominee:
            nominee = strengths[init]
            survivors.append(init + 1)
        init += step
    return survivors, init + 1


n = int(input())
s = list(map(int, input().strip().split()))
most = max(s)
positions = [1]
if most == s[0]:
    stands, _ = get_survivors(s, most, s[-1], n - 2, -1)
    positions.extend(stands)
elif most == s[-1]:
    stands, last = get_survivors(s, most, s[0])
    positions.extend(stands)
    positions.append(last)
else:
    stands, last = get_survivors(s, most, s[0])
    positions.extend(stands)
    positions.append(last)
    positions.append(n)
    stands, _ = get_survivors(s, most, s[-1], n - 2, -1)
    positions.extend(stands)
positions.sort()
print(" ".join(map(str, positions)))
