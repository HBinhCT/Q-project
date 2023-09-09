from re import search

message = input().strip()
if search("l.*o.*v.*e", message):
    print("I love you, too!")
else:
    print("Let us breakup!")
