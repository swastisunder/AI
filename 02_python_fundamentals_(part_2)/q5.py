'''
Write a function to return the sum of digits of a number.
'''

num = int(input("Enter a number : "))

def sum_of_digits(num):
    sum = 0
    while num>0:
        last = num % 10
        sum += last
        num //= 10
        
    return sum

print(sum_of_digits(num))