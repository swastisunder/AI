'''
Let's create a Simple Calculator that performs arithmetic operations.
Create a function calculator(a, b, operation) that performs addition, subtraction, multiplication, or division based on the operation parameter.

The operation parameter can have values '+', '-', '*', and '/'.
'''

a= float(input("Enter first number : "))
b= float(input("Enter second number : "))
oper = input("Enter the operation (+,-,*,/)")

def cal(a,b,oper):
    if(oper=='+'):
        return a+b
    elif(oper=='-'):
        return a-b
    elif(oper=='*'):
        return a*b
    elif(oper=='/'):
        if(b==0):
            return "Error: Division by zero"
        return a/b
    else:
        return "invalid operation"
    
print(cal(a,b,oper))