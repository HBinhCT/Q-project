def solution(N, C, audience):
    # Write your code here
    for i in range(N):
        total = 0
        for j in range(N):
            if audience[i][1] <= audience[j][1] <= audience[i][2]:
                total += audience[j][0]
        if total > C:
            return 'No'
    return 'Yes'


N = int(input())
C = int(input())
audience = [list(map(int, input().split())) for i in range(N)]

out_ = solution(N, C, audience)
print(out_)
