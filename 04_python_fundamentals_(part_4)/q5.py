'''
Create a base class Vehicle with attributes like brand and model.
Create two subclasses Car and Bike that add extra attributes — seats (in Car) and engine_cc (in Bike).
'''

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def get_det(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Seats: {self.seats}")


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def get_det(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Engine CC: {self.engine_cc}")


# Testing
c = Car("Hyundai", "Verna", 5)
c.get_det()

b = Bike("Royal Enfield", "Continental GT 650", 647.95)
b.get_det()
