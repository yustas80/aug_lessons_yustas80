# Task_4

exchange_ = {"UAH": 1, "USD": float(input('USD rate - ')), "EUR": float(input('EUR rate - ')),
             "GBP": float(input('GBP rate - '))}

while True:
    currency_1 = input('Input first currency (UAH, USD, EUR, GBP) - ').upper()
    currency_2 = input('Input second currency (UAH, USD, EUR, GBP) - ').upper()
    how_much = float(input('Input how many you want exchange - '))
    res = exchange_[currency_1] * how_much / exchange_[currency_2]
    print(f'CrossExchange {currency_1, '=>', currency_2} = {res:.2f}')