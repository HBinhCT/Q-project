def symmetric_difference(set_1, set_2):
    print(*sorted(set_1 ^ set_2, key=int), sep='\n')


if __name__ == '__main__':
    m, n = [set(input().rstrip().split()) for _ in range(4)][1::2]
    symmetric_difference(m, n)
