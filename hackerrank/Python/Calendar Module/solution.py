import calendar

m, d, y = map(int, input().split())
assert 2000 < y < 3000
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
