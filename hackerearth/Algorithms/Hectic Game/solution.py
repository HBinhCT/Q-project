"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from functools import reduce
from operator import xor


def calc(arr1, arr2, arr3):
    idx = 0
    temp = [idx]
    for i in range(len(arr2)):
        if arr1[i] > arr2[idx]:
            temp.append(i)
            idx = i
    temp.reverse()
    for i in temp:
        del arr1[i]
        del arr2[i]
        del arr3[i]
    return arr1, arr2, arr3, len(temp)


t = int(input())
for _ in range(t):
    n = int(input())
    tasks = []
    for i in range(n):
        time = list(map(int, input().strip().split()))
        time.reverse()
        time.append(i)
        tasks.append(time)
    tasks.sort()
    f = []
    s = []
    ind = []
    for i in range(n):
        f.append(tasks[i][0])
        s.append(tasks[i][1])
        ind.append(tasks[i][2])
    list_a = []
    list_b = []
    while len(s):
        s, f, ind, c = calc(s, f, ind)
        list_a.append(c)
        if not len(s):
            break
        s, f, ind, c = calc(s, f, ind)
        list_b.append(c)
    a = reduce(xor, list_a)
    b = reduce(xor, list_b)
    if a == b:
        print('Tie')
    elif a > b:
        print('Alice')
    else:
        print('Bob')
