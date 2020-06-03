import numpy
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(numpy.mean(numbers))
print(numpy.median(numbers))
print(int(stats.mode(numbers)[0]))
