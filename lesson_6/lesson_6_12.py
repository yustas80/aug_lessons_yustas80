# Task_12

s_dia = int(input('Please enter last range number: '))

lst = []

for var in range(2, s_dia+1):
    for temp in range(2, var):
        if var % temp == 0:
            break
    else:
        lst.append(var)

print(f'Simple numbers in range (1-{s_dia}) - {lst}')