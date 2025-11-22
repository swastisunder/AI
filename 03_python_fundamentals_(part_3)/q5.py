std_info = {
    "Swasti": 90,
    "Nupur": 100,
    "Ganesh": 50,
    "OM": 90
}

while True:
    operation = input("""
A - Add a student
B - Update marks
C - Search for a student
D - Display all students and marks
E - Exit

Choose an option: """).upper()

    if operation == "A":
        name = input("Enter student name: ")
        if name in std_info:
            print("Student already exists")
            continue
        marks = int(input("Enter the marks: "))
        std_info[name] = marks

    elif operation == "B":
        name = input("Enter student name: ")
        if name not in std_info:
            print("Student does not exist")
            continue
        marks = int(input("Enter new marks: "))
        std_info[name] = marks

    elif operation == "C":
        name = input("Enter student name: ")
        if name not in std_info:
            print("Student does not exist")
            continue
        print(f"Student: {name}, Marks: {std_info[name]}")

    elif operation == "D":
        for name, marks in std_info.items():
            print(f"Name: {name} | Marks: {marks}")

    elif operation == "E":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
