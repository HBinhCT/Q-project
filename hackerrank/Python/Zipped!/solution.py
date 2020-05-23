n, x = map(int, input().split())
students = []
for _ in range(x):
    students.append(map(float, input().split()))
for i in zip(*students):
    print(sum(i) / len(i))
