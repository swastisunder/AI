'''
Create an abstract class Employee with an abstract method calculate_salary().
Create subclasses Intern, FullTimeEmployee, and ContractEmployee that implement the method differently.
'''

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class ContractEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Testing
i = Intern(10000)
print("Intern Salary:", i.calculate_salary())

f = FullTimeEmployee(45000)
print("Full Time Salary:", f.calculate_salary())

c = ContractEmployee(500, 80)
print("Contract Employee Salary:", c.calculate_salary())
