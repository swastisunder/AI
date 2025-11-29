'''
Create a class Person that allows the constructor to work with:
• name only
• name + age
• name + age + address
As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.
'''

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


# Different ways of object creation
p1 = Person("Alice")
p1.get_details()

p2 = Person("Bob", 25)
p2.get_details()

p3 = Person("Charlie", 30, "Delhi")
p3.get_details()
