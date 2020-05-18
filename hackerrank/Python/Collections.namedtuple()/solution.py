from collections import namedtuple

n, student = int(input()), namedtuple('Student', input())
print('{:.2f}'.format(sum([int(student(*input().rstrip().split()).MARKS) for _ in range(n)]) / n))
