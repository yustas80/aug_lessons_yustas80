# Task_2

dict_e_u = {}

while True:
    word_e = input('Enter the word: ').lower()
# _add_new_words
    if word_e not in dict_e_u.keys():
        word_u = input('This is new word. Enter translation: ').lower()
        dict_e_u[word_e] = word_u
        dict_e_u[word_u] = word_e
        print(dict_e_u)
# _see_if_in_dict_e_u
    elif word_e in dict_e_u.keys():
        print(f'Translation - {word_e.title()} - {dict_e_u.get(word_e).title()}')
