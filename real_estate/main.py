from user import User
from random import choice
from region import Region
from estate import Apartment, House, Store

FIRST_NAME = ['mahdi', 'mohammad', 'majid', 'reza']
LAST_NAME = ['mahdivi', 'mohammadi', 'majidi', 'rezayie']
MOBILE = ['09910904501', '09910904502', '09910904503', '09910904504', '09910904505']

if __name__ == "__main__":

    for mobile in MOBILE:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    # for user in User.objects_list:
    #     print(f"{user.id} {user.fullname}")

    reg1 = Region(name='R1')

    apt1 = Apartment(has_elevator=True, has_parking=True, floor=2,
                     user=User.objects_list[0], area=80, room_count=3, built_year=1399,
                     region=reg1, address='qom shahrdary squad')

    apt1.show_description()

    house = House(has_yard=True, floor_count=3,
                  user=User.objects_list[2], area=110, room_count=4,
                  built_year=1401, region=reg1, address='qom jahad squad')
    house.show_description()

    store = Store(user=User.objects_list[1], area=70, room_count=1,
                  built_year=1370, region=reg1, address='qom jahad squad')
    store.show_description()