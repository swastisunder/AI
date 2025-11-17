'''
Write a program to swap values of two numbers entered by the user.
'''

num_1 = int(input("Enter number 1 : "))
num_2 = int(input("Enter number 2 : "))

# temp = num_1
# num_1 = num_2
# num_2 = temp

num_1, num_2 = num_2, num_1

print(f"number 1 is : {num_1}")
print(f"number 2 is : {num_2}")