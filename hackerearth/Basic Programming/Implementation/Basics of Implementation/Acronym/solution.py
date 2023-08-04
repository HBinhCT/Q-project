k = int(input())
disliked_words = set(input().strip() for _ in range(k))
n = int(input())
sentence = input().strip()
acronym = ''
for word in sentence.split():
    if word.lower() not in disliked_words:
        acronym += word[0].upper() + '.'
print(acronym[:-1])
