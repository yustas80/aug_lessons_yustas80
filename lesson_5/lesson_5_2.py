# Task_2
number = list(input('Enter ticket number (6-digits) = '))

print(number)

res = 'Number is Palindrome' if number == number[::-1] else 'Number is NOT Palindrome'

print(res)
