# FILE

from typing import List
import string
import pprint


def txt_to_file(txt):
    return open(txt, 'r', encoding='utf-8')


def expenses_by_category(arg):
    exp_by_cat = {}
    for item in arg:
        item = item.split()
        *_, money, category = item
        money = float(money.replace('$', ''))

        exp_by_cat[category] = exp_by_cat.get(category, 0) + money

    return exp_by_cat


def exp_usr(arg):
    exp_by_usr = {}
    for line in arg:
        line = line.split()
        _, *name, money, category = line
        name = ' '.join(name)
        money = float(money.replace('$', ''))
        exp_by_usr[name] = exp_by_usr.get(name, 0) + money

    return exp_by_usr


def name_buy(arg):
    buy_d = {}
    for line in arg:
        line = line.split()
        _, *name, money, category = line
        name = ' '.join(name)
        buy_d[name] = buy_d.get(name, 0) + 1

    return buy_d


fm_name = input('Input family member name: ')

a = expenses_by_category(txt_to_file('hw_10_test.txt'))
print('1. Amount of family purchases by category in month:')
for key, value in a.items():
    print(f'{key} -> {str(a[key]).replace('[', '').replace(']', '')} dollars')
b = exp_usr(txt_to_file('hw_10_test.txt'))
print('2. Amount of purchases for each family member in month:')
for key, value in b.items():
    print(f'{key} -> {str(b[key]).replace('[', '').replace(']', '')} dollars')
c = name_buy(txt_to_file('hw_10_test.txt'))
print('3. Count of purchases for each family member in month:')
for key, value in c.items():
    print(f'{key} -> {str(c[key]).replace('[', '').replace(']', '')} purchases')


print(f'{fm_name} spent {b.get(fm_name):.2f} dollars and made {c.get(fm_name)} purchases in a month.')



#
#
#
# for text_line in file:
#     exp_name = {}
#     text_line = text_line.split()
#     num, *name, money, category = text_line
#     money = float(money.replace('$', ''))
#     exp_name[str(name).join(name)] = exp_name.get(category, money)
#     # return exp
#     print(exp_name)
#
# for text_line in file:
#     exp_category = {}
#     text_line = text_line.split()
#     num, *name, money, category = text_line
#     money = float(money.replace('$', ''))
#     exp_category[category] = exp_category.get(category, money)
#     # return exp
#     print(exp_category)
#
#
#
# def file_to_dict(tmp):
#     file_dict = {}
#     for line in file:
#         item = line.split()
#
#         id = item[0]
#         cat = item[-1]
#         name = ' '.join(item[1: -2])
#         amount = float(item[-2].replace('$', ''))
#         file_dict[id] = {
#             'name': name,
#             'amount': amount,
#             'category': cat
#         }
#
#     return file_dict
