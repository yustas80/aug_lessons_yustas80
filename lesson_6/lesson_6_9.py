# Task_9

month_count = int(input('Enter month count: '))

salary_count = []

i = 1

if month_count < 1:
    print('Go to work!')
else:
    while i < month_count+1:
        tmp = float(input(f'Enter salary for {i} month - '))
        salary_count.append(tmp)
        i += 1

print(f'Your AVG salary = {sum(salary_count) / len(salary_count):.2f}')