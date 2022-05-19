n = int(input())
processes = list(map(int, input().strip().split()))
ideal_processes = list(map(int, input().strip().split()))
total_time = j = 0
for i in ideal_processes:
    j %= n
    while i != processes[j]:
        j = (j + 1) % n
        total_time += 1
    processes.pop(j)
    n -= 1
    total_time += 1
print(total_time)
