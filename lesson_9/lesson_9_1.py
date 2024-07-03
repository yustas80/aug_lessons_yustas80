# Task_1

lst = []
i = 0
while i < 5:
    tmp = str(input('Input Something: '))
    lst.append(tmp)
    i += 1

set_l = set(lst)

if len(lst) == len(set_l):
    print(f'All items in LIST{lst} are UNIQUE!')
else:
    print(f'Some elements in the list are not unique. :(')
