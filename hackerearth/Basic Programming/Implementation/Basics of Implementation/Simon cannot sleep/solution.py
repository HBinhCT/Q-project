hh, mm = map(int, input().split(':'))
t = hh * 60 + mm
count = t * 11 // 720 + 1
print(count)
