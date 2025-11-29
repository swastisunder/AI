'''
Create a program that:
1. Opens a file "log.txt" in append mode
2. Adds a new log entry (like "Program run successfully")
3. Opens the file in read mode and prints all logs
'''

with open('log.txt','a')as f:
    str = input("Enter any log: ")
    f.write(f"{str}\n")
    
with open('log.txt','r')as f:
    print(f.read())