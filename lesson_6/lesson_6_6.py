# Task_6

w_l = int(input('Enter Width: '))
h_l = int(input('Enter Length: '))

dot = input('Enter the symbol - ')

print(dot * w_l)

chk = w_l

for i in range(1, h_l-1):
    ln_1 = dot[chk % len(dot)]
    chk += 1
    print(f'{ln_1}{' ' * (w_l - 2)}{ln_1}')

print(dot * w_l)
