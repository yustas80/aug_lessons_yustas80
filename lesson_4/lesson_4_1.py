# Task_1

flat_num = int(input('Please enter flat number (1-144) - '))

ent = 4
floor = 9
fl_floor = 4
flat_ent = ent * floor
max_num = ent * flat_ent

if flat_num < 1 or flat_num > max_num:
    print('Wrong flat number.')
else:
    res_ent = (flat_num - 1) // flat_ent + 1
    res_fl = (flat_num - 1) % flat_ent // fl_floor + 1
    res_flat = (flat_num - 1) % fl_floor + 1

    print(f'Entrance - {res_ent}, Floor - {res_fl}, Flat number - {res_flat}')

