"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m = map(int, input().strip().split())
teachers = {}
for _ in range(n):
    teachers[input()] = {}
for i in range(m):
    teacher_name, student_name, student_age = input().strip().split()
    teachers[teacher_name][int(student_age)] = student_name
for teacher in sorted(teachers):
    print(teacher)
    for age in sorted(teachers[teacher]):
        print(teachers[teacher][age], age)
