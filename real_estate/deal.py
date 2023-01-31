from abc import ABC


class Sell(ABC):
    def __init__(self, price_per_meters, discountable, convertable=False, *args, **kwargs):
        self.price_per_meters = price_per_meters
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"price per meters : {self.price_per_meters} , discountable: {self.discountable} ,"
              f"covertable: {self.convertable}")


class Rent(ABC):
    def __init__(self, initial_price, monthly_price, convertable=False, discountable=False, *args, **kwargs):
        self.discountable = discountable
        self.convertable = convertable
        self.monthly_price = monthly_price
        self.initial_price = initial_price
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"initial price : {self.initial_price} ,"
              f" monthly price: {self.monthly_price} ,"
              f"covertable: {self.convertable},"
              f"discountable : {self.discountable}")
