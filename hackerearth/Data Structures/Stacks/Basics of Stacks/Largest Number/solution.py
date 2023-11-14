n = input().strip()
k = int(input())
stack = []
for d in n:
    while stack and k and stack[-1] < d:
        stack.pop()
        k -= 1
    stack.append(d)
while k:
    stack.pop()
    k -= 1
print("".join(stack).lstrip("0") or "0")
