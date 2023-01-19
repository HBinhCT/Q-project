def solve(N, Query):
    # Write your code here
    histories = {}
    visited = set()
    for time, url, key, user_id in Query:
        time = int(time)
        lk = len(key)
        if key in visited or lk < 2 or lk > 12:
            yield 'NO'
            continue
        if user_id in histories and time - histories[user_id] < 5:
            yield 'NO'
            continue
        if 'http://' != url[:7] and 'https://' != url[:8]:
            yield 'NO'
            continue
        if key.isalnum():
            visited.add(key)
        else:
            yield 'NO'
            continue
        histories[user_id] = time
        yield 'YES'


N = int(input())
Query = [input().split() for i in range(N)]

out_ = solve(N, Query)
for i_out_ in out_:
    print(i_out_)
