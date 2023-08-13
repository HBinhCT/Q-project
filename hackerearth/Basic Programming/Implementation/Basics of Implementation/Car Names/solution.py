n = int(input())
for _ in range(n):
    name = input().strip()
    uniq = set(name)
    if len(uniq) == 3:
        count = sum(c * name.count(c) in name for c in uniq)
        print("OK" if count == 3 else "Not OK")
    else:
        print("Not OK")
