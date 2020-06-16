T = int(input())
assert 1 <= T <= 10
for i in range(T):
    S = input()
    assert 2 <= len(S) <= 10000
    print(S[::2], S[1::2])
