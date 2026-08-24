# Project 4: Errors, Assertions, and Input Validation

## Overview

Project 4 focuses on understanding errors and using assertions to
enforce function preconditions. It builds on string-processing and
time-conversion exercises from earlier work, adding checks that help
identify invalid inputs before the main computation proceeds.

The project begins with deliberately buggy fraction-processing code
intended for practicing how to read error messages. It then revisits
`second_in_list()` with assertions and improved diagnostic messages. The
final stage adds format checking and precondition assertions to a set of
functions that process `hh:mm:ss` time strings.

## Learning Objectives

This project demonstrates:

-   Reading and interpreting Python error messages
-   Recognizing different sources of runtime failure
-   Using `assert` to enforce preconditions
-   Adding useful diagnostic messages to assertions
-   Validating argument types and structural requirements
-   Separating input checks from the main computation
-   Reusing validation logic across multiple functions
-   Testing valid and malformed inputs
-   Extending previously developed functions with defensive checks

## Project Files

The uploaded files represent several related stages of Project 4.

## Stage 1: Reading Error Messages

### `funcs(7).py`

This module is explicitly designed to contain multiple bugs. Its
documentation states that the goal is to identify the problems by
reading the resulting error messages rather than necessarily fixing
them.

It defines three functions:

``` python
numerator(s)
denominator(s)
frac_to_dec(s)
```

### `numerator(s)`

The function is intended to return the numerator of a fraction
represented as a string such as:

``` text
1/2
31/64
```

The implementation is:

``` python
return int(s[:2])
```

Because this exercise intentionally contains bugs, the implementation
should be viewed as part of the debugging exercise rather than as a
general fraction parser.

### `denominator(s)`

The function is intended to return the denominator portion of a fraction
string:

``` python
return int(s[-1])
```

Its documented precondition specifies that the denominator is one digit.

### `frac_to_dec(s)`

Calls the two helper functions and divides the resulting numerator by
the denominator:

``` python
n = numerator(s)
d = denominator(s)
return n/d
```

The module contains several example calls near the bottom that can be
uncommented as directed:

``` python
frac_to_dec("10/0")
frac_to_dec("2/5")
frac_to_dec("ll/25")
frac_to_dec("12/10")
```

These inputs provide opportunities to observe how errors arise from
different assumptions or operations in the program.

## Stage 2: Enforcing Preconditions

### `func(4).py`

Revisits the `second_in_list(s)` function developed previously.

The function still extracts the second item from a comma-separated list,
but it now begins by checking assumptions about its input:

``` python
assert type(s) == str, 'Precondition violation'
assert introcs.count_str(s, ',') >= 2
```

These assertions correspond to important parts of the documented
precondition:

-   `s` must be a string.
-   The input must contain enough comma-separated items for a second
    item to exist.

After these checks, the function performs the same general sequence of
operations:

``` text
Find first comma
        ↓
Find second comma
        ↓
Extract text between them
        ↓
Strip surrounding whitespace
        ↓
Return second item
```

### `tests(9).py`

Tests the normal behavior of `second_in_list()` with several valid
comma-separated strings.

The tests include variations in:

-   Item length
-   Whitespace
-   Number of items
-   Placement of spaces after commas

Examples include:

``` python
second_in_list('apple, banana, orange')
second_in_list('apple,   fig , orange')
second_in_list('  do  ,  re  ,  me  ,  fa  ')
second_in_list('z,y,x,w')
```

The tests verify that adding assertions does not change the expected
behavior for inputs satisfying the preconditions.

## Stage 3: Descriptive Assertion Messages

### `func(5).py`

This version retains the same `second_in_list()` implementation but
improves the assertions by providing information about the invalid
value.

The type check becomes:

``` python
assert type(s) == str, 'The value '+repr(s)+' is not a string.'
```

The comma-count check becomes:

``` python
assert introcs.count_str(s,',') >= 2, \
    'The string '+repr(s)+' does not have enough commas.'
```

These messages make an assertion failure more informative by identifying
both the violated condition and the supplied value.

This stage demonstrates that assertions can do more than stop execution:
their messages can help explain why a precondition was violated.

## Stage 4: Validating Time Strings

### `funcs(8).py`

The final stage extends the time-processing functions from the previous
project.

It contains:

``` python
iso_8601(s)
get_seconds(time)
get_minutes(time)
get_hours(time)
str_to_seconds(time)
```

### `iso_8601(s)`

Checks the structure of a string intended to have the form:

``` text
hh:mm:ss
```

The implementation creates separate Boolean checks for the pieces of the
string:

``` python
check1 = introcs.isdigit(s[:2])
check2 = s[2] == ':'
check3 = introcs.isdigit(s[3:5])
check4 = s[5] == ':'
check5 = introcs.isdigit(s[6:8])
```

These checks verify that the expected digit groups and colon separators
occur in the correct positions.

The function also asserts that the supplied value is a string and has
length 8.

### Important Implementation Detail

The `iso_8601()` docstring states that the function returns `True` for a
correctly formatted string and `False` otherwise.

However, the uploaded implementation contains:

``` python
assert check1 and check2 and check3 and check4 and check5 == True
return True
```

Therefore, as written, malformed eight-character strings can cause an
`AssertionError` rather than producing `False`.

This README documents the behavior of the uploaded source rather than
changing or silently correcting it.

## Preconditions in the Time Functions

Each extraction function checks its input before performing the slice.

For example, `get_seconds()` contains:

``` python
assert type(time) == str
assert len(time) == 8
assert iso_8601(time) == True
```

Equivalent checks appear in `get_minutes()` and `get_hours()`.

The primary function, `str_to_seconds()`, also performs these checks
before combining the helper functions:

``` python
return get_hours(time) * 3600 + get_minutes(time) * 60 + get_seconds(time)
```

This demonstrates reuse of the format-checking function as part of
several function preconditions.

## Testing the Time Functions

### `tests(10).py`

The test script contains procedures for:

``` python
test_iso_8601()
test_get_seconds()
test_get_minutes()
test_get_hours()
test_str_to_seconds()
```

As in the preceding project, the test procedures are called in the
intended implementation order.

### Valid Format Tests

Examples expected to satisfy `iso_8601()` include:

``` text
00:00:00
12:35:15
```

### Malformed Format Tests

The test suite also specifies that malformed strings should produce
`False`, including:

``` text
3:302:05
33:0:205
aa:59:59
23:aa:59
23:59:aa
```

These cases test several structural requirements:

-   Correct positions for colons
-   Digits in the hours field
-   Digits in the minutes field
-   Digits in the seconds field

The expected behavior in these tests reflects the function
specification. As noted above, the uploaded implementation's internal
assertion may instead raise an `AssertionError` for some of these
malformed inputs.

## Error Detection and Preconditions

Project 4 illustrates two related but distinct ideas.

### Runtime Errors

The fraction exercise is designed to expose errors and encourage
examination of Python's error messages.

The goal is to understand where execution failed and what information
the error provides.

### Precondition Violations

The later exercises deliberately check assumptions before continuing:

``` python
assert type(s) == str
```

and:

``` python
assert len(time) == 8
```

These checks make the requirements described in the function
specifications executable.

## Diagnostic Messages

The two versions of `second_in_list()` illustrate an improvement in
error reporting.

A general message such as:

``` text
Precondition violation
```

indicates that something is wrong.

A more descriptive message such as:

``` text
The value ... is not a string.
```

provides additional information that can help locate the problem.

## Validation and Computation

The final exercise begins to separate two responsibilities:

**Validation**

``` python
iso_8601(time)
```

determines whether the string has the expected structure.

**Computation**

``` python
get_hours(time)
get_minutes(time)
get_seconds(time)
str_to_seconds(time)
```

extract and calculate values from the time string.

The time-processing functions call the validation function as part of
their precondition checks.

## Requirements

-   Python 3
-   `introcs`

No other external packages are used in the supplied files.

## Running the Exercises

The course files use module names such as:

``` python
import func
```

and:

``` python
import funcs
```

The numbered filenames in this repository preserve different stages of
the coursework. To execute a particular test script in the original
arrangement, the corresponding implementation module must be available
under the name expected by that test.

For example:

``` bash
python tests.py
```

runs the test procedures for the applicable stage.

The fraction module can also be run directly after uncommenting the
function calls indicated in the source.

## Key Concepts

### Error Messages

Python errors provide information about the type and location of a
failure. The first exercise deliberately creates opportunities to
practice interpreting those messages.

### Assertions

Assertions encode assumptions that should be true when a function is
called:

``` python
assert condition
```

If the condition is false, Python raises an `AssertionError`.

### Preconditions

The project converts requirements from function documentation into
executable checks. Examples include requiring a string argument,
requiring enough commas, and requiring an eight-character time
representation.

### Defensive Programming

Checking assumptions before performing the main computation helps detect
invalid usage closer to its source.

### Input Validation

The `iso_8601()` exercise breaks a structured input into individual
conditions that can be checked separately.

### Reuse

Instead of repeating all format checks inside every time-processing
function, the project introduces a common `iso_8601()` function that the
other functions can call.

## Project Structure

``` text
Project-4/
├── funcs(7).py
├── func(4).py
├── tests(9).py
├── func(5).py
├── funcs(8).py
├── tests(10).py
└── README.md
```

## Author

Amelia Litvak

## Course

Cornell CIS 552
