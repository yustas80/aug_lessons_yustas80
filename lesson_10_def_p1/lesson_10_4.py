# Task_4_posled
#
# def logic_sec(pos_t):
#     res = ()
#     ind_p = 0
#     tm_p = 2
#
#     for item in range(1, pos_t[-1]):
#         if pos_t[ind_p] + item == pos_t[ind_p + 1]:
#             if pos_t[ind_p + 1] + item == pos_t[ind_p + 2]:
#                 if pos_t[ind_p + 2] + item == pos_t[ind_p + 3]:
#                     res = pos_t[-1] + item
#
#         if pos_t[ind_p] * item == pos_t[ind_p + 1]:
#             if pos_t[ind_p + 1] * item == pos_t[ind_p + 2]:
#                 if pos_t[ind_p + 2] * item == pos_t[ind_p + 3]:
#                     res = pos_t[-1] * item
#
#         if tm_p ** item == pos_t[ind_p + 1]:
#             if (tm_p + 1) ** item == pos_t[ind_p + 2]:
#                 if (tm_p + 2) ** item == pos_t[ind_p + 3]:
#                     res = int((len(pos_t) + 1) ** item)
#
#     return res
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

from typing import List
import string


def text_to_numbers(text: str) -> List[int]:
    for char in string.punctuation:
        text = text.replace(char, ' ')
    return list(map(int, text.split()))


def is_arithmetic_progression(numbers: List[int]) -> bool:
    if len(numbers) < 2:
        return False

    d = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i - 1] != d:
            return False
    return True


def is_geometric_progression(numbers: List[int]) -> bool:
    if len(numbers) < 2:
        return False

    q = numbers[1] // numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] // numbers[i - 1] != q:
            return False
    return True


def next_arihmetic_number(numbers: List[int]) -> int:
    d = numbers[1] - numbers[0]
    return numbers[-1] + d


def next_geometric_number(numbers: List[int]) -> int:
    q = numbers[1] // numbers[0]
    return numbers[-1] * q


def base(numbers: List[int]) -> int:
    if is_arithmetic_progression(numbers):
        return next_arihmetic_number(numbers)

    if is_geometric_progression(numbers):
        return next_geometric_number(numbers)

    return None


def main():
    text = input("Enter a list of numbers separated by a space: ")
    numbers = text_to_numbers(text)
    res = base(numbers)
    if res:
        print(f"The next number in the sequence is: {res}")
    else:
        print(f"The sequence is not defined by an arithmetic or geometric progression.")


if __name__ == "__main__":
    main()
