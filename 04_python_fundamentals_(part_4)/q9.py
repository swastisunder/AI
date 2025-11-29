'''
Create the following classes:Herbivore, Carnivore, Omnivore with some
attributes & methods. Then create a class Bear that inherits from all the above 
classes to showcase how multiple inheritance works
'''

class Herbivore:
    def __init__(self):
        self.food_type = "Plants"
        
    def eat_plants(self):
        print("Eats grass, fruits, and leaves.")
        
class Carnivore:
    def __init__(self):
        self.food_type = "Meat"
        
    def eat_meat(self):
        print("Hunts and eats meat.")
        
class Omnivore:
    def __init__(self):
        self.food_type = "Both Plants and Meat"
        
    def eat_both(self):
        print("Can eat both plants and meat.")
        
class Bear(Herbivore,Carnivore,Omnivore):
    def __init__(self):
        Herbivore.__init__(self)
        Carnivore.__init__(self)
        Omnivore.__init__(self)
    
    def show_info(self):
        print(f"Food Type (from Omnivore): {self.food_type}")
        
# Testing
b = Bear()

b.show_info()

b.eat_plants()   # from Herbivore
b.eat_meat()     # from Carnivore
b.eat_both()     # from Omnivore