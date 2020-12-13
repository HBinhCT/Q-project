"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
i = 0
normal = 0
n = -1
for i in range(t):
    k = 0
    if i == 0 or normal == 1:
        n = int(input())
        k = 1
    people = list(map(int, input().strip().split()))
    ln = len(people)
    middle = ln // 2
    if k == 1 and ln == n:
        normal = 1
        girls = people
        boys = list(map(int, input().strip().split()))
    else:
        girls = people[0:middle]
        if i == t - 1:
            boys = people[middle:ln]
        else:
            boys = people[middle:ln - 1]
    girls.sort()
    boys.sort(reverse=True)
    if i == 0 or normal == 1:
        end = n
    else:
        end = middle
    count = 0
    for j in range(end):
        if girls[j] % boys[j] == 0 or boys[j] % girls[j] == 0:
            count += 1
    print(count)
