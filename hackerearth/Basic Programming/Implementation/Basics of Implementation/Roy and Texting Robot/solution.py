groups = {
    "_": 0,
    "0": 0,
    ".": 1,
    ",": 1,
    "?": 1,
    "!": 1,
    "1": 1,
    "a": 2,
    "b": 2,
    "c": 2,
    "2": 2,
    "d": 3,
    "e": 3,
    "f": 3,
    "3": 3,
    "g": 4,
    "h": 4,
    "i": 4,
    "4": 4,
    "j": 5,
    "k": 5,
    "l": 5,
    "5": 5,
    "m": 6,
    "n": 6,
    "o": 6,
    "6": 6,
    "p": 7,
    "q": 7,
    "r": 7,
    "s": 7,
    "7": 7,
    "t": 8,
    "u": 8,
    "v": 8,
    "8": 8,
    "w": 9,
    "x": 9,
    "y": 9,
    "z": 9,
    "9": 9,
}
indexes = {
    "_": 1,
    "0": 2,
    ".": 1,
    ",": 2,
    "?": 3,
    "!": 4,
    "1": 5,
    "a": 1,
    "b": 2,
    "c": 3,
    "2": 4,
    "d": 1,
    "e": 2,
    "f": 3,
    "3": 4,
    "g": 1,
    "h": 2,
    "i": 3,
    "4": 4,
    "j": 1,
    "k": 2,
    "l": 3,
    "5": 4,
    "m": 1,
    "n": 2,
    "o": 3,
    "6": 4,
    "p": 1,
    "q": 2,
    "r": 3,
    "s": 4,
    "7": 5,
    "t": 1,
    "u": 2,
    "v": 3,
    "8": 4,
    "w": 1,
    "x": 2,
    "y": 3,
    "z": 4,
    "9": 5,
}
t = int(input())
for _ in range(t):
    s = input().strip()
    total_time = 0
    cursor = 1
    for c in s:
        if cursor != groups[c]:
            total_time += 1
        total_time += indexes[c]
        cursor = groups[c]
    print(total_time)