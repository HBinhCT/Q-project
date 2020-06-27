def main(arr):
    print(sorted(set(arr))[-2])


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    main(arr)
