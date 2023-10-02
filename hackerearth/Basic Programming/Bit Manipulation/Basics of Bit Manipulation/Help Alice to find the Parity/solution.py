def find_x(a, b):
    def get_xor(n):
        mod = n % 4
        if 0 == mod:
            return n
        elif 1 == mod:
            return 1
        elif 2 == mod:
            return n + 1
        elif 3 == mod:
            return 0

    return get_xor(a - 1) ^ get_xor(b)


l, r = map(int, input().strip().split())
x = find_x(l, r)
print("odd" if x % 2 else "even")
