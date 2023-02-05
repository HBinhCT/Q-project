def Consistent(N):
    # Write your code here
    mod = 1000000007
    counter = [1, 0]
    for i in range(1, N):
        counter[i % 2] = (sum(counter) + 1) % mod
    return sum(counter) % mod


N = int(input())

out_ = Consistent(N)
print(out_)
