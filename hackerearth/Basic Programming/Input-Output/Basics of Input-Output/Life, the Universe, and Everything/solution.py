from sys import stdin

numbers = stdin.read().splitlines()
for number in numbers:
    if number == '42':
        break
    print(number)
