#!/bin/python3

import math
import os
import random
import re
import sys

EMPTY = '-'
SIZE = 10


def possible_directions(board, word):
    ln = len(word)
    for i in range(SIZE):
        for j in range(SIZE):
            is_possible_ver = is_possible_hor = True
            for k in range(ln):
                if not is_possible_ver and not is_possible_hor:
                    break
                # vertical possible location
                if is_possible_ver and i < SIZE - ln + 1:
                    if board[i + k][j] not in (EMPTY, word[k]):
                        is_possible_ver = False
                # horizontal possible location
                if is_possible_hor and j < SIZE - ln + 1:
                    if board[i][j + k] not in (EMPTY, word[k]):
                        is_possible_hor = False
            else:
                if is_possible_ver and i < SIZE - ln + 1:
                    yield i, j, 1  # 1 is axis indicator
                if is_possible_hor and j < SIZE - ln + 1:
                    yield i, j, -1  # -1 is axis indicator


def move(board, word, start_location):
    i, j, axis = start_location
    ln = len(word)
    if axis == 1:  # axis 1 is vertical
        for k in range(ln):
            board[i + k][j] = word[k]
    else:  # axis -1 is horizontal
        for k in range(ln):
            board[i][j + k] = word[k]


def rollback(board, word, start_location):
    i, j, axis = start_location
    ln = len(word)
    if axis == 1:  # axis 1 is vertical
        for k in range(ln):
            board[i + k][j] = EMPTY
    else:  # axis -1 is horizontal
        for k in range(ln):
            board[i][j + k] = EMPTY


# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    solved = False

    def _crossword_puzzle(board, list_words):
        nonlocal solved
        if solved:
            return
        if len(list_words) == 0:
            solved = True
            return
        word = list_words.pop()
        for direction in possible_directions(board, word):
            move(board, word, direction)
            _crossword_puzzle(board, list_words)
            if solved:
                return
            rollback(board, word, direction)
        list_words.append(word)

    fill_map = [list(item) for item in crossword]
    _crossword_puzzle(fill_map, words.split(';'))
    res = [''.join(row) for row in fill_map]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
