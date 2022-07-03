t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    candies = input().strip().split()
    currently_students = set(candies[:n])
    more_students = candies[n:]
    for student in more_students:
        if student in currently_students:
            print('YES')
        else:
            currently_students.add(student)
            print('NO')
