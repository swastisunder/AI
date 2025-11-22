
# Python Fundamentals (Part3)

### Concepts : String, List, Tuple, Dictionary & Set

In this chapter we are going to dive deep into some of the not-so-simple data types of Python.

---

# **Strings**

## What is a String?

A string in Python is a sequence of characters enclosed in quotes:  
Strings are immutable, meaning once created, their contents can’t be changed directly.

### Function

We can use the built-in function to print the length of a string:

```python
word = 'Prime'
print(len(word)) # 5
```
````

### Concatenation

Just like we add numbers, we can concatenate (i.e. join) strings using the `+` operator.

```python
str1 = "Apna"
str2 = "College"
word = str1 + " " + str2
print(word)
```

### Loop on Strings

```python
s = "Python"
for ch in s:
    print(ch)
```

### Indexing in Strings

Index in a sequence represents the position value of individual characters.

```python
s = "Python"
print(s[0])     # 'P'
print(s[3])     # 'h'
print(s[-1])    # 'n'
```

---

# **Slicing in Strings**

General syntax:

```
string[start : end : step]
```

• start → inclusive
• stop → exclusive
• step → default = 1

Examples:

```python
s = "Python"
print(s[0:2])   # Py
print(s[2:])    # thon
print(s[:3])    # Pyt
print(s[::2])   # Pto
print(s[::-1])  # nohtyP
```

---

# **String Formatting**

String formatting inserts dynamic values inside a template string.

Two modern ways:

1. `.format()`
2. f-strings

### Using `.format()`

```python
name = "Rahul"
age = 25
text = "My name is {} and I am {} years old".format(name, age)
print(text)

"Coordinates: {1}, {0}".format("x", "y")
"Name: {n}, Age: {a}".format(n="Bob", a=30)
```

### Using f-strings

```python
name = "Rahul"
age = 25
text = f"My name is {name} and I am {age} years old"
print(text)

a = 5
b = 10
print(f"sum of {a} & {b} = {a + b}")
print(f"avg of {a} & {b} = {(a + b) / 2}")
```

---

# **Lists**

## What is a List?

• Ordered
• Mutable
• Allows duplicates
• Heterogeneous
• Written using `[]`

### Example:

```python
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))

my_list2 = [10, "Hello", 3.14, True, 10]
print(my_list2)
```

### List Indexing

```python
my_list = ["apple", "banana", "cherry"]
print(my_list[0])
print(my_list[1])
print(my_list[-1])
```

### Modify Elements

```python
my_list = [1, 2, 3, 4]
my_list[0] = 10
print(my_list)
```

### Slicing Lists

```python
numbers = [0,1,2,3,4,5,6,7,8,9]

print(numbers[2:5])
print(numbers[:4])
print(numbers[5:])
print(numbers[:])

print(numbers[::2])
print(numbers[1::3])
print(numbers[-5:-2])
```

---

# **List Methods**

```python
nums = [5, 2, 9]

print(len(nums))

nums.append(7)
nums.insert(1, 4)
nums.sort()
nums.reverse()
```

---

# **Loops on Lists**

### Printing elements:

```python
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)
```

### Linear Search:

```python
numbers = [5, 12, 7, 3, 18, 9]
x = 18
idx = 0

for num in numbers:
    if num == target:
        print(f"{x} found at index={idx}")
        break
    idx += 1
```

---

# **Tuples**

## What is a Tuple?

Ordered, Immutable, Allows duplicates, Heterogeneous.

### Example:

```python
tup = (10, 20, 30)
print(tup)
print(type(tup))

empty_tuple = ()
single_element_tuple = (42,)
```

### Indexing & Slicing

```python
t = (10, 20, 30, 40)
print(t[0])
print(t[-1])
print(t[1:3])
```

### Loop

```python
t = (10, 20, 30, 40)
for val in t:
    print(val)
```

### Sum using loop

```python
t = (5, 15, 25)
sum = 0
for val in t:
    sum += val
print("Sum:", sum)
```

### Tuple Methods

```python
t = (1, 2, 2, 3, 5)
print(t.index(2))
print(t.count(2))
```

---

# **Dictionaries**

## What is a Dictionary?

Unordered, Mutable, Key-value pairs.

### Example:

```python
my_dict = {
 "name": "Shradha",
 "age": 30,
 "city": "Delhi"
}
```

### Accessing

```python
student = {"name": "Bob", "age": 20}
print(student["name"])
```

### Dictionary Methods

```python
d = {
 "name": "Shradha",
 "subjects": ["math", "science", "physics"],
 "cgpa": 9.5
}

print(d.keys())
print(d.values())
print(d.items())
print(d.get("cgpa2"))

new_item = {"city": "Delhi"}
d.update(new_item)
print(d)
```

### Looping dictionary

```python
d = {
 "name": "Shradha",
 "subjects": ["math", "science", "physics"],
 "cgpa": 9.5
}

for key, value in d.items():
    print(key, value)
```

---

# **Sets**

## What is a Set?

Unordered, Unique elements, Mutable, No indexing.

### Example:

```python
my_set = {1, 2, 2, 2, 3}
print(my_set)
print(type(my_set))
print(len(my_set))

empty_set = set()
```

---

# **Set Methods**

```python
s = {10, 20, 30}
s.add(40)
s.remove(10)
print(s.pop())
s.clear()
```

### Union & Intersection

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A.intersection(B))
```

---
