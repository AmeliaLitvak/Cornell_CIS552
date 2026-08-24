# Project 1: Functions, Procedures, and Dice

## Overview

This project introduces several fundamental Python programming concepts
through a series of small dice-based programs. The files progress from a
simple script to reusable procedures and functions, then demonstrate
default arguments, global variables, and decomposition of a larger
problem into smaller functions.

The dice examples use Python's `random` module to generate random
integers within a specified range. Together, the exercises illustrate
how code can evolve from a sequence of statements into reusable and
better-organized components.

## Learning Objectives

The project demonstrates:

-   Using the `random` module to generate random integers
-   Reading user input and converting strings to integers
-   Defining and calling procedures and functions
-   Understanding the difference between displaying a result and
    returning a value
-   Using parameters and preconditions
-   Providing default parameter values
-   Working with global variables
-   Returning Boolean values
-   Breaking a larger programming task into smaller functions
-   Writing docstrings that describe behavior, parameters, examples, and
    preconditions

## Files

### `dice.py`

A basic dice-rolling script.

The program:

1.  Prompts the user for the lowest and highest possible numbers.
2.  Converts the input values to integers.
3.  Generates two random integers in the specified inclusive range.
4.  Adds the two generated values.
5.  Prints the resulting sum.

This file demonstrates a straightforward procedural script before the
dice behavior is moved into reusable functions.

### `proc.py`

Introduces the procedure `rollem(first, last)`.

The procedure generates two random numbers between `first` and `last`,
adds them together, and displays the result. Unlike the later function
version, this implementation prints the sum rather than returning it to
the caller.

The documented preconditions specify that `first` must be an integer and
`last` must be an integer greater than or equal to `first`.

### `func.py`

Reworks `rollem(first, last)` as a function.

Instead of displaying the result itself, the function returns the sum of
the two randomly generated numbers. This makes the result available to
other parts of a program and allows the function to be reused in larger
computations.

For example, when called as:

``` python
rollem(1, 6)
```

the function can return any value from `2` through `12`.

### `func(1).py`

Extends the `rollem` function by providing default parameter values:

``` python
def rollem(first=1, last=6):
```

Because the defaults represent a standard six-sided die, the function
can be called simply as:

``` python
rollem()
```

It can still accept other ranges when arguments are supplied.

### `globb.py`

Demonstrates the use of a global variable.

The module initializes:

``` python
VAR = 1
```

The `next()` function returns the current value of `VAR` and then
increments the global variable by one. Repeated calls therefore produce
successive values.

This exercise illustrates how the `global` keyword allows a function to
modify a variable defined at module scope.

### `game.py`

Builds a simple two-player dice game and demonstrates function
decomposition.

The `roll_off(handicap1, handicap2)` function:

1.  Rolls two six-sided dice for Player 1 using `rollem(1, 6)`.
2.  Adds Player 1's handicap.
3.  Rolls two six-sided dice for Player 2.
4.  Adds Player 2's handicap.
5.  Displays both scores.
6.  Returns `True` if Player 1's score is greater than Player 2's score
    and `False` otherwise.

The module separates the dice-rolling behavior into the `rollem()`
helper function instead of placing all of the random-number logic
directly inside `roll_off()`.

This illustrates how a longer function can be divided into smaller,
reusable functions.

## Requirements

-   Python 3
-   Python standard-library `random` module

No third-party packages are required.

## Running the Examples

The basic script can be run from a terminal with:

``` bash
python dice.py
```

It prompts for the lower and upper bounds used to generate the two
random numbers.

The other files primarily define functions intended to be called from
Python. For example:

``` python
from func import rollem

result = rollem(1, 6)
print(result)
```

A standard six-sided roll can also be produced by the version of
`rollem` that provides default arguments.

## Key Concepts

### Procedures vs. Functions

The project demonstrates an important distinction between producing
output and returning a value.

In `proc.py`, `rollem()` displays the dice total directly:

``` python
print('The sum is '+str(thesum)+'.')
```

In `func.py`, the function instead returns the value:

``` python
return thesum
```

Returning the result makes the operation more reusable because another
function can use the value in a larger computation.

### Parameters and Preconditions

The function docstrings document both the purpose of each parameter and
assumptions about valid arguments. For the dice functions, `first`
represents the lowest possible random value and `last` represents the
greatest possible value.

### Default Arguments

The alternate function implementation introduces defaults of `1` and
`6`, allowing a caller to omit arguments when standard six-sided dice
are desired.

### Global State

`globb.py` demonstrates that a function can access and modify
module-level state with the `global` keyword. Each call to `next()`
changes the value that will be observed by the next call.

### Function Decomposition

`game.py` shows why reusable functions become useful as programs grow.
Dice generation is handled by `rollem()`, while `roll_off()` focuses on
the rules of the game. Separating these responsibilities makes the
program easier to understand and organize.

## Example Game Logic

A roll-off can be evaluated with:

``` python
roll_off(0, 0)
```

Each player rolls two six-sided dice with no additional handicap. The
program prints both scores and returns whether Player 1 won.

Different handicaps can be supplied:

``` python
roll_off(2, 0)
```

In this example, Player 1 receives two additional points before the
scores are compared.

## Project Structure

``` text
Project-1/
├── dice.py
├── proc.py
├── func.py
├── func(1).py
├── globb.py
├── game.py
└── README.md
```

## Author

Amelia Litvak

## Course

Cornell CIS 552
