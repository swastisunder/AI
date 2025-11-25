'''
Print multiplication table for any number using while loop.
'''

num = int(input("Enter a number: "))

i = 1
while i<=10:
    print(f"{num} * {i} = {num*i}")
    i=i+1