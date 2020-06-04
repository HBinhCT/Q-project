import statistics

n = int(input())
data = list(map(int, input().strip().split()))
freq = list(map(int, input().strip().split()))
s = []
for i in range(n):
    s += [data[i]] * freq[i]
N = sum(freq)
s.sort()
q1 = statistics.median(s[:N // 2])
q3 = statistics.median(s[(N + 1) // 2:])
print(f'{q3 - q1:.1f}')
