for _ in range(int(input())):
    a, b = input().rstrip().split()
    try:
        print(int(a) // int(b))
    except BaseException as e:
        print('Error Code:', e)
