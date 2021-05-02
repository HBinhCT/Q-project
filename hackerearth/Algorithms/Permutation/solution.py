"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = input().strip().split()
goal = ''.join(map(str, range(1, n + 1)))
acts = {''.join(a)}
done = set()
res = 0
while goal not in acts:
    olds = acts
    done |= acts
    acts = set()
    res += 1
    for old in olds:
        for j in range(1, n):
            gen = old[0:j + 1][::-1] + old[j + 1:]
            if gen not in done:
                acts.add(gen)
print(res)
