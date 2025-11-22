"""
Ask the user for a string and print:
• All unique characters
• The count of unique characters
"""

str = input("Enter a string : ")

unique = []

for i in str:
    if str.count(i) == 1:
        unique.append(i)
        
print(unique)
print(len(unique))