# Task 2

a = input('a = ')
b = input('b = ')
c = input('c = ')
d = input('d = ')
e = input('e = ')

a = float(a)
b = float(b)
c = float(c)
d = float(d)
e = float(e)

x = min(a, b, c, d, e)

y = max(a, b, c, d, e)

z = sum([a, b, c, d, e]) / len([a, b, c, d, e])

print(f'Min = {x}')
print(f'Max = {y}')
print(f'AVG = {z}')

print('Have a Nice Day!')
