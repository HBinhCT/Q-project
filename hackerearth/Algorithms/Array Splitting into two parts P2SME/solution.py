def find_answer(A):
    # Write your code here
    return int((sum(A) / 2) ** 2)


N = int(input())
A = map(int, input().split())

out_ = find_answer(A)
print(out_)
