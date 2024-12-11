class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        info = f'''Марка автомобиля: {self.make},
модель машины: {self.model}'''
        return info

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type


    def get_info(self):
        info = f'''Марка автомобиля: {self.make},
модель машины: {self.model},
вид топлива: {self.fuel_type}'''
        return info

make = 'BMW'
model = 'BMW X5'
fuel_type = 'бензин'

my_vehicle = Vehicle(make, model)
print(my_vehicle.get_info())

my_car = Car(make, model, fuel_type)
print(my_car.get_info())