"""
Input two lists of integers from the user. Merge them into one list and sort the result.
Eg - list1 = [1, 2, 7] , list2 = [2, 4, 5]
result = [1, 2, 3, 54, 5, 7]
"""

def merge_and_sorted_list(list1,list2):
    return sorted(list1+list2)

length1= int(input("Enter the length of first list: "))
list1=[]

for _ in range(length1):
    list1.append(int(input(f"Enter the {_} element for list 1: ")))
    
length2= int(input("Enter the length of first list: "))
list2=[]

for _ in range(length2):
    list2.append(int(input(f"Enter the {_} element for list 2: ")))

print(merge_and_sorted_list(list1,list2))