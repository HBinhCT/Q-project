def solve(n, s):
    # Write your code here
    def query(array, idx):
        total = 0
        while idx > 0:
            total += array[idx]
            idx -= idx & -idx
        return total

    def update(array, idx):
        while idx < len(array):
            array[idx] += 1
            idx += idx & -idx

    chars = {'a': 1, 'b': 0, 'c': -1}
    fx = [0] * n
    for i in range(n):
        fx[i] = fx[i - 1] + chars[s[i]]
    start = n + 1
    tree = [0] * (2 * n + 4)
    res = 0
    update(tree, start)
    for i in range(n):
        j = start + fx[i]
        update(tree, j)
        res += query(tree, j - 1)
        res %= 1000000007
    return res


n = int(input())
s = input()

out_ = solve(n, s)
print(out_)
