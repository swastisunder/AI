# ⭐ **1. What is NumPy?**

* NumPy = **Numerical Python** (library for maths + data).
* Used for **fast calculations** on large data.
* Gives a new data structure → **ndarray** (n-dimensional array).
* Much faster than Python lists.
* Used in **Data Science, Machine Learning, Deep Learning**.

---

# ⭐ **2. Important Features**

* **Multidimensional arrays** → 1D, 2D, 3D…
* **Math functions** → algebra, random numbers, FFT etc.
* **Vectorization** → do operations without loops.
* **Interoperability** → works with Pandas, Matplotlib, TensorFlow, PyTorch.

---

# ⭐ **3. NumPy Arrays vs Python Lists**

* NumPy is **faster** (written in C).
* Stores data in **continuous memory** → faster access.
* Arrays are **homogeneous** (same data type).
* Supports **vectorized operations** (no slow loops).

---

# ⭐ **4. Performance Comparison**

* Python list squaring = **slow (loop)**.
* NumPy array squaring = **fast (`arr**2`)**.
* Memory:

  * Python list uses **more memory**.
  * NumPy uses **less memory (`nbytes`)**.

---

# ⭐ **5. Creating NumPy Arrays**

### ✔ From Python List

```python
arr = np.array([1, 2, 3])
```

### ✔ 2D Array (Matrix)

```python
arr2 = np.array([[1,2,3],[4,5,6]])
```

---

### ✔ Built-in Functions

* `np.zeros((m,n))` → array of 0s
* `np.ones((m,n))` → array of 1s
* `np.full((m,n), value)` → filled with a value
* `np.eye(n)` → identity matrix
* `np.arange(start, stop, step)`
* `np.linspace(start, stop, count)` → evenly spaced numbers

---

# ⭐ **6. Useful Array Properties**

For array `arr`:

* `arr.shape` → rows × columns
* `arr.size` → total elements
* `arr.ndim` → number of dimensions
* `arr.dtype` → data type
* `arr.itemsize` → size of each element

---

# ⭐ **7. Dtypes (Data Types)**

NumPy supports:

* Integers → `int32`, `int64`
* Floats → `float32`, `float64`
* Boolean → `bool`
* Complex → `complex64`, `complex128`
* Strings → `S`, `U`
* Object → `object` (slow)

### ✔ Change dtype

```python
float_arr = arr.astype('float64')
```

### ✔ Downcasting

Convert to smaller type to save memory (ex: ages → int8).

---

# ⭐ **8. Reshaping**

```python
reshaped = arr.reshape((rows, cols))
flattened = arr.flatten()
```

* reshape = change shape
* flatten = convert 2D → 1D

---

# ⭐ **9. Indexing**

### ✔ 1D

```python
arr[0]
```

### ✔ 2D

```python
arr[0][1]
```

---

# ⭐ **10. Fancy Indexing**

* Pass a list of indices:

```python
arr[[0,1,4]]
```

---

# ⭐ **11. Boolean Indexing**

```python
arr[arr > 2]
arr[arr % 2 == 0]
```

---

# ⭐ **12. Slicing**

### 1D

```python
arr[2:6]
arr[:6]
arr[3:]
arr[::2]
```

### ✔ Very Important

* Slicing **list** → returns **COPY**
* Slicing **NumPy array** → returns **VIEW** (affects original)

### Make a COPY

```python
copy_arr = arr[1:4].copy()
```

---

# ⭐ **13. Multi-Dimensional Arrays**

* **1D** → vector
* **2D** → matrix
* **3D** → tensor (used in images)

### Images

* Grayscale → 2D
* Color (RGB) → 3D (H × W × 3)

---

# ⭐ **14. Operations Along Axis**

```python
np.sum(arr, axis=0)   # column sum
np.sum(arr, axis=1)   # row sum
```

---

# ⭐ **15. 3D Array Operations**

Indexing:

```python
arr3D[layer][row][col]
```

Selecting:

```python
arr3D[:, :, 0]   # all layers, column 0
arr3D[:, 0, :]   # all layers, row 0
```

Modify:

```python
arr3D[:, 0, :] = 99
```

---

# ⭐ **16. Vectorization**

Do operations on full array:

```python
arr ** 2
arr + arr2
arr * 10
```

No loops → very fast.

---

# ⭐ **17. Broadcasting**

NumPy automatically expands shapes.

Examples:

```python
arr * 10
arr1D + arr2D
```

### ✔ Normalization Example

```python
normalized = (arr - mean) / std
```

---

# ⭐ **18. Mathematical Functions**

### ✔ Aggregation

```python
np.sum()
np.prod()
np.min()
np.max()
np.mean()
np.median()
np.std()
np.var()
np.argmin()
np.argmax()
```

---

### ✔ Power Functions

```python
np.square()
np.sqrt()
np.pow(a, b)
```

---

### ✔ Log & Exponential

```python
np.log()
np.log10()
np.log2()
np.exp()
```

---

### ✔ Rounding

```python
np.round()
np.floor()
np.ceil()
np.trunc()
```

---

### ✔ Misc

```python
np.abs()
np.sort()
np.unique()
```

---

# ⭐ **NUMPY SUMMARY (Super Short Revision)**

* NumPy = fast numerical library
* ndarray = powerful array
* Faster + memory efficient
* Create: `np.array()`, `zeros`, `ones`, `full`, `arange`, `linspace`
* Properties: shape, size, ndim, dtype
* Indexing, slicing, fancy indexing
* Copy vs view → IMPORTANT
* Reshape, flatten
* Math across axes
* Broadcasting
* Vectorization
* Tons of math functions

---
