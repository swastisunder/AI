
# 🐍 Python Fundamentals — Part 2

**Concepts:** Conditional Statements, Loops & Functions

---

## ✦ Conditional Statements

Conditional statements allow your program to make decisions based on **True/False** conditions.

### **1. `if` Statement**

Runs a block of code only if the condition is true.

```python
if age >= 18:
    print("you can vote")
    print("you can drive")
```

### **2. `else` Statement**

Runs when the `if` condition is false.

```python
if age >= 18:
    print("you can vote")
else:
    print("you can't vote")
```

### **3. `elif` Statement**

Used for multiple conditions.

```python
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Look")
elif color == "green":
    print("Go")
else:
    print("wrong color")
```

---

## ✦ Logical Operators

Used to combine conditions:

| Operator | Meaning                      |
| -------- | ---------------------------- |
| `and`    | Both conditions must be true |
| `or`     | At least one is true         |
| `not`    | Reverses a condition         |

Example:

```python
if age >= 13 and age < 18:
    print("teenager")
```

---

## ✦ Nested Conditionals

A conditional inside another conditional.

```python
if username == "admin" and password == "pass":
    print("log in successful!")
else:
    if username != "admin":
        print("wrong user name")
    else:
        print("wrong password")
```

---

## ✦ Ternary / One-line Conditions

```python
status = "Adult" if age >= 18 else "Not Adult"
```

---

## ✦ `match case` (Python 3.10+)

Alternative to long `if/elif` chains.

```python
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Look")
    case "green":
        print("Go")
    case _:
        print("wrong color")
```

---

# 🌀 Loops

Loops allow repeating a block of code.

## ✦ 1. `while` Loop

Runs **while condition is true**.

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### Infinite Loop (avoid)

```python
while True:
    print("Prime")
```

### Loop Control Statements

| Keyword    | Function               |
| ---------- | ---------------------- |
| `break`    | Stop loop completely   |
| `continue` | Skip current iteration |

Example:

```python
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
```

---

## ✦ 2. `for` Loop

Used to loop over sequences (string, list, range).

```python
for i in range(5):
    print(i)
```

### Looping over a string

```python
for ch in "Prime":
    print(ch)
```

### Checking membership

```python
if 'i' in "Prime":
    print("letter exists")
```

### Nested Loop

```python
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
```

---

# 🔢 `range()` Function

Used to generate numbers.

```python
range(start, stop, step)
```

Examples:

```python
range(5)          # 0–4
range(1, 6)       # 1–5
range(1, 10, 2)   # 1,3,5,7,9
```

---

# 🧩 Functions

Functions are reusable blocks of code.

### **Defining a function**

```python
def hello():
    print("hello from Prime")
```

### **Calling a function**

```python
hello()
```

### Parameters & Arguments

```python
def sum(a, b):
    print(a + b)

sum(5, 10)
```

### Return Statement

```python
def avg(a, b, c):
    return (a + b + c) / 3
```

---

## ✦ Default Parameters

```python
def sum(a, b=1):
    return a + b

print(sum(5))  # 6
```

*Note:* Default parameters must come last.

---

# ⚡ Lambda Functions

Short, one-line anonymous functions.

**Syntax:**

```
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x
print(square(5))
```

---

# 📝 Practice Problem Solutions

## **Set 1 — Conditionals**

### Multiple of 5

```python
num = int(input("enter number: "))
if num % 5 == 0:
    print("multiple of 5")
else:
    print("NOT a multiple of 5")
```

### Odd or Even

```python
num = int(input("enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## **Set 2 — Loops**

### Multiplication Table

```python
n = int(input("enter n: "))
for i in range(1, 11):
    print(i * n)
```

### Odd numbers using continue

```python
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
```

### Count vowels

```python
word = "artificial intelligence"
count = 0

for ch in word:
    if ch in "aeiou":
        count += 1

print("vowel count =", count)
```

### Sum of first n natural numbers

```python
n = int(input("enter n: "))
total = 0

for i in range(1, n+1):
    total += i

print("sum =", total)
```

---

## **Set 3 — Functions**

### Factorial

```python
n = int(input("enter n: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial =", fact)
```

### Largest of 3 numbers

```python
def get_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(get_largest(3, 10, 5))
```

---

# ⭐ Keep Learning & Keep Exploring!

---

If you want, I can also convert this into a **downloadable `.md` file** for you.
