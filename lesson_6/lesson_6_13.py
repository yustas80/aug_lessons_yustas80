# Task_13

max_star = int(input('Max Length - '))
min_star = int(input('Min Length - '))

dot = input('Enter symbol - ')

for i in range(max_star, min_star, -2):
    lne = (max_star - i) // 2
    print(' ' * lne + dot * i)

for i in range(min_star, max_star + 1, 2):
    lne = (max_star - i) // 2
    print(' ' * lne + dot * i)
