# Task_1

import string

text = input('Input the TEXT: ')

d_c = {}

for i in string.punctuation:
    if i in text:
        text = text.replace(i, ' ').lower().split()
for word in text:
    d_c[word] = text.count(word)

print(d_c)
