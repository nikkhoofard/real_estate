from base import BaseClass


class Sell(BaseClass):
    def __init__(self, price_per_meters, discountable, convertable, *args, **kwargs):
        self.price_per_meters = price_per_meters
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)


class Rent(BaseClass):
    def __init__(self, initial_price, monthly_price, convertable, discountable, *args, **kwargs):
        self.discountable = discountable
        self.convertable = convertable
        self.monthly_price = monthly_price
        self.initial_price = initial_price
        super().__init__(*args, **kwargs)
