def merge_the_tools(string, k):
    # your code goes here
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(*[d.setdefault(c, c) for c in part if c not in d], sep='')


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
