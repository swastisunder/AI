'''
Write a function to return the count the number of digits in a number.
'''

num = int(input("Enter a number : "))

'''
def count_digits(num):
    return len(str(num))
'''

def count_digits(num):
    if num == 0:
        return 1
    if num < 0:
        num = -num
    count = 0
    while (num>0):
        num //= 10
        count+=1
    return count


print(count_digits(num))