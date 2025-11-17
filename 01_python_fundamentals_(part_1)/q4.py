'''
The user enters a string containing a number (e.g., "45" ). Convert it to:
• an integer
• a float
• a string again
Print all three values with their types.
'''

str_val = str(input("Enter a number : "))
int_val = int(str_val)
float_val = float(str_val)
str_again_val = str(str_val)

print(f"{int_val} is type of {type(int_val)}")
print(f"{float_val} is type of {type(float_val)}")
print(f"{str_again_val} is type of {type(str_again_val)}")