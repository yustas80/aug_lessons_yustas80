# Task_10

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print('Your matrix:')
print(*matrix, sep='\n')

i = 0
z = 0

while i < 4:
    y = sum(matrix[0+i])
    i += 1
    z += y

print(f'Matrix summa = {z}')
