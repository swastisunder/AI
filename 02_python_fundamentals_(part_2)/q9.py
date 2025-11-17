'''
Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.
'''

import math

def is_prime(num):
    if(num<2):
        return False
    if(num==2):
        return True
    
    prime = True
    
    for i in range(2,int(math.sqrt(num)+1)):
        if(num%i==0):
            prime =False
            break
    
    return prime

print(is_prime(6))