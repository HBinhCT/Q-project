_, A = int(input().rstrip()), set(map(int, input().rstrip().split()))
N = int(input())
for _ in range(N):
    method, new_set = input().rstrip().split()[0], set(map(int, input().rstrip().split()))
    getattr(A, method)(new_set)

print(sum(A))
