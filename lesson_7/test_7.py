# Task
#
# data = [
#     '1 Bob Simson 19.58$ decorations',
#     '2 Mary 66.7$ food',
#     '3 Mary 98.91$ toys',
#     '4 Aleksa 72.29$ drinks'
#     '5 Maria Simson 84.48$ food'
#     '6 Aleksa 100.41$ accessories'
#     '7 Mary 19.9$ accessories'
#     '8 Bob Simson 83.88$ drinks'
#     '9 Bob Simson 58.21$ instruments'
#     '10 Maria Simson 20.61$ accessories'
# ]
#
# res = sum(float(line.split()[-2].replace('$', '')) for line in data if 'food' in line.lower())
#
# print('Food cost = ', res, '$')

n = int(input('Input n: '))
i = 1
j = 1

while i <= n:
    j = 1
    while j <= i:
        print(f'{' ' * (n - j)}{'*' * j}')
        j += 1
    print()
    i += 1




