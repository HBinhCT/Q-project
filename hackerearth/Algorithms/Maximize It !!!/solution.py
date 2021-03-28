"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
k = int(input())
gems = []
for _ in range(n):
    ni, wi = list(map(int, input().strip().split()))
    gems.append((ni, wi))
gems.sort(key=lambda x: x[1])
weight = 0
checked = set()
for gem in gems:
    if gem[0] in checked:
        continue
    if gem[1] + weight > k:
        break
    checked.add(gem[0])
    weight += gem[1]
print(','.join(str(i) for i in sorted(checked)) if checked else -1)
