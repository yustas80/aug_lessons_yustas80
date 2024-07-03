# Task_3

side_a, side_b, side_c = map(int, input('Enter the sides of triangle: ').split())

if side_a + side_b > side_c or side_b + side_c > side_b or side_a + side_c > side_b:
    print('Triangle Exist')
elif side_a + side_b <= side_c or side_b + side_c <= side_a or side_a + side_c <= side_b:
    print('Triangle Do Not Exist')
