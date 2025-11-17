'''
Design a program to continuously input a number from user & print if it is positive or negative until the user enters “Quit”.
'''

while (True):
    num = input("Enter a number or want to exit type quit : ")
    if(num=="quit"):
        break
    print(num)