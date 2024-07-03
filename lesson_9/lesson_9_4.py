# Task_4

friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}

lst_fr = list(friendships.keys())

while True:
    ind_1 = int(input('Enter the first friend (1-4) - '))
    ind_2 = int(input('Enter the second friend (1-4) - '))
    if ind_1 <= 0 or ind_1 >= 5:
        print('Enter correct number first friend.')
    elif ind_2 <= 0 or ind_2 >= 5:
        print('Enter correct number second friend.')
    else:
        print(f'Mutual friends {lst_fr[ind_1-1]} and {lst_fr[ind_2-1]} is = '
              f'{friendships.get(lst_fr[ind_1-1]) & friendships.get(lst_fr[ind_2-1])}')





# Task 4
# friendships = {
#     "user1": {"user2", "user3", "user4"},
#     "user2": {"user1", "user3"},
#     "user3": {"user1", "user2", "user4"},
#     "user4": {"user1", "user3"}
# }
#
# user_1 = input('Enter user1: ')
# user_2 = input('Enter user2: ')
#
# friends_1 = friendships.get(user_1, set())
# friends_2 = friendships.get(user_2, set())
#
# mutual_friends = friends_1 & friends_2
# mutual_friends = mutual_friends or 'No mutual friends'
#
# print(mutual_friends)
#
#
# users = []
# for _ in range(10):
#     user = input('Enter user: ')
#     users.append(friendships.get(user, set()))
#
# mutual_friends = set.intersection(*users)