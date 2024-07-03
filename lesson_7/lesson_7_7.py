# Task_7

# text = '</b> <head> Hello,<div id=rcnt style=clear:both;position:relative;zoom:1> World! <div>You is </div>Great!'
#
# res = ''
#
# for i in range(len(text)):
#     if text[i] == '<':
#         stop = True
#     elif text[i] == '>':
#         stop = False
#     elif stop == False:
#         res += text[i]
#
# print(f' Clean text: {res.replace('  ', ' ')}')

# Task_7

text = '</b> <head> Hello,<div id=rcnt style=clear:both;position:relative;zoom:1> World! <div>You is </div>Great!'

res = ''
i = 0

while i < len(text):
    if text[i] == '<':
        stop = True
    elif text[i] == '>':
        stop = False
    elif stop == False:
        res += text[i]
    i += 1

print(f' Cleen text: {res.replace('  ', ' ')}')