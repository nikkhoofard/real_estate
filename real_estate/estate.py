from abc import abstractmethod, ABC


class EstateAbstract(ABC):
    def __init__(self, user, area, room_count, built_year, region, address,
                 *args, **kwargs):

        self.user = user
        self.area = area
        self.room_count = room_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)

    @abstractmethod
    def show_description(self):
        pass


class Apartment(EstateAbstract):
    def __init__(self, has_elevator, has_parking, floor, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args, **kwargs)
        
    def show_description(self):
        print(f"Apartment id : {self.id} seller : {self.user.fullname} area: {self.area}")
     

class House(EstateAbstract):
    def __init__(self, has_yard, floor_count, *args, **kwargs):
        self.has_yard = has_yard
        self.floor_count = floor_count
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"House id : {self.id} seller: {self.user.fullname} area: {self.area}")


class Store(EstateAbstract):
    def show_description(self):
        print(f"Store id : {self.id}seller: {self.user.fullname} area: {self.area}")
