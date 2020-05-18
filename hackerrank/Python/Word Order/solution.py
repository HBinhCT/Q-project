from collections import OrderedDict

count_word = OrderedDict()
for _ in range(int(input())):
    word = input()
    count_word[word] = count_word.get(word, 0) + 1
print(len(count_word))
print(*count_word.values())
