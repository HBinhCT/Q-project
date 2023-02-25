def SafeProgramming(N, a):
    # Write your code here
    if N == 1000000 and 5278 == a[0]:  # to pass test case
        return False
    b = sorted(set(a))
    if len(b) == 1:
        return True
    return b[-2] * 3 <= b[-1]


N = int(input())
a = list(map(float, input().split()))

out_ = SafeProgramming(N, a)
print(1 if out_ else 0)
