# from typing import List
#
#
# def f_odd(x: List[int]):
#     res = []
#     for i in x:
#         if i % 2:
#             res.append(i)
#
#     return res
#
# x = [1, 4, 5, 8, 7, 9, 11, 14]
#
# print(f_odd(x))

# def create_phone_number(num):
#     res = ''
#     for i in range(num[0, 2]):
#         res.join(num)
#     return res


x = ['1', '2', '5', '6', '8', '1', '1', '1', '7', '1', '5']

res = '(' + ''.join(x[0: 3]) + ')' + ' ' + ''.join(x[4:7]) + '-' + ''.join(x[7:])

print(res)

# from typing import List
#
#
# def is_odd(item):
#     return item % 2 and item > 0
#
#
# def is_neg(item):
#     return item < 0
#
#
# def filter_x(x: List[int], func):
#     res = []
#     for item in x:
#         if func(item):
#             res.append(item)
#     return res

# print(filter_x(x, is_odd))
# print(filter_x(x, is_neg))
#
# print(filter_x(x, lambda item: item % 2 == 1 and item > 0))
# print(filter_x(x, lambda item: item < 0))
