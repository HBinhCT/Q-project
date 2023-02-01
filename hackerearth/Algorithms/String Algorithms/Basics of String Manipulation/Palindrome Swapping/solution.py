def make_equal(T, S):
    # Write your code here
    n = len(T)
    m = n // 2
    if n % 2 and S[m] != T[m]:
        return 'NO'
    for i in range(m):
        j = n - i - 1
        if not ((S[i] == S[j] and T[i] == T[j]) or
                (S[i] == T[i] and S[j] == T[j]) or
                (S[i] == T[j] and S[j] == T[i])):
            return 'NO'
    return 'YES'


T = input()
S = input()

out_ = make_equal(T, S)
print(out_)
