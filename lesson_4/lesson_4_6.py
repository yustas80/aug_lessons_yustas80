# Task_2_add

buy_am = float(input('Введить сумму покупки - '))

if buy_am <= 0:
    print('Некорректна сумма.')
elif buy_am > 1000:
    print(f'Вітання! Ви отримуєте знижку 10% {buy_am * 0.9}')
else:
    print(f'Сума вашої покупки {buy_am}.')

print('Гарного дня!')
