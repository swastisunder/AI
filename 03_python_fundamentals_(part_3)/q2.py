"""
Given a list of integers compute the average of all numbers in the list.
"""

list = [1,2,3,4,5,6,7,8,9,10]

def calculate_average(numbers):
    return sum(numbers)/len(numbers)

print("The average is:", calculate_average(list))    
