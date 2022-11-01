t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int, input().strip().split())
    even_nums = [i for i in a if i % 2 == 0]
    even_count = len(even_nums)
    odd_count = 2 * n - even_count
    if even_count >= odd_count or sum((i & ~(i - 1)) // 4 for i in even_nums) >= (n - even_count):
        print('YES')
    else:
        print('NO')
