"""
Write a program to check whether two lists share no common elements.
share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
share common elements list1 = [1, 2, 3] list2 = [3, 4]
"""

def no_common_elements(list_a, list_b):
    for item in list_a:
        if item in list_b:
            return "Repeated"
    return "Unique"

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
print(no_common_elements(list_a, list_b))   # Unique

list_a = [1, 2, 3]
list_b = [3, 4]
print(no_common_elements(list_a, list_b))   # Repeated

### using sets

def no_common_elements2(list1,list2):
    if set(list1).intersection(set(list2)):
        return "Lists share common elements"
    else:
        return "Lists do NOT share any common elements"
    
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
print(no_common_elements(list1, list2))

list1 = [1, 2, 3]
list2 = [3, 4]
print(no_common_elements(list1, list2))