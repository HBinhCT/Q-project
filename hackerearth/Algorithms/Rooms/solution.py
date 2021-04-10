"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    arrival_times = list(map(int, input().strip().split()))
    durations = list(map(int, input().strip().split()))
    longest = max(sum(z) for z in zip(arrival_times, durations))
    calc = [0] * longest
    for z in zip(arrival_times, durations):
        calc[z[0] - 1] += 1
        calc[z[0] + z[1] - 1] -= 1
    total = 0
    rooms = 0
    for i in calc:
        total += i
        rooms = max(rooms, total)
    print(rooms)
