n = int(input())
a = list(map(int, input().strip().split()))
product = 1
for i in a:
    product = product * i % 1000000007
print(product)
