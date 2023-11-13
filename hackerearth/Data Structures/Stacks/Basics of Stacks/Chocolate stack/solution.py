def solution(N, C):
    # Write your code here
    stack = []
    for i in C:
        if i:
            stack.append(i)
        else:
            yield stack.pop()


N = int(input())
C = list(map(int, input().split()))

out_ = solution(N, C)
print(" ".join(map(str, out_)))
