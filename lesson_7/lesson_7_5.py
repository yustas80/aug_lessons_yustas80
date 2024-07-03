# Task_5

import string

text = input("Input some text: ").lower()

for i in string.punctuation:
    if i in text:
        text = text.replace(i, ' ')

x = text.split()

print(f'Longest word in text - {max(x, key=len)}')
