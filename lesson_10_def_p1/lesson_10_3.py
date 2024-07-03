# Task_3_poli
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def max_palindrom(start=100, stop=1000):
    res = []
    for i in range(start, stop):
        for j in range(i, stop):
            if is_palindrome(str(i * j)):
                res.append((i * j, i, j))

    return max(res, key=lambda tpl: tpl[0])


print(max_palindrom())

# def max_palindrom(ran_1, ran_2):
#     palindroms = []
#     m_pal = {}
#
#     for item_1 in range(ran_2, ran_1, -1):
#         for item_2 in range(item_1, ran_1, -1):
#             tem_p = item_1 * item_2
#             res = str(tem_p)
#             if res == res[::-1]:
#                 palindroms.append(res)
#                 m_pal = max(list(map(int, palindroms)))
#     if not m_pal:
#         return 'No palindroms.'
#
#     return m_pal
#
#
# start_ = int(input('Input range start ==> '))
# finish_ = int(input('Input range finish ==> '))
#
# print(f'Max palindrom in range "{start_}" - "{finish_}" ==> ', max_palindrom(start_, finish_))
