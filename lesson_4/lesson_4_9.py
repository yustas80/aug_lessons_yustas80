# Task_5_add

height = float(input('Please, enter your height (m): '))

weight = float(input('Please, enter your weight (kg): '))

index = weight / height ** 2

if weight <= 0 or height <= 0:
    print('Wrong Height/weight.')
elif index >= 30:
    print(f'Your body mass index {index:.2f} - Obesity.')
elif index >= 25:
    print(f'Your body mass index {index:.2f} - Overweight.')
elif index >= 18.5:
    print(f'Your body mass index {index:.2f} - Normal weight.')
else:
    print(f'Your body mass index {index:.2f} - Underweight.')

print('Have a nice day!')





