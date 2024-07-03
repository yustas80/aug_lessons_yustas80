# Task_3

str_s = int(input('Enter start line - '))
str_f = int(input('Enter finish line - '))
move = int(input('Enter move - '))

while str_s <= str_f:
    line = ''
    st_a = 1
    while st_a <= move:
        if str_s > str_f:
            break
        line += str(str_s) + ' '
        str_s += 1
        st_a += 1
    print(line)

