def solve(N, keyboard, word):
    # Write your code here
    word = set(word)
    for i in keyboard:
        row = set(i)
        if word.issubset(row):
            return 1
    return 0


N = int(input())
keyboard = []
for _ in range(N):
    keyboard.append(input())
word = input()

out_ = solve(N, keyboard, word)
print(out_)
