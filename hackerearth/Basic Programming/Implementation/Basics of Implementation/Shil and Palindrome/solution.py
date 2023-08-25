from collections import Counter

s = input().strip()
haft = mid = ""
odd = 0
for k, v in Counter(s).items():
    if v % 2:
        odd += 1
        if odd > 1:
            print("-1")
            break
        mid += k
        v -= 1
    haft += k * (v // 2)
else:
    haft = "".join(sorted(haft))
    print(haft + mid + haft[::-1])
