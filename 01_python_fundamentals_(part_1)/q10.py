'''
Take a decimal number as input (like 45.78 ) and output its:
• integer part - 45
• fractional part - .78
'''

num = input("Enter a number : ")
parts = num.split(".")

print("Integer part -", parts[0])
print("Fractional part -", parts[1])