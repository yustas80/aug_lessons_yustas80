# Task_2

year_num = int(input('Enter year number - '))

if year_num < 1:
    print('Wrong year number')
elif year_num % 4 == 0 and year_num % 100 != 0 or year_num % 400 == 0:
    print('This year Leap')
else:
    print('This year not leap')



