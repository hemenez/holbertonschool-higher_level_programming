# 0x02. Python - import & modules

## Synopsis
This project covers:
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function `dir()`
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs

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

### 0-add.py

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`

* You have to use `print` function with string format to display integers
* You have to assign:
  * the value `1` to a variable called `a`
  * the value `2` to a variable called `b`
  * and use those two variables as arguments when calling the functions `add` and `print`
* `a` and `b` must be define in 2 different lines: `a = 1` and another `b = 2`
* Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
* You can only use the word `add_0` once in your code
* You are not allowed to use `*` for importing or `__import__`
* Your code should not be executed when imported - by using `__import__`, like the example below

### 1-calculation.py

Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

* Do not use the function `print` (with string format to display integers) more than 4 times
* You have to define:
  * the value `10` to a variable `a`
  * the value `5` to a variable `b`
  * and use those two variables only, as arguments when calling functions (included `print`)
* `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`
* Your program should call each of the imported functions.
* the word `calculator_1` should be used only once in your file
* You are not allowed to use `*` for importing
* Your code should not be executed when imported

### 2-args.py

Write a program that prints the number of and the list of its arguments.

* The output should be:
  * Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by:
  * `:` (or `.` if no argument where passed) followed by
  * a new line, followed by (if at least one argument),
  * one line per argument:
    * the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line
* Your code should not be executed when imported
* The number of elements of `argv` can be retrieved by using: `len(argv)`

### 3-infinite_add.py

Write a program that prints the result of the addition of all arguments

* The output should be the result of the addition of all arguments, followed by a new line
* You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers)
* Your code should not be executed when imported

### 4-hidden_discovery.py

Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

* You should print one name per line, in alpha order
* You should print only names that do not start with `__`
* Your code should not be executed when imported
* Make sure you are running your code in Python3.4.x (`hidden_4.pyc` has been compiled with this version)

### 5-variable_load.py

Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

* You are not allowed to use `*` when importing
* Your code should not be executed when imported