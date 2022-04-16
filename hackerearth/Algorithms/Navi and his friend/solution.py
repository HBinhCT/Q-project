def purchase(ith=0, total_weight=0, total_price=0, count=0):
    if ith == n or count == c or total_weight == w_max:
        return total_price
    res1 = purchase(ith + 1, total_weight, total_price, count)
    res2 = 0
    next_weight = total_weight + weights[ith]
    if next_weight <= w_max:
        res2 = purchase(ith + 1, next_weight, total_price + prices[ith], count + 1)
    return max(res1, res2)


d = int(input())
for i in range(1, d + 1):
    n = int(input())
    prices = []
    weights = []
    for _ in range(n):
        p, w = map(int, input().strip().split())
        prices.append(p)
        weights.append(w)
    w_max, c = map(int, input().strip().split())
    ans = purchase()
    print(f'For Day #{i}:')
    print(ans if ans > 0 else -1)
