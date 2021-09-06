"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict


def check_assign(x, y, v, string, pair_list, sharp_val_list, alpha_cat, beta_cat):
    child_sharp_values = []
    i = x + 1
    total_alpha = 0
    total_beta = 0
    while i < y:
        if string[i] == '(':
            total_alpha += alpha_cat[i]
            total_beta += beta_cat[i]
            i = pair_list[i]
        else:
            child_sharp_values.append(sharp_val_list[i])
        i += 1
    if total_alpha > v and total_beta > v:
        return False
    child_sharp_values.sort()
    is_alpha = False
    is_beta = False
    if total_alpha <= v and total_beta <= v:
        if total_alpha < total_beta:
            is_beta = True
        else:
            is_alpha = True
    elif total_alpha <= v:
        is_alpha = True
    else:
        is_beta = True
    if is_alpha:
        alpha_cat[x] = v
        beta_cat[x] = sum(child_sharp_values) + total_alpha - v
    elif is_beta:
        alpha_cat[x] = sum(child_sharp_values) + total_beta - v
        beta_cat[x] = v
    return True


n = int(input())
s = input()
sharp_values = defaultdict(int)
pairs = defaultdict(int)
pair_values = defaultdict(int)
for _ in range(s.count('#')):
    idx, val = map(int, input().strip().split())
    idx -= 1
    sharp_values[idx] = val
for _ in range(s.count('(')):
    start, end, val = map(int, input().strip().split())
    start -= 1
    end -= 1
    pairs[start] = end
    pairs[end] = start
    pair_values[start] = val
    pair_values[end] = val
alpha_category = defaultdict(int)
beta_category = defaultdict(int)
for i in range(n):
    if s[i] == ')' and not check_assign(
            pairs[i],
            i,
            pair_values[i],
            s,
            pairs,
            sharp_values,
            alpha_category,
            beta_category
    ):
        print('No')
        break
else:
    print('Yes')
