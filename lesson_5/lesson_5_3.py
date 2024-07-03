# Task_3

rad, x, y = float(input('Radius = ')), float(input('Point X = ')), float(input('Point Y = '))

hypo = (x ** 2 + y ** 2) ** 0.5

if hypo <= rad:
    print('The point at Circle')
else:
    print('The point does not at Circle')
