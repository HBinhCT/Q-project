t = int(input())
for _ in range(t):
    n = int(input())
    strengths = list(map(int, input().strip().split()))
    total = sum(i for i in strengths if i > 0)
    print("No" if not total or total & total - 1 else "Yes")
