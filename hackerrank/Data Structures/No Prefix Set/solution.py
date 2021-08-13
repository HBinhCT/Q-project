#!/bin/python3

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    trie = {}
    for word in words:
        curr = trie
        length = len(word)
        for i in range(length):
            letter = word[i]
            if letter in curr:
                curr = curr[letter]
                if not curr or i == length - 1:
                    print('BAD SET')
                    print(word)
                    return
                continue
            curr[letter] = {}
            curr = curr[letter]
    print('GOOD SET')


if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
