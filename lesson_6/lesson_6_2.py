# Task_2

n = int(input('Enter the end of range: '))

summa = []

for count in range(1, n):
    if count % 2:
        summa.append(count)

print(f'Summa = {sum(summa)}')
