texts = []
words = {}
texts = input("Text: ").split()
for x in texts:
    frequency = words.get(x, 0)
    words[x] = frequency + 1

for x in words:
    print(f"{x} : {words[x]}")

words = list(words.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, words[x]))