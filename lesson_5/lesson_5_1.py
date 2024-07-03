# Task_1

ticket = input('Enter ticket number (XXXX) = ')

ticket = list(map(int, ticket))

if len(ticket) % 2:
    print('Wrong ticket number')
else:
    mid = len(ticket) // 2
    f_half = ticket[:mid]
    s_half = ticket[mid:]

    if sum(f_half) == sum(s_half):
        print('You have Lucky ticket!!!')
    else:
        print('Sorry. Better luck next time!')
