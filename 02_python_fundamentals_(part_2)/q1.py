'''
Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
• If salary < 30,000 → 5%
• If salary is 30,000-70,000 → 15%
• If salary > 70,000 → 25%
'''

salary = int(input("Enter your salary: "))
    
if salary < 30000:
    tax = salary * 0.05
elif salary < 70000:
    tax = salary * 0.15
else:
    tax = salary * 0.25

print("Tax =", tax)
