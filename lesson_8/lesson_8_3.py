# Task_3

contacts_ = {}

while True:
    name_ = input('Enter the name of the contact: ')
# _add_new_contact
    if name_ not in contacts_.keys():
        number_ = input('This is new contact. Enter number of contact: ')
        contacts_[name_] = number_
        print(contacts_)
# _see_if_in_contacts
    elif name_ in contacts_.keys():
        see_ = input('Do you want see it? (y/n): ')
        if see_ == 'y':
            print(contacts_.get(name_))
# _change_number
        elif see_ == 'n':
            change_ = input('Do you want change the number? (y/n) ')
            if change_ == 'y':
                number_ = input('Enter the new number of the contact: ')
                contacts_[name_] = number_
                print(f'New contact {contacts_.items()}')
# _delete_name
            elif change_ == 'n':
                delete_ = input('Do you want delete the contact? (y/n): ')
                if delete_ == 'y':
                    del contacts_[name_]
                    print(contacts_)



