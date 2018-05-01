# Javascript - Warm up

## Synopsis
This project begins an introduction to JavaScript.

## Requirements for JavaScript scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 14.04 LTS using node (version 6.10.2)
* The first line of all files should be exactly `#!/usr/bin/node`
* All files should end with a new line
* A `README.md` at the root of the folder of the project is mandatory
* Code should be `semistandard` compliant (version 11.0.0)
* All files must be executalbe

## Environment
The project was tested and compiled on `Ubuntu 14.04 (trusty64)` via Vagrant run through VirtualBox.

## File Descriptions
This repository contains the following files. Listed are the parameters of each task:

### 0-javascript_is_amazing.js

Write a script that prints “Javascript is amazing”:

* You must create a constant variable called `myVar` with the value “Javascript is amazing”
* You must use `console.log(...)` to print all output
* Not allowed to use `var`

### 1-multi_languages.js

Write a script that prints 3 lines:

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “Javascript is amazing”
* You must use `console.log(...)` to print all output
* Not allowed to use `var`

### 2-arguments.js

Write a script that prints a message depending of the number of arguments passed:

* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
* You must use `console.log(...)` to print all output
* Not allowed to use `var`

### 3-value_argument.js

Write a script that prints the first argument passed to it:

* If no arguments are passed to the script, print “No argument”
* You must use `console.log(...)` to print all output
* Not allowed to use `var`
* Not allowed to use `length`

### 4-concat.js

Write a script that prints two arguments passed to it, in the following format: “ is ”

* You must use `console.log(...)` to print all output
* Not allowed to use `var`

### 5-to_integer.js

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

* If the argument can’t be converted to an integer, print “Not a number”
* You must use `console.log(...)` to print all output
* Not allowed to use `var`
* Not allowed to use `try/catch`

### 6-multi_languages_loop.js

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “Javascript is amazing”
* You must use `console.log(...)` to print all output
* Not allowed to use `var`
* Not allowed to use `if/else` statement
* Can only use one `console.log`
* Must use a loop

### 7-multi_c.js

Write a script that prints `x` times "C is fun"

* `x` is first argument of the script
* If the first argument can’t be converted to an integer, print “Missing number of occurrences”
* You must use `console.log(...)` to print all output
* Not allowed to use `var`
* Can only use two `console.log`
* Must use a loop

### 8-square.js

Write a script that prints a square

* The first argument is the size of the square
* If the first argument can’t be converted to an integer, print “Missing size”
* Use the character `X` to print the square
* You must use `console.log(...)` to print all output
* Not allowed to use `var`
* Must use a loop

### 9-add.js

Write a script that prints the addition of 2 integers

* The first argument is the first integer
* The second argument is the second integer
* You have to define a function with this prototype: `function add(a, b)`
* You must use `console.log(...)` to print all output
* Not allowed to use `var`

### 10-factorial.js

Write a script that computes and prints a factorial

* The first argument is integer (argument can be cast as integer) used for computing the factorial
* Factorial of `NaN` is `1`
* Must do it recursively
* Must use a function
* You must use `console.log(...)` to print all output
* Not allowed to use `var`

### 11-second_biggest.js

Write a script that searches the second biggest integer in the list of arguments.

* You can assume all arguments can be converted to integer
* If no argument passed, print `0`
* If the number of arguments is 1, print `0`
* You must use `console.log(...)` to print all output
* Not allowed to use `var`

### 12-object.js

Update this script to replace the value	`12` with `89`:

* Not allowed to use `var`

### 13-add.js

Write a function that returns the addition of 2 integers.

* The function must be visible from outside
* The name of the function must be `add`
* You are not allowed to use `var`