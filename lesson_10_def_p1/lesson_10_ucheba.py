# def draw(h, w, fill='*'):
#     for i in range(h):
#         print(fill * w)
#
#
# draw(5, 7)

# def human_ind(name, last_name, age):
#     human = {
#         'name': name,
#         'last_name': last_name,
#         'age': age
#
#     }
#     return human
#
#
# human_one = human_ind('Alex', 'Mig', 32)
#
# human_two = human_ind(age=41, name='Oleg', last_name='Bobko')
# print(human_one)
# print(human_two)

# def write(**args):
#     for key in args.keys():
#         print(key, '->', args.get(key))
#
# write(name='Alex', last='Ts', age=36)


# def draw_triangle (h, fill):
#     for i in range(h):
#         print(fill * (i + 1))
#
#
# arg = (7, 'X')
#
# draw_triangle(*arg)

def goods_info(*args, serial_n, price):
    goods = {
        'description': args,
        'serial_number': serial_n,
        'price': price
    }
    return goods


good_1 = goods_info('Comp', 'Good', '23-inch monitor', serial_n=123456789, price=25363)
good_2 = goods_info('Box', 'Bad', 'Unknown', serial_n=9876543210, price=245.36)
