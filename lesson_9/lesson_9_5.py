# Task_5

import string

str_1 = 'Do you have any questions?'

str_2 = 'No. We do not have any questions.'

for i in string.punctuation:
    if i in str_1:
        str_1 = set(str_1.replace(i, ' ').lower().split())
    elif i in str_2:
        str_2 = set(str_2.replace(i, ' ').lower().split())

comm_word = str_1 & str_2

print(f'Longest unique word in two sentences - {max(comm_word, key=len).title()}')
