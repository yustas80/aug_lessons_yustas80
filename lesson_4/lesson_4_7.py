# Task_3_add

mont_num = int(input('Enter month number (1-12) - '))

if mont_num > 12 or mont_num < 1:
    print('Incorrect month number.')
elif mont_num == 2:
    print('This month have - 28 days or 29 (leap year)')
elif mont_num == 4 or mont_num == 6 or mont_num == 9 or mont_num == 11:
    print('This month have - 30 day')
else:
    print('This month have - 31 day')
