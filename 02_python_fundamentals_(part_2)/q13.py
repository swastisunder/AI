'''
Count vowels in a word using for
'''

str = "aeioulll"
count = 0
for i in str:
    if i in "aeiou":
        count+=1
        
print(count)