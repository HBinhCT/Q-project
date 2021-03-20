"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    s = input()
    a = list(map(int, input().strip().split()))
    arr = [(chr(97 + i), x) for i, x in enumerate(a)]  # ord('a') = 97
    arr.sort(key=lambda x: -x[1])
    included = set()
    chars = 0
    index = 0
    last_char = ''
    last_char_included = 0
    while True:
        if arr[index][0] in s:
            if s.count(arr[index][0]) >= k - chars:
                last_char = arr[index][0]
                last_char_included = k - chars
            else:
                included.add(arr[index][0])
            chars += min(s.count(arr[index][0]), k - chars)
        index += 1
        if chars >= k:
            break
    if k == 1:
        print(last_char)
    else:
        res = []
        last_chars = 0
        last_char_remained = s.count(last_char)
        for char in s:
            if char in included:
                if last_chars > 0:
                    if char > last_char:
                        min_last_chars = min(last_chars, last_char_included)
                        res.extend(last_char * min_last_chars)
                        last_char_included -= min_last_chars
                    else:
                        if last_char_included > last_char_remained - last_chars:
                            new_last_char_included = last_char_remained - last_chars
                            res.extend(last_char * (last_char_included - new_last_char_included))
                            last_char_included = new_last_char_included
                last_char_remained -= last_chars
                last_chars = 0
                res.append(char)
            elif char == last_char:
                last_chars += 1
        if last_chars > 0:
            if s[-1] > last_char:
                res.extend(last_char * min(last_chars, last_char_included))
            else:
                if last_char_included > last_char_remained - last_chars:
                    res.extend(last_char * (last_char_included - last_char_remained + last_chars))
        print(*res, sep='')
