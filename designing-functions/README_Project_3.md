# Project 3: Function Design and Decomposition

## Overview

Project 3 focuses on designing functions from specifications and
building larger solutions from smaller, testable pieces. The exercises
progress from a function stub, to a string-processing function developed
with backwards design, and finally to a time-conversion function
implemented with several helper functions.

Across the project, test scripts define and verify expected behavior.
The exercises emphasize incremental implementation, string indexing and
slicing, helper functions, and functional decomposition.

## Learning Objectives

This project demonstrates:

-   Using function specifications and stubs
-   Developing functions from documented examples and preconditions
-   Applying backwards design to a programming problem
-   Building and testing a solution incrementally
-   Finding delimiters within strings
-   Extracting information with string slicing
-   Removing surrounding whitespace
-   Converting numeric strings to integers
-   Creating helper functions
-   Combining helper functions into a larger computation
-   Organizing tests in implementation order

## Project Files

The uploaded files represent three stages of Project 3. The numbered
filenames preserve the separate versions supplied or developed during
the course.

## Stage 1: Function Stubs and `initials`

### `func(2).py`

Introduces a function stub for:

``` python
initials(n)
```

The function specification defines the desired result as the initials of
a two-part name in the form:

``` text
<first initial>. <last initial>.
```

For example:

``` python
initials('John Smith')
```

should return:

``` text
J. S.
```

The specification assumes that the input contains exactly a first name
and last name separated by one space. Middle names are not supported.

The provided file illustrates the idea of a function stub: a function
can first be specified before its implementation is completed.

### `tests(6).py`

Provides the completed test procedure:

``` python
test_initials()
```

The tests specify several expected results:

``` python
initials('John Smith')     # 'J. S.'
initials('Walker White')   # 'W. W.'
initials('alan smith')     # 'a. s.'
initials('Joan vanDeer')   # 'J. v.'
```

These cases demonstrate that the function should preserve the
capitalization of the original characters rather than automatically
converting initials to uppercase.

The supplied `func(2).py` contains the specification/stub but does not
contain a completed implementation of `initials()`.

## Stage 2: Backwards Design and `second_in_list`

### `func(3).py`

Implements:

``` python
second_in_list(s)
```

The function returns the second item from a comma-separated string and
removes whitespace surrounding that item.

Examples from the specification include:

``` python
second_in_list('apple, banana, orange')
```

returning:

``` text
banana
```

and:

``` python
second_in_list('  do  ,  re  ,  me  ,  fa  ')
```

returning:

``` text
re
```

The implementation breaks the task into several intermediate operations:

``` python
start = introcs.find_str(s, ',')
end = introcs.find_str(s, ',', start+1)
slice = s[start+1:end]
result = introcs.strip(slice)
```

First, it locates the first comma. It then searches for the next comma,
extracts the text between them, removes surrounding whitespace, and
returns the result.

The module identifies this function as having been implemented with the
backwards-design technique.

### `tests(7).py`

Tests `second_in_list()` using progressively varied inputs.

The comments divide the tests into successive implementation steps. The
cases include:

-   Standard comma-separated lists
-   Different item lengths
-   Extra spaces around an item
-   Lists containing more than three items
-   Whitespace in different positions
-   Lists without spaces after commas

Examples include:

``` python
second_in_list('apple,   fig , orange')
second_in_list('apple, fig, banana, orange')
second_in_list('do  ,  re  ,  me  ,  fa  ')
second_in_list('z,y,x,w')
```

All of these tests verify that the function identifies the second
comma-separated item rather than depending on fixed character positions.

## Stage 3: Helper Functions and Time Conversion

### `funcs(6).py`

The final stage contains four related functions:

``` python
get_seconds(time)
get_minutes(time)
get_hours(time)
str_to_seconds(time)
```

The input is documented as an extended ISO 8601-style time string in the
form:

``` text
hh:mm:ss
```

### `get_seconds(time)`

Extracts the seconds portion of the time string and converts it to an
integer:

``` python
return int(time[6:8])
```

For example:

``` python
get_seconds('03:02:05')
```

returns:

``` text
5
```

### `get_minutes(time)`

Extracts the minutes portion:

``` python
return int(time[3:5])
```

For example:

``` python
get_minutes('12:35:15')
```

returns:

``` text
35
```

### `get_hours(time)`

Extracts the hours portion:

``` python
return int(time[0:2])
```

For example:

``` python
get_hours('03:02:05')
```

returns:

``` text
3
```

### `str_to_seconds(time)`

Uses all three helper functions to calculate the number of seconds since
midnight:

``` python
return get_hours(time) * 3600 + get_minutes(time) * 60 + get_seconds(time)
```

For example:

``` python
str_to_seconds('12:35:15')
```

returns:

``` text
45315
```

This function illustrates functional decomposition. Instead of
extracting and converting every component inside one larger function,
the task is divided among three helper functions.

## Testing the Time Functions

### `tests(8).py`

The final test script contains four test procedures:

``` python
test_get_seconds()
test_get_minutes()
test_get_hours()
test_str_to_seconds()
```

The module documentation explicitly notes that the tests are called in
the same order in which the functions are intended to be implemented.

The helper functions are therefore tested first:

1.  `get_seconds()`
2.  `get_minutes()`
3.  `get_hours()`

Only after those components are tested does the script test:

4.  `str_to_seconds()`

The time-conversion tests include important boundaries and
representative values such as:

``` text
00:00:00
00:00:59
00:01:00
01:00:00
01:01:00
01:01:01
12:35:15
03:02:05
23:59:59
```

For example:

``` python
str_to_seconds('00:01:00')
```

must return `60`, while:

``` python
str_to_seconds('23:59:59')
```

must return `86399`.

## Design Progression

A major theme of Project 3 is the progression from a specification to a
complete solution.

### Function Specification

The `initials()` exercise begins with a documented function whose
expected behavior is established before the implementation.

### Backwards Design

`second_in_list()` demonstrates how a desired result can be broken into
the intermediate operations needed to produce it:

``` text
Locate first comma
        ↓
Locate second comma
        ↓
Extract second item
        ↓
Strip whitespace
        ↓
Return result
```

### Functional Decomposition

The time exercise extends this idea further. The larger conversion
problem is separated into smaller helper functions:

``` text
             str_to_seconds()
                    |
        +-----------+-----------+
        |           |           |
   get_hours() get_minutes() get_seconds()
```

Each helper can be implemented and tested independently before being
used by the primary function.

## Testing Strategy

The project continues the testing approach introduced in the previous
project by keeping implementation and testing code separate.

The tests use:

``` python
introcs.assert_equals(expected, result)
```

to compare the function's actual return value with the expected result.

The final exercise also demonstrates dependency-aware testing. Because
`str_to_seconds()` depends on the three helper functions, those helpers
are tested before the primary function.

## Requirements

-   Python 3
-   `introcs`

No additional third-party packages are used by the supplied project
files.

## Running the Tests

The course files import modules using names such as:

``` python
import func
```

and:

``` python
import funcs
```

The numbered filenames in this repository preserve the different stages
of the project. When running an individual stage in the original
arrangement, the corresponding implementation file should use the module
name expected by its test script.

For example:

``` bash
python tests.py
```

runs the applicable test procedures when the implementation is available
under the expected module name.

Successful test scripts conclude with:

``` text
Module func is working correctly
```

or:

``` text
Module funcs is working correctly
```

depending on the stage.

## Key Concepts

### Function Stubs

A stub provides the structure and specification of a function before its
implementation is complete. It allows the expected interface and
behavior to be established first.

### Backwards Design

Backwards design starts with the desired output and determines the
intermediate operations needed to construct that output.

### String Searching and Slicing

`second_in_list()` combines delimiter searches with slicing to isolate a
specific portion of a structured string.

### Helper Functions

The time-conversion exercise separates extraction of hours, minutes, and
seconds into independent functions.

### Functional Decomposition

Breaking a larger task into smaller functions improves organization and
allows each component to be tested independently.

### Incremental Testing

The supplied tests reflect the intended development order. Smaller
pieces are verified before the functions that depend on them.

## Project Structure

``` text
Project-3/
├── func(2).py
├── tests(6).py
├── func(3).py
├── tests(7).py
├── funcs(6).py
├── tests(8).py
└── README.md
```

## Author

Amelia Litvak

## Course

Cornell CIS 552
