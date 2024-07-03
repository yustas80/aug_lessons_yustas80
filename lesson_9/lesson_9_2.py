# Task_2

lst = []
i = 0
while i < 7:
    tmp = str(input('Input Something 7 times: '))
    lst.append(tmp)
    i += 1

set_l = len(set(lst))

print(f'Number of unique elements - {set_l}')
