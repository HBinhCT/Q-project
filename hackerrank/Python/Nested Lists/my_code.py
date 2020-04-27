if __name__ == '__main__':
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())

    mark_sheet = [[input(), float(input())] for _ in range(int(input()))]
    second_lowest = sorted(list(set([marks for name, marks in mark_sheet])))[1]
    print('\n'.join([a for a, b in sorted(mark_sheet) if b == second_lowest]))
