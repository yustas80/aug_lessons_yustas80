# Task_1

num = int(input('Enter fold number: '))
s_dia = int(input('Enter the start of range: '))
e_dia = int(input('Enter the end of range: '))
y = []

for item in range(s_dia, e_dia+1):
    if item % num == 0:
        y.append(item)

print(f'Fold numbers in range {s_dia} to {e_dia}: {y}')
