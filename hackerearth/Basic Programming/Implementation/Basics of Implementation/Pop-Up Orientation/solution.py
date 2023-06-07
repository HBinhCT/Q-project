t = int(input())
for _ in range(t):
    x, y, l, m, a, b = map(int, input().strip().split())
    print(('bottom-' if (m <= b) else 'top-') + ('right' if (l <= x - a) else 'left'))
