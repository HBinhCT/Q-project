t = int(input())
for _ in range(t):
    b = int(input())
    u = v = 1
    for _ in range(b):
        balloon_type = input().strip()
        if 'N' == balloon_type:
            u, v = min(u, -v), max(-u, v)
        else:
            op, x = balloon_type.split()
            x = int(x)
            if '+' == op:
                u, v = min(u, u + x), max(v, v + x)
            elif '-' == op:
                u, v = min(u, u - x), max(v, v - x)
            elif '*' == op:
                u, v = min(u, u * x, v * x), max(v, u * x, v * x)
            elif '/' == op:
                u, v = min(u, u // x, v // x), max(v, u // x, v // x)
    print(v)
