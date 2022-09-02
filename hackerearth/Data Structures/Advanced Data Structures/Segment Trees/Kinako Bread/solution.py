n, m = map(int, input().strip().split())
breads = list(map(int, input().strip().split()))
lefts = [0] * (m + 1)
rights = [0] * (m + 1)
for i in range(1, m + 1):
    lefts[i], rights[i] = map(int, input().strip().split())
gt_left = gt_right = -1
eq_left = 0
eq_right = m
left_vals = [0] * (m + 1)
right_vals = [0] * (m + 1)
ans = 0
for i in range(n):
    j = breads[i]
    left_vals[j] += 1
    right_vals[j] += 1
    if left_vals[j] == lefts[j]:
        eq_left += 1
    if right_vals[j] > rights[j]:
        eq_right -= 1
    while gt_left < i:
        k = breads[gt_left + 1]
        if left_vals[k] > lefts[k]:
            left_vals[k] -= 1
            gt_left += 1
        else:
            break
    while gt_right < i and right_vals[j] > rights[j]:
        gt_right += 1
        k = breads[gt_right]
        right_vals[k] -= 1
        if right_vals[k] == rights[k]:
            eq_right += 1
    if m == eq_left == eq_right and gt_right <= gt_left:
        ans += gt_left - gt_right + 1
print(ans)
