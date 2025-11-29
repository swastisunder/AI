# **Python Fundamentals (Part 5) – Notes**

## **File I/O**

File I/O = reading/writing files in Python.

### **Opening a File**

```
file = open("filename", "mode")
```

### **Common Modes**

| Mode | Meaning       | Description                    |
| ---- | ------------- | ------------------------------ |
| r    | Read          | Error if file doesn't exist    |
| w    | Write         | Creates or overwrites          |
| a    | Append        | Adds content at end            |
| r+   | Read + Write  | File must exist                |
| w+   | Write + Read  | Overwrites                     |
| a+   | Append + Read | Reads + appends                |
| b    | Binary        | Used with other modes (rb, wb) |

---

## **Reading Files**

### `read()`

Reads whole file as a string.

```
f = open("data.txt", "r")
content = f.read()
f.close()
```

### `readline()`

Reads one line at a time.

```
line1 = f.readline()
line2 = f.readline()
```

### `readlines()`

Reads all lines into a list.

```
lines = f.readlines()
```

---

## **Writing to Files**

### `write()`

Writes a string.

```
f = open("data.txt", "w")
f.write("Hello students!")
f.close()
```

### `writelines()`

Writes multiple lines.

```
f = open("data.txt", "a")
f.writelines(["Line 1\n", "Line 2\n"])
f.close()
```

---

## **Recommended: `with open()`**

Automatically closes file.

```
with open("data.txt", "r") as f:
    content = f.read()
```

---

## **Deleting a File**

```
import os
os.remove("data.txt")
```

---

# **Exception Handling**

### **Common exceptions**

* `ZeroDivisionError`
* `NameError`
* `FileNotFoundError`
* `TypeError`

### **Basic Syntax**

```
try:
    # risky code
except:
    # runs if error
```

### **Specific Exception**

```
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### **else block**

Runs only when **no exception**.

```
try:
    x = int(input())
except ValueError:
    print("Invalid")
else:
    print(x)
```

### **finally block**

Runs **always**.

```
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")
```

---

# **List Comprehensions**

### **Basic Syntax**

```
[expression for item in iterable]
```

### Example

```
nums = [x for x in range(1, 6)]
```

### **With condition**

```
evens = [x for x in range(1, 11) if x % 2 == 0]
```

### **With if–else**

```
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
```

---

# **JSON Module**

### Import

```
import json
```

---

## **Python → JSON**

### `json.dumps()`

```
json_string = json.dumps(data)
```

### `json.dump()` (write to file)

```
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

---

## **JSON → Python**

### `json.loads()`

```
python_obj = json.loads(json_data)
```

### `json.load()` (read file)

```
with open("data.json", "r") as f:
    data = json.load(f)
```

---