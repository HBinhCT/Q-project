def findHighestRating(Q, arr, M):
    # Write your code here
    size = max(arr) + 1
    freq = [0] * size
    for i in arr:
        freq[i] += 1
    highest = 0
    for i in range(size):
        cnt = freq[i]
        for j in range(1, Q + 1):
            left = i - j * M
            right = i + j * M
            if left >= 0:
                cnt += freq[left]
            if right < size:
                cnt += freq[right]
        highest = max(highest, cnt)
    return highest


M = int(input())
Q = int(input())
N = int(input())
arr = list(map(int, input().strip().split()))

out_ = findHighestRating(Q, arr, M)
print(out_)
