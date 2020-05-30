def wrapper(f):
    def fun(l):
        # complete the function
        f(map(lambda x: "+91 " + x[-10:-5] + " " + x[-5:], l))

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
