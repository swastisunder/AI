'''
Ask the user for a temperature in Celsius (string input). Convert it to ,float then calculate and print temperature in Fahrenheit.
Conversion formula: FahrenheitTemp = (CelsiusTemp * (9/5)) + 32
'''

temp_in_celsius = int(input("Enter temperature in Celsius : "))
temp_in_celsius = float(temp_in_celsius)
temp_in_fahrenheit = (temp_in_celsius * (9/5)) + 32

print(f"temperature in Fahrenheit is {temp_in_fahrenheit}")