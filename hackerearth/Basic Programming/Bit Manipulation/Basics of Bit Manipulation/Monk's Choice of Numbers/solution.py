t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    numbers = list(map(int, input().strip().split()))
    cheesecakes = sorted([bin(int(i)).count("1") for i in numbers], reverse=True)
    print(sum(cheesecakes[:k]))
