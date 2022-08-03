def maxCustomers(N, M, d, arr, cost):
    # Write your code here
    arr.sort()
    cost.sort()

    def can_buy(x):
        discount_left = d
        for i in range(x):
            using_discount = max(0, cost[i] - arr[i - x])
            if using_discount > discount_left:
                return False
            else:
                discount_left -= using_discount
        return True

    def get_minimum_total(x):
        total_discount = sum(max(0, cost[i] - arr[i - x]) for i in range(x))
        total_cost = sum(cost[:x])
        money_spent = total_cost - total_discount
        return money_spent if total_discount == d else max(0, total_cost - d)

    left = 0
    right = min(N, M)
    while right - left > 1:
        middle = (left + right) // 2
        if can_buy(middle):
            left = middle
        else:
            right = middle - 1
    if can_buy(right):
        return right, get_minimum_total(right)
    return left, get_minimum_total(left)


N, M, d = map(int, input().split())
arr = list(map(int, input().split()))
cost = list(map(int, input().split()))

out_ = maxCustomers(N, M, d, arr, cost)
print(' '.join(map(str, out_)))
