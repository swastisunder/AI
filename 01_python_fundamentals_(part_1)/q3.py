'''
Ask the user to enter two integers and one float. Convert them all to floats
and print their average.
'''

int_num_1 = int(input("Enter integer number 1 : "))
int_num_2 = int(input("Enter integer number 2 : "))
float_num_1 = float(input("Enter float number 1 : "))

average = (int_num_1 + int_num_2 + float_num_1) / 3

print(f"Average of {int_num_1}, {int_num_2} and {float_num_1} is : {average}")
