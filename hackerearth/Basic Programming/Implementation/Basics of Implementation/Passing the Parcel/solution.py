n = int(input())
lyrics = input().strip()
students = list(range(1, n + 1))
roll_number = 0
while len(students) > 1:
    for lyric in lyrics:
        if "a" == lyric:
            roll_number += 1
        else:
            students.pop(roll_number)
        total = len(students)
        if 1 == total:
            break
        if roll_number == total:
            roll_number = 0
print(students[0])
