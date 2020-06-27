def main(marks, q):
    print('{0:.2f}'.format(sum(marks[q]) / len(marks[q])))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    main(student_marks, query_name)
