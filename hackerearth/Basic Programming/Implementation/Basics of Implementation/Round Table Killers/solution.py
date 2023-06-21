n, k, x = map(int, input().strip().split())
persons = list(range(1, n + 1))
while len(persons) > 1:
    i = persons.index(x)
    pre = persons[:i]
    del persons[:i]
    persons.extend(pre)
    i = persons.index(x)
    i += 1
    del persons[i:i + x % k]
    if len(persons) > 1:
        x = persons[i]
print(persons[0])
