#!/bin/python3


#
# Complete the aOrB function below.
#
def aOrB(k, a, b, c):
    #
    # Write your code here.
    #
    a, b, c = int(a, 16), int(b, 16), int(c, 16)
    # get minimum flips
    ac = a ^ c
    bc = b ^ c
    ab = ac & bc
    ab &= ~c
    x = (a | b) ^ c
    x = bin(x).count('1') + bin(ab).count('1')
    if x > k:
        print(-1)
    else:
        # get spare flips
        spare = k - x
        # flip off set bits in a and b to match off bits in c
        a &= c
        b &= c
        # find bits in a or b that need to be set to match c
        x = (a | b) ^ c
        #  apply x set bits to b
        b |= x
        # use spare flips to reduce a to its minimum
        l = len(bin(a)) - 1
        mask = 2 ** l
        ones = 2 ** len(bin(c)) - 1
        while spare and mask:
            mask >>= 1
            if a & mask:
                if b & mask:
                    a &= ones ^ mask
                    spare -= 1
                elif spare > 1:
                    a &= ones ^ mask
                    b |= mask
                    spare -= 2
        # print a and b in hex
        print(hex(a)[2:].upper())
        print(hex(b)[2:].upper())


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        k = int(input())

        a = input()

        b = input()

        c = input()

        aOrB(k, a, b, c)
