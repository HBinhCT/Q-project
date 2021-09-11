#!/bin/python3

import os


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    return max([h[ord(char) - ord('a')] for char in word]) * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
