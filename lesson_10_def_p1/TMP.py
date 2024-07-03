# FILE

def txt_to_file(txt):
    return open(txt, 'r', encoding='utf-8')


def uni_parc(arg, n_f: str = 'cat'):
    """
    Calculate money by category, money by users, users purchase

    :param arg: file.txt
    :param n_f: cat - category of goods (Default),
                name - calculate amount by name,
                number - count purchases by name
    :return: dictionary
    """
    univ = {}
    for item in arg:
        item = item.split()
        _, *name, money, category = item
        money = float(money.replace('$', ''))
        name = ' '.join(name)
        if n_f == 'cat':
            univ[category] = univ.get(category, 0) + money
        if n_f == 'name':
            univ[name] = univ.get(name, 0) + money
        if n_f == 'number':
            univ[name] = univ.get(name, 0) + 1

    return univ


cat = uni_parc(txt_to_file('hw_10_test.txt'), 'cat')
print('1. Amount of family purchases by category in month:')
for key, value in cat.items():
    print(f'{key} -> {cat[key]:.2f} dollars')
name = uni_parc(txt_to_file('hw_10_test.txt'), 'name')
print('2. Amount of purchases for each family member in month:')
for key, value in name.items():
    print(f'{key} -> {name[key]:.2f} dollars')
number = uni_parc(txt_to_file('hw_10_test.txt'), 'number')

while True:
    fm_name = input('Family member name(Bob Simson, Maria Simson, Mary, Aleksa, Jack): ')
    print(f'>>> {fm_name} spent {name[fm_name]:.2f} dollars and made {number.get(fm_name)} purchases in a month. <<<')
