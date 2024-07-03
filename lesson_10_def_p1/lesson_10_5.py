# # Task_5_doll
#
# def digits_words(num):
#
#     dic_dig = {
#         0: 'zero',
#         1: 'one',
#         2: 'two',
#         3: 'three',
#         4: 'four',
#         5: 'five',
#         6: 'six',
#         7: 'seven',
#         8: 'eight',
#         9: 'nine',
#         10: 'ten',
#         11: 'eleven',
#         12: 'twelve',
#         13: 'thirteen',
#         14: 'fourteen',
#         15: 'fifteen',
#         16: 'sixteen',
#         17: 'seventeen',
#         18: 'eighteen',
#         19: 'nineteen',
#         20: 'twenty',
#         30: 'thirty',
#         40: 'forty',
#         50: 'fifty',
#         60: 'sixty',
#         70: 'seventy',
#         80: 'eighty',
#         90: 'ninety'
#     }
#
#     num_1 = int(num // 100)
#     num_2 = int(num % 100 % 10)
#     num_3 = int(num % 100)
#     num_4 = int(num % 100 - num_2)
#     num_5 = int(num % 100 % 10 % 1 * 100 / 10 * 10)
#     num_6 = int(num_5 % 10)
#
#
#     res = list()
#
#     if 0 < num_1 < 10:
#         res.append(dic_dig.get(num_1) + ' ' + 'hundred')
#     if 9 < num_3 < 20:
#         res.append(dic_dig.get(num_3) + ' ' + 'dollars')
#     if num_4 >= 20:
#         res.append(dic_dig.get(num_4))
#         if num_2 > 0:
#             res.append(dic_dig.get(num_2) + ' ' + 'dollars')
#     if 0 < num_5 < 20:
#         res.append(dic_dig.get(num_5) + ' ' + 'cents')
#     if num_5 >= 20:
#         num_5 = num_5 - num_6
#         res.append(dic_dig.get(num_5))
#         if num_6 > 0:
#             res.append(dic_dig.get(num_6) + ' ' + 'cents')
#     if num_5 == 0:
#         res.append(dic_dig.get(num_5) + ' ' + 'cents')
#
#     return res
#
#
# num = float(input('Enter the number of USD: '))
#
# print('You have ==> ', *digits_words(num))

from num2words import num2words

money = input('Enter the amount of money: ')

first_part, second_part = money.split(',')

first_part = int(first_part)
second_part = int(second_part)

first_part = num2words(first_part, lang='uk')
second_part = num2words(second_part, lang='uk')

print(f'{first_part} dollars and {second_part} cents.')

