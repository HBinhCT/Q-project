from collections import deque

s = list(input())
stack = deque([])
for i in range(len(s)):
    if s[i] == '/':
        stack.append(i)
    elif s[i] == '\\':
        j = stack.pop()
        s[j:i + 1] = reversed(s[j:i + 1])
print(''.join(filter(lambda c: c != '\\' and c != '/', s)))
