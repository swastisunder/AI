"""
Ask the user for a string and check whether it is a palindrome or not.
A is a palindrome string which is same when we read it forward & backward.
Eg -
    “madam”, “racecar” etc.
"""

def is_palindrome(s):
    s=s.lower().replace(" ", "")
    return s==s[::-1]

user_input=input("Enter a String: ")
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')    