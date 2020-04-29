if __name__ == '__main__':
    N = int(input())

    arr = []
    for _ in range(N):
        command = input().rstrip().split()
        func = command[0]
        args = command[1:]
        if func != 'print':
            eval(f"arr.{func}({','.join(args)})")
        else:
            print(arr)
