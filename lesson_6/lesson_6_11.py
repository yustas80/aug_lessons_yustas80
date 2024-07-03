# Task_11

from random import randint

fst = int(input('START - '))
sec = int(input('FINISH - '))
var = int(input('COUNT - '))

lst = [randint(fst, sec) for i in range(var)]

lst_r = []

for item in lst[::-1]:
    lst_r.append(item)

print(lst, lst_r, sep='\n')
