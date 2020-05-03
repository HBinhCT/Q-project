def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase
    for i in range(size - 1, -size, -1):
        s = '-'.join(alpha[size - 1:abs(i):-1] + alpha[abs(i):size])
        print(s.center(4 * size - 1 - 2, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
