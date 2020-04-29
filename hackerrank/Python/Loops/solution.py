if __name__ == '__main__':
    n = int(input())

    print(*[num ** 2 for num in range(n)], sep='\n')
