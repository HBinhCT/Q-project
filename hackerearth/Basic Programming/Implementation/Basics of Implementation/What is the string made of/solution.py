dashes = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
}
string = input().strip()
ans = 0
for i in string:
    ans += dashes[i]
print(ans)
