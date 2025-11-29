'''
Write a program that tries to open 'data.txt' in read mode. If the file does not
exist, catch the exception and print "File not found!".
'''

try:
    with open('data.txt','r')as f:
        print(f.read())
except:
    print("File not found!")