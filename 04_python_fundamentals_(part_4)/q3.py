'''
Create a class Student with private attributes _name, _roll_no, and _marks.
Provide getter and setter methods with validation 
- marks cannot be negative,
- roll number has to be between 1 & 100,
- name cannot be empty).
'''

class Student:
    def __init__(self,name,roll_no,marks):
        if name.strip() == "":
            print("Name cannot be empty.")
            return
        self._name=name
        if roll_no not in range(1,101):
            print("Roll number must be between 1 and 100.")
            return
        self._roll_no=roll_no
        if marks < 0:
            print("Marks cannot be negative.")
        self._marks=marks
        
    def set_name(self,name):
        if name.strip() == "":
            print("Name cannot be empty.")
            return
        self._name=name
        
    def set_roll_no(self,roll_no):
        if roll_no not in range(1,101):
            print("Roll number must be between 1 and 100.")
            return
        self._roll_no=roll_no
        
    def set_marks(self,marks):
        if marks < 0:
            print("Marks cannot be negative.")
        self._marks=marks

    def get_name(self):
        return self._name
    
    def get_roll_no(self):
        return self._roll_no
    
    def get_marks(self):
        return self._marks
    
    def get_details(self):
        print(f"Name: {self._name}, Roll No: {self._roll_no}, Marks: {self._marks}")
        
s = Student("SSB",95,45)
s.set_name("OM")
print(s.get_roll_no())
s.get_details()