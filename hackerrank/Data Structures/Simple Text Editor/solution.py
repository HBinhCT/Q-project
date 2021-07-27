q = int(input())
s = ''
stack = []
for _ in range(q):
    operation = input().strip().split()
    t = operation[0]
    if t == '1':
        stack.append(s)
        s = s + operation[1]
    elif t == '2':
        stack.append(s)
        k = int(operation[1])
        s = s[0:-k]
    elif t == '3':
        k = int(operation[1])
        print(s[k - 1])
    else:
        s = stack.pop()
