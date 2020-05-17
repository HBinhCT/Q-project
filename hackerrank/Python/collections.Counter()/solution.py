import collections

X = int(input())
shoe_sizes = collections.Counter(map(int, input().rstrip().split()))
amount = 0
for _ in range(int(input())):
    size, price = map(int, input().rstrip().split())
    if shoe_sizes[size]:
        amount += price
        shoe_sizes[size] -= 1
print(amount)
