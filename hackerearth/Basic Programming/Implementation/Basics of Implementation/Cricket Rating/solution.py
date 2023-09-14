n = int(input())
if not n:
    print(0)
else:
    ratings = list(map(int, input().strip().split()))
    sum_rating = max_sum = 0
    for i in ratings:
        sum_rating += i
        sum_rating = max(sum_rating, 0)
        max_sum = max(max_sum, sum_rating)
    print(max_sum)
