# # Task_4_posled
#
# def logic_sec(pos_t):
#     if len(pos_t) < 4:
#         return 'Need More Information'
#     if pos_t[1] - pos_t[0] == pos_t[2] - pos_t[1] == pos_t[3] - pos_t[2]:
#         return pos_t[-1] + pos_t[1] - pos_t[0]
#     if pos_t[2] / pos_t[1] == pos_t[3] / pos_t[2] == pos_t[4] / pos_t[3]:
#         return pos_t[-1] * (pos_t[2] / pos_t[1])
#     for i in range(1, pos_t[-1]):
#         if len(pos_t)**i == pos_t[-1] and (len(pos_t)-1)**i == pos_t[-2] and (len(pos_t)-2)**i == pos_t[-3]:
#             return (len(pos_t) + 1) ** i
#     return ' I don"t know sequence logic.'
#
#
# pos_t = []
# num_t = 1
# while len(pos_t) < 5:
#     a = int(input(f'Enter {num_t} number in sequence: '))
#     if a >= 0:
#         pos_t.append(a)
#         num_t += 1
#     else:
#         print('Wrong number!')
#     continue
#
# print('Next sequence number ==> ', logic_sec(pos_t))

from num2words import num2words

