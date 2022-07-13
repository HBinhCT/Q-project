n = int(input())
counter = {}
occupied_list = []
for _ in range(n):
    li = input().strip()
    if li not in counter:
        counter[li] = 0
        occupied_list.append(li)
    else:
        i = counter[li]
        pick = li + str(i)
        while pick in counter:
            i += 1
            pick = li + str(i)
        occupied_list.append(pick)
        counter[pick] = 0
        counter[li] = i + 1
print('\n'.join(occupied_list))
