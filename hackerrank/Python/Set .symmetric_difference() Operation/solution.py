_, a = input(), set(input().rstrip().split())
_, b = input(), set(input().rstrip().split())
print(len(a.symmetric_difference(b)))  # or
# print(len(a ^ b))
