# Task_6

text = 'catCatcatcatcat'
word = 'cat'

for word in text:
    if text.count(word) > 1:
        text = text.replace(word, '', 1).lower()

print(f'{text}')

