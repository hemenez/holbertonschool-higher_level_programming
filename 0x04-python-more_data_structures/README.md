# 0x04. Python - More Data Structures: Set, Dictionary

## Synopsis
This project covers:
* Why indentation is so important in Python
* How to use the `if`, `if ... else` statements
* How to use comments
* How to affect values to variables
* How to use the `while` and `for` loops
* How is the Python’s `for` different from the `C`‘s?
* How to use the `break` and `continues` statements
* How to use `else` clauses on loops
* What does the `pass` statement do, and when to use it
* How to use `range`
* What is a function and how do you use functions
* What does return a function that does not use any `return` statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them

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

### 0-square_matrix_simple.py

Write a function that computes the square value of all integers of a matrix.

* Prototype: `def square_matrix_simple(matrix=[]):`
* `matrix` is a 2-d array
* Returns a new matrix:
  * same size as `matrix`
  * Each value should be the square of the value of the input
* Initial matrix should not be modified
* You are not allowed to import any module
* You are allow to use regular loops, map, etc

### 1-search_replace.py

Write a function that replaces all occurrences of an element by another in a new list.

* Prototype: `def search_replace(my_list, search, replace):`
* `list` is the initial list
* `search` is the element to replace in the list
* `replace` is the new element
* You are not allowed to import any module

### 2-uniq_add.py

Write a function that makes the addition of all unique integers in a list (only one time each integer).

* Prototype: `def uniq_add(my_list=[]):`
* You are not allowed to import any module

### 3-common_elements.py

Write a function that returns a set of common elements in two sets.

* Prototype: `def common_elements(set_1, set_2):`
* You are not allowed to import any module

### 4-only_diff_elements.py

Write a function that returns a set of all elements present in only one set.

* Prototype: `def only_diff_elements(set_1, set_2):`
* You are not allowed to import any module

### 5-number_keys.py

Write a function that returns the number of keys in a dictionary.

* Prototype: `def number_keys(a_dictionary):`
* You are not allowed to import any module

### 6-print_sorted_dictionary.py

Write a function that prints a dictionary by ordered keys.

* Prototype: `def print_sorted_dictionary(a_dictionary):`
* You can assume that all keys are string
* Keys should be sorted by alphabetic order
* Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
* Dictionary values can have any type
* You are not allowed to import any module

### 7-update_dictionary.py

Write a function that replace or add key/value in a dictionary.

* Prototype: `def update_dictionary(a_dictionary, key, value):`
* `key` argument will be always a string
* `value` argument will be any type
* If a key exists in the dictionary, the value will be replaced
* If a key doesn’t exist in the dictionary, it will be created
* You are not allowed to import any module

### 8-simple_delete.py

Write a function that deletes a key in a dictionary.

* Prototype: `def simple_delete(a_dictionary, key=""):`
* `key` argument will be always a string
* If a key doesn’t exist, the dictionary won’t change
* You are not allowed to import any module

### 9-multiply_by_2.py

Write a function that returns a new dictionary with all values multiplied by 2

* Prototype: `def multiply_by_2(a_dictionary):`
* You can assume that all values are only integers
* Returns a new dictionary
* You are not allowed to import any module

### 10-best_score.py

Write a function that returns a key with the biggest integer value.

* Prototype: `def best_score(a_dictionary):`
* You can assume that all values are only integers
* If no score found, return `None`
* You can assume all students have a different score
* You are not allowed to import any module

### 11-mutiply_list_map.py

Write a function that returns a list with all values multiplied by a number without using any loops.

* Prototype: `def mutiply_list_map(my_list=[], number=0):`
* Returns a new list:
  * same length as `my_list`
  * each value should be multiplied by `number`
* Initial list should not be modified
* You are not allowed to import any module
* You have to use `map`
* Your file should be max 3 lines