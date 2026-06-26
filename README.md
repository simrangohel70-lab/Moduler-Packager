# Moduler-Packager

# 🛠️ Multi Utility Toolkit

## 📖 Project Overview

The **Multi Utility Toolkit** is a Python-based console application developed using Python modules, packages, and built-in libraries. This project demonstrates modular programming concepts by integrating built-in modules and custom modules to perform multiple utility operations such as date-time processing, mathematical calculations, random data generation, UUID creation, file handling, and dynamic module exploration.

The toolkit provides a **menu-driven interface** that allows users to easily access and interact with various features.

---

## ✨ Features

### 🕒 1. Date and Time Operations

Uses Python's `datetime` and `time` modules to:

✔ Display current date and time
✔ Calculate differences between dates
✔ Format dates and times
✔ Implement stopwatch functionality

---

### 🧮 2. Mathematical Operations

Uses Python's `math` module to:

✔ Calculate square root
✔ Calculate factorial
✔ Perform trigonometric calculations
✔ Calculate compound interest
✔ Find area of geometric shapes

---

### 🎲 3. Random Data Generation

Uses Python's `random` module to:

✔ Generate random numbers
✔ Generate random passwords
✔ Generate OTPs
✔ Randomly sample data from lists

---

### 🆔 4. Unique Identifier Generation

Uses Python's `uuid` module to:

✔ Generate unique identifiers
✔ Create UUID4 values for files, records, or sessions

---

### 📂 5. File Operations (Custom Module)

Provides file handling functionality:

✔ Create files
✔ Write data into files
✔ Read file content
✔ Append data into files

---

### 🔍 6. Module Exploration

Uses the `dir()` function to:

✔ Explore built-in module attributes
✔ Dynamically inspect module functionalities

---

### 🚪 7. Exit Program

✔ Safely terminates the application

---

## 📁 Project Structure

```text
Multi Utility Toolkit/
│
├── main.py
│
└── Packages/
    ├── __init__.py
    ├── file_utils.py
    └── math_utils.py
```

---

## 💡 Concepts Demonstrated

### 📚 Built-in Modules Used

* `datetime`
* `time`
* `math`
* `random`
* `uuid`

---

### ⚙️ Custom Modules Created

* `file_utils.py`
* `math_utils.py`

---

### 📦 Package Implementation

Uses:

```python
__init__.py
```

to initialize package functionality.

---

### 👨‍💻 User Defined Functions (UDF)

Functions implemented in the project:

* `date_time()`
* `stopwatch()`
* `math_operations()`
* `random_operations()`
* `generate_uuid()`
* `file_menu()`
* `explore()`
* `menu()`

---

### 🔎 Dynamic Module Exploration

Implemented using:

```python
dir(math)
dir(random)
```

---

### ▶ Main Program Execution

Uses:

```python
if __name__ == "__main__":
    menu()
```

This ensures that the program executes only when the script is run directly.

---

## 🔄 Program Flow

1️⃣ User starts the program
2️⃣ Main menu is displayed
3️⃣ User selects an operation
4️⃣ Program processes the request
5️⃣ Results are displayed
6️⃣ User continues or exits the toolkit safely

---

## 📸 Output Screenshots

### 🏠 Main Menu

![Main Menu](mainmenu.png)

### 🕒 Date and Time Operations

![Datetime](datetime.png)

### 🧮 Mathematical Operations

![Math](math.png)

### 🎲 Random Data Generation

![Random](random.png)

### 🆔 UUID Generation

![UUID](uuid.png)

### 📂 File Operations

![Files](files.png)

### 🔍 Module Exploration

![Module](module.png)
---

## 👩‍💻 Author

**Simran Gohel**
