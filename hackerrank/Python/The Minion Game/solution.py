def minion_game(string):
    # your code goes here
    vowels = frozenset('AEIOU')
    length = len(string)
    kev_sc = 0
    stu_sc = 0
    for i in range(length):
        if string[i] in vowels:
            kev_sc += length - i
        else:
            stu_sc += length - i
    if kev_sc > stu_sc:
        print('Kevin', kev_sc)
    elif kev_sc < stu_sc:
        print('Stuart', stu_sc)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
