n = int(input())
s = input().strip()
q = int(input())
shifts = []
for _ in range(q):
    shifts.append(int(input()))
sorted_shifts = sorted(set(shifts))
all_shifts = {}
smallest_string = shifted_string = s
smallest_idx = 0
k = sorted_shifts.pop(0)
for i in range(n):
    if smallest_string > shifted_string:
        smallest_string = shifted_string
        smallest_idx = i
    if i == k:
        all_shifts[k] = smallest_idx
        if not sorted_shifts:
            break
        k = sorted_shifts.pop(0)
    shifted_string = shifted_string[1:] + shifted_string[0]
for i in shifts:
    print(all_shifts[i])
