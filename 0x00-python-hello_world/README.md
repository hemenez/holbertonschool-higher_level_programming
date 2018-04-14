# 0x00. Python - Hello, World

## Synopsis
This project covers:
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using `print`
* How to use strings
* What are indexing and slicing in Python
* What is the official Holberton Python coding style and how to check your code with `PEP 8`

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

## Requirements for Shell scripts
* First line of all files should be exactly `#!/bin/bash`
* All files should end with a new line
* All files must be executable

## Environment
The project was tested and compiled on `Ubuntu 14.04 (trusty64)` via Vagrant run through VirtualBox.

## File Descriptions
This repository contains the following files. Listed are the parameters of each task:

### 0-run

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`

### 1-run_inline

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`

### 2-print.py

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

* Use the function `print`

### 3-print_number.py

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery Street`, followed by a new line.

* You are not allowed to cast the variable `number` into a string
* Your code must be 3 lines long
* You have to use the new print numbers [tips](https://pyformat.info/#number)

### 4-print_float.py

Complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable `number` with a precision of 2 digits.

* You are not allowed to cast the variable `number` into a string
* You have to use the new print numbers [tips](https://pyformat.info/#number)

### 5-print_string.py

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

* Must use new lines
* You are not allowed to use any loops or conditional statement
* Your program should be maximum 5 lines long

### 6-concat.py

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`

* You are not allowed to use any loops or conditional statements.
* You have to use the variables `str1` and `str2` in your new line of code
* Your program should be exactly 5 lines long

### 7-edges.py

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)

* You are not allowed to use any loops or conditional statements
* Your program should be exactly 8 lines long
* `word_first_3` should contain the first 3 letters of the variable `word`
* `word_last_2` should contain the last 2 letters of the variable `word`
* `middle_word` should contain the value of the variable `word` without the first and last letters

### 8-concat_edges.py

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.

* You are not allowed to use any loops or conditional statements
* Your program should be exactly 5 lines long
* You are not allowed to create new variables
* You are not allowed to use string literals

### 9-easter_egg.py

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

* our script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

### Linked list cycle (technical interview preparation)

* You are not allowed to google anything
* Whiteboard first
* This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.

* Prototype: `int check_cycle(listint_t *list);`
* Return: `0` if there is no cycle, `1` if there is a cycle

Requirements:

* Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`

#### lists.h

Header file containing function prototypes

#### 10-check_cycle.c

Function tests if linked lists has a cycle