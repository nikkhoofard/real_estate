from estate import Apartment, House, Store
from deal import Sell, Rent


class ApartmentSell(Apartment, Sell):

    def show_details(self):
        self.show_description()
        self.show_price()


class ApartmentRent(Apartment, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()


class HouseSell(House, Sell):
    def show_details(self):
        self.show_description()
        self.show_price()


class HouseRent(House, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()


class StoreSell(Store, Sell):
    def show_details(self):
        self.show_description()
        self.show_price()


class StoreRent(Store,  Rent):
    def show_details(self):
        self.show_description()
        self.show_price()