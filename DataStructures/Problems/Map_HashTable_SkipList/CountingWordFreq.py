fred = dict()

string = 'Process finished with exit code 0 finished'
for piece in string.split():
    word = ''.join(c for c in piece if c.isalpha())
    if word:
        fred[word] = 1 + fred.get(word, 0)

max_word = ''
max_count = 0
for (w, c) in fred.items():
    if c > max_count:
        max_word = w
        max_count = c
print('The most frequent word is ', max_word)
print('Its number of occurrences is ', max_count)