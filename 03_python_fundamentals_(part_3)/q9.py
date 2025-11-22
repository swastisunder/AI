"""
Given a list, print all elements that appear more than once in the list.
[Hint - use sets]
"""

def print_duplicates(list):
    printed = []
    for i in list:
        if list.count(i) > 1 and i not in printed:
            print(i)
            printed.append(i)
            
            
print_duplicates([1,1,2,2,3])


# using set

def print_duplicates2(list):
    seen = set()
    duplicates = set()
    
    for i in list:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return duplicates

print(print_duplicates2([1,1,2,2,3]))