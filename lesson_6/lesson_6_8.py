# Task_8

from random import randint

x = int(input('Enter list start: '))
y = int(input('Enter list finish: '))
z = int(input('Enter range of random: '))

lst_1 = [randint(x, y) for i in range(z)]
lst_2 = [item * 2 for item in lst_1]

lst_1.extend(lst_2)

print(lst_1)
