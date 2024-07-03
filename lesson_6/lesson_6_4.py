# Task_4

n = int(input('Input positive number - '))

f = 1

if n < 1 or n % 1 > 0:
    print('Wrong.')

for i in range(1, n+1):
    f = f * i

print(f'Factorial {n} = {f}')
