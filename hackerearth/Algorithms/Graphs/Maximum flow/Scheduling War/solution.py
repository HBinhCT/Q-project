n = int(input())
si = list(map(int, input().strip().split()))
b = int(input())
systems = []
processes = []
system_lens = []
total_processes = 0
for _ in range(b):
    s, *nums, p = map(int, input().strip().split())
    system_lens.append(s)
    systems += list(nums)
    processes.append(p)
    total_processes += p
total_systems = sum(si[i - 1] for i in list(set(systems)))
if total_processes > total_systems:
    print(total_processes - total_systems)
else:
    i = count_processes = 0
    for j, system in enumerate(system_lens):
        count_systems = 0
        for _ in range(system):
            count_systems += si[systems[i] - 1]
            i += 1
        if count_systems < processes[j]:
            count_processes += processes[j] - count_systems
    print(count_processes)
