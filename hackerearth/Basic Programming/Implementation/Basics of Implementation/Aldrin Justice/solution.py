t = int(input())
for _ in range(t):
    bt1, bt2, mt1, mt2 = map(int, input().strip().split())
    left = min(max(bt1, bt2), max(mt1, mt2))
    right = max(min(bt1, bt2), min(mt1, mt2))
    if left > right:
        print("Nothing")
    elif left < right:
        print("Line")
    else:
        print("Point")
