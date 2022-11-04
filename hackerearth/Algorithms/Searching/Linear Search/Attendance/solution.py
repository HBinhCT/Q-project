import datetime
import time
from fractions import Fraction


def time_to_sec(time_str):
    x = time.strptime(time_str, '%H:%M:%S')
    return int(datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds())


n = int(input())
start_time, end_time = map(time_to_sec, input().strip().split())
mx = 86400
counter = [0] * mx
me = [0] * mx
for _ in range(n):
    sid, m, *pairs = input().strip().split()
    sid = int(sid)
    m = int(m)
    for i in range(m):
        arrival_time = time_to_sec(pairs[2 * i])
        leave_time = time_to_sec(pairs[2 * i + 1])
        counter[arrival_time] += 1
        counter[leave_time] -= 1
        if sid == 1:
            me[arrival_time] += 1
            me[leave_time] -= 1
mn = float('inf')
for i in range(start_time, end_time):
    counter[i] += counter[i - 1]
    me[i] += me[i - 1]
    mn = min(mn, counter[i])
p = q = 0
for i in range(start_time, end_time):
    if counter[i] == mn:
        q += 1
        if me[i] == 1:
            p += 1
if p == 0:
    print(0)
elif p == q:
    print('1/1')
else:
    print(Fraction(p, q))
