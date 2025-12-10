# **Pandas – Short Notes**

## **What is Pandas?**

* A popular Python library for **data analysis & manipulation**.
* Built on top of **NumPy**.
* Provides high-level data structures for working with labeled/tabular data.

---

# **Core Data Structures**

## **1. Series**

* One-dimensional labeled array.
* Contains:

  * **Values**
  * **Index**
* Supports **vectorized operations**.
* Mutable values but **immutable size**.
* Can handle missing values (`NaN`).
* Homogeneous data.

### Usage

```
s = pd.Series([23, 24, 25, 26])
s2 = pd.Series([23,24,25,26], index=["Adam","Eve","Charlie","Bob"])
```

---

## **2. DataFrame**

* Two-dimensional tabular structure (rows + columns).
* Each column is a **Series**.
* Contains:

  * Rows
  * Columns
  * Index
  * Column labels

### Create DataFrame

```
df = pd.DataFrame(info_dict)
df = pd.DataFrame(np_array, columns=[...])
df = pd.DataFrame(list_of_lists, columns=[...])
```

---

# **Working With Data Files**

### **Import**

```
pd.read_csv("data.csv")
pd.read_json("data.json")
```

### **Export**

```
df.to_csv("output.csv")
df.to_csv("output.csv", index=False)
df.to_json("output.json")
```

---

# **Data Viewing & Inspection**

```
df.head(n)
df.tail(n)
df.sample(n)
df.info()
df.describe()
df.nunique()
df.shape
df.columns
df.dtypes
```

---

# **Indexing & Selection**

## **Selecting Columns**

```
df["col"]           # Series
df[["col1","col2"]] # DataFrame
```

## **Selecting Rows**

### **loc → label-based**

```
df.loc[0]
df.loc[0:3]   # inclusive
df.loc[0, "country"]
```

### **iloc → position-based**

```
df.iloc[0]
df.iloc[4:7]  # exclusive
df.iloc[0, 2]
```

## **Selecting Single Cell**

```
df.at[row_label, col_label]
df.iat[row_pos, col_pos]
```

---

# **Filtering & Querying**

## **Boolean Filtering**

```
df[df["Age"] > 30]
df[(df["Age"] > 30) & (df["Salary"] > 50000)]
```

## **Query Method**

```
df.query("Age > 30 and Salary < 70000")
df.query("country == @my_country")
```

### Query rules:

* Condition inside string.
* Operators: `and`, `or`, `not`, `==`, `!=`, `<`, `>`, `<=`, `>=`
* Use backticks for column names with spaces.
* `@` to access python variables.

---

# **Data Cleaning**

## **Missing Values**

```
df.isnull()
df.isnull().sum()
df.dropna()
df.dropna(axis=1)
df.fillna(val)
df["age"] = df["age"].fillna(df["age"].mean())
df.ffill()
df.bfill()
```

---

## **Duplicate Values**

```
df.duplicated()
df.duplicated("country")
df.duplicated(["country","gender"])
df.drop_duplicates()
```

---

## **Changing Data Types**

```
df["income"] = df["income"].astype(int)
pd.to_datetime("2025-12-01")
```

---

## **String Cleaning**

```
df["col"].str.lower()
df["col"].str.upper()
df["col"].str.capitalize()
df["col"].str.strip()
df["col"].str.split(" ")
df["col"].str.contains("text")
```

---

# **Other Useful Methods**

```
df.apply()
df.map()
df.assign()
df.replace(old, new)
```

---
