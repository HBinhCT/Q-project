from datetime import datetime, timedelta

t = int(input())
for _ in range(t):
    date = input().strip()
    date_obj = datetime.strptime(date, "%d %B %Y")
    previous_day = date_obj - timedelta(days=1)
    print(previous_day.strftime("%d %B %Y").lstrip("0"))
