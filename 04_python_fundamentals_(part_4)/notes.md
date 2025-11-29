# **Python OOP – Short Notes (Part-4)**

## **What is OOP?**

* A programming style that organizes code into **objects** (data + behaviour).
* Helps make code **modular, reusable, maintainable**.
* Based on **classes** (blueprints) and **objects** (instances).

---

## **Classes & Objects**

### **Class**

* A **blueprint/template** for creating objects.
* Contains **attributes** (variables) and **methods** (functions).

### **Object**

* A **real instance** created from a class.
* Uses dot `.` operator to access data or methods.

---

## **Constructor (`__init__`)**

* Special method called automatically when object is created.
* Used to **initialize values**.
* Types:

  1. **Default constructor** – only `self`.
  2. **Parameterized constructor** – takes values.

---

## **Attributes**

### **1. Class Attributes**

* Shared by all objects.
* Declared **outside methods**.

### **2. Instance Attributes**

* Unique to each object.
* Declared inside `__init__` using `self`.

---

## **Methods**

### **1. Instance Method**

* First parameter: `self`.
* Can access **instance + class attributes**.

### **2. Class Method**

* Decorator: `@classmethod`
* First parameter: `cls`
* Works with **class-level data**.

### **3. Static Method**

* Decorator: `@staticmethod`
* No `self` or `cls`.
* Used for logically related utility functions.

---

# **OOP Pillars**

## **1. Encapsulation**

* Bundling data + methods in one class.
* Access modifiers:

  * **Public**: normal variables.
  * **Protected**: `_var`
  * **Private**: `__var` (name-mangled as `_ClassName__var`)
* Use **getters** & **setters** for private variables.

---

## **2. Inheritance**

Child class inherits parent features.

### Types:

1. **Single Inheritance**
2. **Multi-level Inheritance**
3. **Multiple Inheritance**

`super()` → used to call parent’s method/constructor.

---

## **3. Abstraction**

* Hiding internal complexity, showing only essential behaviour.
* Achieved using:

  * Abstract classes (`ABC`)
  * Abstract methods (`@abstractmethod`)
* Cannot instantiate abstract class.

---

## **4. Polymorphism**

### **1. Method Overriding**

* Child class redefines parent method.
* Runtime polymorphism.

### **2. Duck Typing**

* If an object has the method, it can be used.
* Python doesn’t check types, only behaviour.

### Operator Overloading Example

* `+` works differently for numbers and strings.

---