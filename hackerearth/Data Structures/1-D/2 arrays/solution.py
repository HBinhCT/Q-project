n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
a_count = a.count(-1)
b_count = b.count(-1)
a_sum = sum(a)
b_sum = sum(b)
if a_count == b_count:
    print('Infinite')
elif a_count == 1:
    print(1 if a_sum < b_sum else 0)
elif b_count == 1:
    print(1 if b_sum < a_sum else 0)
elif a_count == 2 and a_sum < b_sum:
    print(b_sum - a_sum - 1)
elif b_count == 2 and b_sum < a_sum:
    print(a_sum - b_sum - 1)
else:
    print(0)
