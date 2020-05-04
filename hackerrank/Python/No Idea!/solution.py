def happiness(array, set_a, set_b):
    total = 0
    for x in array:
        total += x in set_a
        total -= x in set_b
    return total


if __name__ == '__main__':
    n, m = list(map(int, input().rstrip().split()))
    arr = list(map(int, input().rstrip().split()))
    A = set(map(int, input().rstrip().split()))
    B = set(map(int, input().rstrip().split()))
    result = happiness(arr, A, B)
    print(result)
