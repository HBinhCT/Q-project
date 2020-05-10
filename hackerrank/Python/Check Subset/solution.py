for _ in range(int(input().rstrip())):
    _, a = input(), set(map(int, input().rstrip().split()))
    _, b = input(), set(map(int, input().rstrip().split()))
    print(a.issubset(b))
