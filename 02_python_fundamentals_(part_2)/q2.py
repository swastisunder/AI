'''
Write a function that takes two integers a and b and prints all even numbers between them (inclusive).
'''

a = int(input("Enter starting number : "))
b = int(input("Enter ending number : "))

def even_numbers(a,b):
    if a % 2 != 0:
        a+=1
    
    for i in range(a,b+1,2):
        print(i)

even_numbers(a,b)