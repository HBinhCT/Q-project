t = int(input())
for _ in range(t):
    n = int(input())
    p, w = map(int, input().strip().split())
    waiting_floors = list(map(int, input().strip().split()))
    reached_floors = {i: [] for i in range(1, n + 1)}
    total_persons = total_weights = 0
    ans = n
    is_overload = False
    for i in range(1, n):
        desired_floors = list(map(int, input().strip().split()))
        employee_weights = list(map(int, input().strip().split()))
        if is_overload:
            continue
        for j in range(len(desired_floors)):
            reached_floors[desired_floors[j]].append(employee_weights[j])
        leave_employees = reached_floors[i]
        if len(leave_employees):
            total_persons -= len(leave_employees)
            total_weights -= sum(leave_employees)
        total_persons += len(desired_floors)
        total_weights += sum(employee_weights)
        if total_persons > p or total_weights > w:
            ans = i
            is_overload = True
    print(ans)
