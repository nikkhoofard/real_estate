from user import User
from random import choice

FIRST_NAME = ['mahdi', 'mohammad', 'majid', 'reza']
LAST_NAME = ['mahdivi', 'mohammadi', 'majidi', 'rezayie']
MOBILE = ['09910904501', '09910904502', '09910904503', '09910904504', '09910904505']

if __name__ == "__main__":

    for mobile in MOBILE:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in User.objects_list:
        print(f"{user.id} {user.fullname}")
