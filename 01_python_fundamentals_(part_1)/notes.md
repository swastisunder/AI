# 🐍 Python Fundamentals — Part 1

**Concepts:** Output, Input, Variables, Data Types & Operators

---

# ✦ Output in Python

The simplest thing Python can do is **print** output on the screen using the `print()` function.

### **Syntax**

```python
print("hello world")
print(3.14)
print(2 + 3)
print("hello world", "from PRIME")
```

### **Notes**

* Anything inside single or double quotes → **string**
* Multiple values inside `print()` are shown on the **same line**, separated with a space.

---

# ✦ Python Character Set

Python understands characters like:

1. **English letters:** `A–Z`, `a–z`
2. **Digits:** `0–9`
3. **Special symbols:** `+ - * / %` etc.
4. **Whitespaces & escape sequences:**

   * space
   * `\t` (tab)
   * `\n` (newline)
5. **All ASCII & Unicode characters**

---

# ✦ Variables

A variable is a **container** that stores data.

```python
name = "Shradha"
age = 30
PI = 3.14
```

### **Variable Naming Rules**

* Must start with **letter** or **underscore**
* Cannot start with digits
  ❌ `2name`
* Cannot use keywords
  ❌ `class = 10`

### **Important Notes**

* Python is **dynamically typed**
* Python is **case-sensitive**
  `age` ≠ `Age`
* Uses **indentation (4 spaces)** for code structure
* Keywords include:
  `if`, `for`, `while`, `else`, `in`, `def`, `class`, etc.

---

# ✦ Data Types

Python’s basic data types:

| Type       | Description      |
| ---------- | ---------------- |
| `int`      | Whole numbers    |
| `float`    | Decimal numbers  |
| `str`      | Strings          |
| `bool`     | `True` / `False` |
| `NoneType` | No value         |

Checking data type:

```python
type(x)
```

Example:

```python
x = 10
print(type(x))   # int

PI = 3.14
print(type(PI))  # float

name = "shradha"
print(type(name)) # str
```

---

# ✦ Type Conversion & Casting

### 1. **Implicit Type Conversion** (done automatically)

```python
a = 5
b = 3.0
print(a + b)  # result converted to float
```

### 2. **Explicit Type Casting**

Common functions:
`int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`

```python
x = 10
y = float(x)
z = str(x)
```

---

# ✦ Operators

Operators perform operations on values.

---

## **1. Arithmetic Operators**

| Operator | Meaning             |
| -------- | ------------------- |
| `+`      | Addition            |
| `-`      | Subtraction         |
| `*`      | Multiplication      |
| `/`      | Division            |
| `%`      | Modulus (remainder) |
| `**`     | Power               |

Example:

```python
a = 5
b = 10
print(a + b)
print(a ** b)
```

---

## **2. Relational Operators**

Used to compare values.

| Operator | Meaning       |
| -------- | ------------- |
| `==`     | Equal         |
| `!=`     | Not equal     |
| `>`      | Greater       |
| `<`      | Less          |
| `>=`     | Greater equal |
| `<=`     | Less equal    |

---

## **3. Assignment Operators**

| Operator | Meaning           |
| -------- | ----------------- |
| `=`      | Simple assign     |
| `+=`     | Add & assign      |
| `-=`     | Subtract & assign |
| `*=`     | Multiply & assign |
| `/=`     | Divide & assign   |
| `%=`     | Modulus assign    |
| `**=`    | Power assign      |

Example:

```python
x = 10
x += 5   # 15
x *= 2   # 30
```

---

## **4. Logical Operators**

| Operator | Meaning                   |
| -------- | ------------------------- |
| `and`    | True if both true         |
| `or`     | True if at least one true |
| `not`    | Reverses boolean          |

Truth table (simplified):

| A | B | A and B | A or B | not A |
| - | - | ------- | ------ | ----- |
| T | T | T       | T      | F     |
| T | F | F       | T      | F     |
| F | T | F       | T      | T     |
| F | F | F       | F      | T     |

---

# ✦ Operator Precedence

Order in which Python evaluates expressions:

1. `()` → Parentheses
2. `**` → Exponent
3. Unary: `+x`, `-x`, `~x`
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. Bitwise shifts: `<<`, `>>`
7. Bitwise AND: `&`
8. Bitwise XOR: `^`
9. Bitwise OR: `|`
10. Comparisons: `==`, `!=`, `<`, `<=`, etc.
11. `not`
12. `and`
13. `or`
14. Assignment (`=`, `+=`, etc.)

---

# ✦ Input

We use `input()` to take user input.

```python
name = input("enter name: ")
print(name)
```

**Note:** input is always a **string**.

Convert input type:

```python
a = int(input("enter number: "))
```

---

# ✦ Practice Problem — Average of 2 Numbers

```python
a = int(input("enter 1st num: "))
b = int(input("enter 2nd num: "))

avg = (a + b) / 2
print("average =", avg)
```

---