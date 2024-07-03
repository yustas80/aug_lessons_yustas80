# # Task_1
# salaries = []
#
# month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
#
# i = 0
#
# while i < len(month):
#     salary = int(input(f'Enter your salary in {month[i]} month:'))
#     if salary <= 0:
#         print('Salary cannot be negative or zero')
#         continue
#     salaries.append(salary)
#     i += 1
#
#
# min_salary = min(salaries)
# max_salary = max(salaries)
# avg_salary = sum(salaries) / len(salaries)
#
# min_month = month[salaries.index(min_salary)]
# max_month = month[salaries.index(max_salary)]
#
# print(f'Min salary: {min_salary}')
# print(f'Max salary: {max_salary}')
# print(f'Avg salary: {avg_salary:.2f}')
#
# print(f'Min salary: {min_salary} in {min_month} month')
# print(f'Max salary: {max_salary} in {max_month} month')

# # Task_2
#
# x = ['Hello', 123, 68.89]
#
# for item in x:
#     if isinstance(item, str | list | tuple):
#         print(*item, sep='\n')
#     else:
#         print(f'-{item}-')

# Task_3

# seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
#
# for i in range(10):
#     print(i+1)

width = 10
height = 7
symbols = '#'

print((symbols * width)[:width])

index = width
for i in range(1, height):
    char1 = symbols[index % len(symbols)]
    index += 1
    char2 = symbols[index % len(symbols)]
    index += 1
    print(f'{char1}{" " * (width - 2)}{char2}')

print((symbols * width)[index % len(symbols):width + index % len(symbols)])
