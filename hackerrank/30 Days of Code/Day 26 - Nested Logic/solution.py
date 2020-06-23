day_actual, month_actual, year_actual = map(int, input().strip().split())
day_expected, month_expected, year_expected = map(int, input().strip().split())
if (year_actual, month_actual, day_actual) <= (year_expected, month_expected, day_expected):
    print(0)
elif (year_actual, month_actual) == (year_expected, month_expected):
    print(15 * (day_actual - day_expected))
elif year_actual == year_expected:
    print(500 * (month_actual - month_expected))
else:
    print(10000)
