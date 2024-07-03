# Task_3

dic_one = {1: 'one', 2: '$$$', 3:'GOOD', 4: 65, 5: 777, 6: 65}

res = 'All items in Dictionary is Unique!' if len(set(dic_one.values())) == len(dic_one) else ('We have not unique '
                                                                                               'elements in '
                                                                                               'Dictionary.')

print(res)
