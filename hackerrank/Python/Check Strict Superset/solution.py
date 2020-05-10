a = set(input().rstrip().split())
print(all(a > set(input().rstrip().split()) for _ in range(int(input().rstrip()))))
