from user import User
from random import choice
from region import Region
from estate import Apartment, House, Store
from advertisment import ApartmentRent, ApartmentSell,\
    HouseRent, HouseSell, StoreRent, StoreSell

FIRST_NAME = ['mahdi', 'mohammad', 'majid', 'reza']
LAST_NAME = ['mahdivi', 'mohammadi', 'majidi', 'rezayie']
MOBILE = ['09910904501', '09910904502', '09910904503', '09910904504', '09910904505']


def create_sample():

    for mobile in MOBILE:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    # for user in User.objects_list:
    #     print(f"{user.id} {user.fullname}")

    reg1 = Region(name='R1')

    apartment_sell = ApartmentSell(has_elevator=True, has_parking=True, floor=2,
                                   user=User.objects_list[0], area=80,
                                   room_count=3, built_year=1399,
                                   region=reg1, address='qom shahrdary squad',
                                   price_per_meters=12000, discountable=True,
                                   convertable=True)

    apartment_rent = ApartmentRent(has_elevator=True, has_parking=True, floor=2,
                                   user=User.objects_list[0],
                                   built_year=1393, region=reg1, area=80, room_count=2, convertable=False,
                                   initial_price=100, monthly_price=3.5, address="Some text...",
                                   )

    house_rent = HouseRent(
        has_yard=True, floor_count=1, user=User.objects_list[2], area=400,
        room_count=6, built_year=1370, region=reg1, address='Some text ...',
        initial_price=130, monthly_price=5.5, convertable=False
    )

    house_sell = HouseSell(
        has_yard=True, floor_count=1, user=User.objects_list[2], area=400,
        room_count=6, built_year=1370, region=reg1, address='Some text ...',
        price_per_meters=20, discountable=False, convertable=False
    )

    print("#" * 20, "\t samples created \t", "#" * 20)