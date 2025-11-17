'''
Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and compute simple interest:
SI = (P * R * T)/100
'''

P = float(input("Enter P : "))
R = float(input("Enter R : "))
T = float(input("Enter T : "))

si = (P * R * T)/100

print(f"Simple Interest is : {si}")
