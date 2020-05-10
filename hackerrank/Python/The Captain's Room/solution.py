k, rooms = int(input().rstrip()), list(map(int, input().rstrip().split()))
res = set(rooms)
print(((sum(res) * k) - (sum(rooms))) // (k - 1))
