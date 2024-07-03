# Task_4_add

grade = int(input('Rate the Service (1-5) - '))

if grade > 5 or grade < 1:
    print('Wrong grade.')
elif grade == 5:
    print('Great!')
elif grade == 4:
    print('Good.')
elif grade == 3:
    print('Normal.')
elif grade == 2:
    print('Bad.')
else:
    print('Terrible!')
