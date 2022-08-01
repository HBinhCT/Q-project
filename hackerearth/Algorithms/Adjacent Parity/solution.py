t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    even_count = odd_count = 0
    for i in a:
        if i % 2:
            odd_count += 1
        else:
            even_count += 1
    if even_count == 0 or odd_count == 0 or even_count == odd_count or abs(even_count - odd_count) == 1:
        print('YES')
    else:
        print('NO')
