def Solve(k, arr):
    # Write code here
    total = counter = 0
    r = k
    for i in arr:
        if i >= 0:
            counter += 1
            total += i
            r = k
        else:
            if counter:
                r -= 1
                total += abs(i) if r < 0 else i
            else:
                return abs(sum(arr) + i)
    return abs(total)


n, k = map(int, input().split())
arr = map(int, input().split())

out_ = Solve(k, arr)
print(out_)
