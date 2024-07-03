# Task_2
import string

name = input('Please, enter your NAME - ')

res = 'Your name is correct.' if name.istitle() and name.replace(' ', '').isalpha() else 'Your name incorrect'

print(res)
