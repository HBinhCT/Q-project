"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
to_minute = lambda h=0, m=0: h * 60 + m
for i in range(t):
    n = int(input())
    x, y = map(int, input().strip().split(':'))
    p, q = map(int, input().strip().split(':'))
    a, b = map(int, input().strip().split(':'))
    r = int(input())
    s = int(input())
    times = list()
    for j in range(n):
        start_time, end_time = input().strip().split()
        h1, m1 = map(int, start_time.split(':'))
        h2, m2 = map(int, end_time.split(':'))
        times.append((to_minute(h1, m1), to_minute(h2, m2)))
    in_time = to_minute(x, y)
    wake_up_time = to_minute(p, q)
    store_open_time = to_minute(a, b)
    travel_time = to_minute(m=r)
    selection_time = to_minute(m=s)
    time_constant = 2 * travel_time + selection_time
    start = max(wake_up_time, store_open_time - travel_time)
    anticipate_end = start + time_constant
    min_val = float('inf')
    friend = -1
    for index, time in enumerate(times):
        if anticipate_end < time[0] and anticipate_end < in_time:
            if friend == -1 or anticipate_end < min_val:
                friend = index + 1
                min_val = anticipate_end
        elif max(time[1], start) + time_constant < in_time:
            takes = max(time[1], start) + time_constant
            if takes < min_val:
                min_val = takes
                friend = index + 1
    print(f'Case {i + 1}: {friend}')
