# Project 2: Testing and String Functions

## Overview

Project 2 focuses on testing, debugging, and string manipulation in
Python. The exercises use small string-processing functions together
with dedicated test scripts to demonstrate how expected behavior can be
checked systematically with assertions.

The project progresses from testing a function that identifies vowels,
to organizing tests into reusable test procedures, to implementing and
testing a function that replaces the first occurrence of a substring.

## Learning Objectives

This project demonstrates:

-   Writing test cases for Python functions
-   Using assertions to compare expected and actual results
-   Selecting both positive and negative test cases
-   Organizing tests into dedicated test procedures
-   Testing boundary and position-sensitive behavior
-   Working with Python strings and substrings
-   Using string slicing
-   Finding the position of a substring
-   Replacing only the first occurrence of a substring
-   Using function specifications, examples, parameters, and
    preconditions to guide testing
-   Separating implementation code from testing code

## Project Files

The uploaded files consist of three versions of `funcs.py` and three
corresponding versions of `tests.py`. The numbered filenames preserve
the separate stages of the project.

### Stage 1: Testing `has_a_vowel`

#### `funcs(3).py`

Defines:

``` python
has_a_vowel(s)
```

The function returns `True` when the supplied lowercase string contains
at least one of the vowels:

``` text
a, e, i, o, u
```

The letter `y` is explicitly excluded.

The function specification states that `s` must be a non-empty string
containing lowercase letters.

#### `tests(3).py`

Provides a collection of tests for `has_a_vowel()` using
`introcs.assert_equals`.

The tests include strings that:

-   Contain multiple vowels
-   Contain a single vowel
-   Contain no standard vowels
-   Contain `y`
-   Contain vowels in different positions

Examples include:

``` python
funcs.has_a_vowel('aeiou')
funcs.has_a_vowel('hat')
funcs.has_a_vowel('xxx')
funcs.has_a_vowel('fly')
funcs.has_a_vowel('fling')
```

The script prints:

``` text
Module funcs is working correctly
```

after all assertions complete successfully.

## Stage 2: Testing Multiple Functions

### `funcs(4).py`

Expands the string-checking module to contain two functions:

``` python
has_a_vowel(s)
has_y_vowel(s)
```

`has_a_vowel()` retains the behavior from the previous stage.

`has_y_vowel()` tests whether `y` occurs in what the function
specification calls a "vowel position." In this exercise, `y` counts as
a vowel only when it is not the first character of the string.

The implementation therefore searches the portion of the string after
its first character:

``` python
return 'y' in s[1:]
```

### `tests(4).py`

Reorganizes the tests into two dedicated testing procedures:

``` python
test_has_a_vowel()
test_has_y_vowel()
```

This structure separates the tests for each function and makes the test
script easier to organize as the module grows.

The `has_y_vowel()` tests exercise important positional cases. For
example:

``` python
funcs.has_y_vowel('young')
```

should return `False` because the `y` occurs only in the first position,
while:

``` python
funcs.has_y_vowel('wheely')
funcs.has_y_vowel('yoyo')
```

should return `True` because they contain a `y` after the first
character.

The script calls both test procedures before reporting that the module
is working correctly.

## Stage 3: String Manipulation

### `funcs(5).py`

Introduces:

``` python
replace_first(word, a, b)
```

The function returns a copy of `word` in which the **first occurrence**
of substring `a` is replaced with substring `b`.

For example:

``` python
replace_first('crane', 'a', 'o')
```

returns:

``` text
crone
```

and:

``` python
replace_first('poll', 'l', 'o')
```

returns:

``` text
pool
```

The implementation uses `introcs.find_str()` to determine the position
of the target substring. It then divides the original string into the
portion before the target and the portion after it:

``` python
pos = introcs.find_str(word, a)
before = word[:pos]
after = word[pos+len(a):]
result = before+b+after
```

This approach demonstrates how slicing and concatenation can be combined
to construct a new string.

### `tests(5).py`

Defines the test procedure:

``` python
test_replace_first()
```

The test suite checks a variety of replacement situations, including:

-   Replacing a single character
-   Replacing a multi-character substring
-   Replacing a substring at the beginning of a string
-   Case-sensitive replacement
-   Replacing text containing special characters and digits
-   Replacing one character with a longer string
-   Replacing a character with an empty string

One particularly useful test is:

``` python
funcs.replace_first('aaaa', 'a', 'bb')
```

which expects:

``` text
bbaaa
```

This confirms that only the **first** occurrence is replaced.

Another test:

``` python
funcs.replace_first('a', 'a', '')
```

expects an empty string, demonstrating that the replacement substring
may itself be empty.

## Testing Approach

A central theme of Project 2 is the relationship between a function's
specification and its tests.

The test scripts import both the function module and the `introcs`
package:

``` python
import introcs
import funcs
```

Expected results are compared with actual results using:

``` python
introcs.assert_equals(expected, result)
```

If an assertion fails, the test identifies behavior that does not match
the expected result. If all assertions succeed, the test script reaches
its final success message.

The project also demonstrates how testing evolves as software grows. The
initial tests are written directly as script code, while the later
versions group related assertions into functions such as:

``` python
test_has_a_vowel()
test_has_y_vowel()
test_replace_first()
```

This creates a clearer separation between individual units of
functionality and their corresponding tests.

## Requirements

-   Python 3
-   `introcs`
-   Python files from the corresponding stage of the project

The project uses Cornell's `introcs` module for assertion helpers and
string functionality.

## Running the Tests

The source files are presented as sequential versions of `funcs.py` and
`tests.py`. In their original course structure, each matching pair is
intended to operate with the names:

``` text
funcs.py
tests.py
```

The test module imports:

``` python
import funcs
```

so the appropriate function file must be available as `funcs.py` when
running that stage.

A test script can then be run with:

``` bash
python tests.py
```

When all tests pass, the script reports:

``` text
Module funcs is working correctly
```

## Key Concepts

### Unit Testing

Each function is tested independently against known inputs and expected
outputs. This makes it possible to determine whether a small unit of the
program satisfies its specification.

### Assertions

Assertions automate comparisons between expected and actual behavior.
Instead of visually inspecting every result, the tests fail when the
implementation produces an unexpected value.

### Test Case Selection

The tests do more than demonstrate normal behavior. They exercise
different categories of inputs, including strings with and without
vowels, different positions for `y`, multi-character substrings, case
differences, and empty replacement strings.

### String Slicing

`replace_first()` demonstrates Python slicing:

``` python
word[:pos]
word[pos+len(a):]
```

These expressions isolate the portions before and after the substring
being replaced.

### Function Specifications and Preconditions

The provided docstrings specify what each function should return and
what conditions its parameters must satisfy. The tests are designed
around those documented expectations.

## Project Structure

``` text
Project-2/
├── funcs(3).py
├── tests(3).py
├── funcs(4).py
├── tests(4).py
├── funcs(5).py
├── tests(5).py
└── README.md
```

## Author

Amelia Litvak

## Course

Cornell CIS 552
