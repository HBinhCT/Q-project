def process_string(S):
    # Write your code here
    subs = set()
    n = len(S)
    for i in range(n):
        temp = ''
        for j in range(i, n):
            temp += S[j]
            subs.add(temp)
    res = 0
    for sub in subs:
        if sub[::-1] in subs:
            res = max(res, len(sub))
    if res <= 1:
        yield 'NO'
    else:
        yield 'YES'
        yield res


S = input()

out_ = process_string(S)
for i_out_ in out_:
    print(i_out_)
