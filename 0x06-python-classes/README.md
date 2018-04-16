# 0x06. Python - Classes and Objects

## Synopsis
This project covers:
* What is OOP
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is `self`
* What is a method
* What is the special `__init__` method and how to use it
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python

## Requirements for Python scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* The first line of all files should be exactly `#!/usr/bin/python3`
* All files should end with a new line
* A `README.md` at the root of the folder of the project is mandatory
* Code should use the `PEP 8` style (version 1.7.*)
* All files must be executalbe
* All modules should have documentation
* Code should not be executed when imported (by using `if __name__ == "__main__":`)

## Environment
The project was tested and compiled on `Ubuntu 14.04 (trusty64)` via Vagrant run through VirtualBox.

## File Descriptions
This repository contains the following files. Listed are the parameters of each task:

### 0-square.py

Write an empty class `Square` that defines a square.

### 1-square.py

Add to class `Square`:

* Private instance attribute: `size`
* Instantiation with `size` (no type/value verification)
* You are not allowed to import any module

### 2-square.py

Add to class `Square`:

* Instantiation with optional `size`: `def __init__(self, size=0):` (with type/value verification)
* You are not allowed to import any module

### 3-square.py

Add to class `Square`:

* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module

### 4-square.py

Add to class `Square`:

* property `def size(self):` to retrieve it
* property setter `def size(self, value):` to set it
* You are not allowed to import any module

### 5-square.py

Add to class `Square`:

* Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`
* You are not allowed to import any module

### 6-square.py

Add to class `Square`:

* Private instance attribute: position:
  * property `def position(self):` to retrieve it
  * property setter `def position(self, value):` to set it
* Instantiation with optional `position`: `def __init__(self, size=0, position=(0, 0)):`