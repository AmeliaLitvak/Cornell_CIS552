# Project 5: Parentheses and String Processing

## Overview

Project 5 is the course project and brings together several programming
techniques developed in the earlier exercises. The project implements
and tests two related functions for identifying and extracting
information from parentheses within strings.

The first function, `matching_parens(s)`, determines whether a string
contains an opening parenthesis followed by a closing parenthesis. The
second function, `first_in_parens(s)`, returns the substring located
between the first opening parenthesis and the first closing parenthesis
that follows it.

The project emphasizes function specifications, preconditions,
assertions, string searching, slicing, Boolean expressions, and
systematic testing of normal and unusual inputs.

## Learning Objectives

This project demonstrates:

-   Translating function specifications into Python code
-   Searching strings for specific characters
-   Interpreting search results and sentinel values
-   Constructing Boolean expressions
-   Using assertions to enforce preconditions
-   Extracting substrings with slicing
-   Distinguishing a specified behavior from more general parentheses
    matching
-   Designing tests for normal, boundary, and unusual inputs
-   Applying concepts from previous projects in a compact course project

## Project Files

### `funcs(9).py`

Contains the two functions implemented for the course project:

``` python
matching_parens(s)
first_in_parens(s)
```

### `tests(20260824-171622).py`

Contains dedicated test procedures for both functions:

``` python
test_matching_parens()
test_first_in_parens()
```

The script executes both test procedures and reports that the module is
working correctly if all assertions succeed.

## `matching_parens(s)`

The function:

``` python
matching_parens(s)
```

returns `True` when the string contains what the project specification
defines as a matching pair of parentheses.

For this project, a matching pair consists of:

1.  An opening parenthesis `(`
2.  A closing parenthesis `)` occurring after that opening parenthesis

Anything may appear between those two characters, including additional
parentheses.

Examples from the specification include:

``` python
matching_parens('A (B) C')
```

returning:

``` text
True
```

and:

``` python
matching_parens('A )B( C')
```

returning:

``` text
False
```

### Implementation

The function first enforces its documented type precondition:

``` python
assert type(s) == str
```

It then searches for the first opening parenthesis:

``` python
first_open_paren = introcs.find_str(s, '(')
```

Next, it searches for a closing parenthesis beginning from the position
of that opening parenthesis:

``` python
first_closed_paren = introcs.find_str(s, ')', first_open_paren)
```

Finally, it returns whether both searches produced valid positions:

``` python
return first_open_paren != -1 and first_closed_paren != -1
```

The value `-1` indicates that the requested character was not found.

## Testing `matching_parens`

The test suite includes both successful and unsuccessful cases.

### Matching Cases

Examples expected to return `True` include:

``` text
(X) Y Z
(()) 1 2
()
(A)(S)(D)
```

These cases test simple pairs, additional parentheses, an otherwise
empty pair, and multiple pairs.

### Non-Matching Cases

Examples expected to return `False` include:

``` text
A )B( C
<empty string>
((
rggn
```

These cases test:

-   A closing parenthesis appearing before the opening parenthesis
-   An empty string
-   Opening parentheses without a closing parenthesis
-   A string containing no parentheses

Together, the tests clarify the precise definition of "matching" used by
this project.

## `first_in_parens(s)`

The second function:

``` python
first_in_parens(s)
```

returns the substring between the first opening parenthesis and the
first closing parenthesis that follows it.

For example:

``` python
first_in_parens('A (B) C')
```

returns:

``` text
B
```

and:

``` python
first_in_parens('A (B) (C)')
```

returns:

``` text
B
```

The second pair is irrelevant because the function only processes the
first pair as defined by its specification.

## Implementation of `first_in_parens`

The function first verifies that the argument is a string:

``` python
assert type(s) == str
```

It finds the first opening parenthesis:

``` python
first_open_paren = introcs.find_str(s, '(')
```

and then searches for the first closing parenthesis following that
position:

``` python
first_closed_paren = introcs.find_str(s, ')', first_open_paren)
```

The function asserts that both positions were found:

``` python
assert first_open_paren != -1 and first_closed_paren != -1
```

It then extracts the substring between them:

``` python
in_parens = s[first_open_paren+1:first_closed_paren]
```

and returns the result.

## Parentheses Interpretation

An important detail of Project 5 is that these functions do **not**
implement a general balanced-parentheses algorithm.

For example, the specification states:

``` python
first_in_parens('A ((B) (C))')
```

returns:

``` text
(B
```

The function finds:

``` text
A ((B) (C))
   ^  ^
   |  |
 first (
      first following )
```

and returns the characters between those two positions.

It does not attempt to determine which closing parenthesis would form a
structurally balanced nested pair.

This behavior is intentional according to the function specification and
tests.

## Testing `first_in_parens`

The test procedure includes several useful cases.

### Simple Content

``` python
first_in_parens('(X) Y Z')
```

expects:

``` text
X
```

### Parenthesis Inside the Extracted Content

``` python
first_in_parens('(() 1 2 ')
```

expects:

``` text
(
```

This demonstrates that another opening parenthesis may appear between
the first opening and first subsequent closing parenthesis.

### Whitespace

``` python
first_in_parens('(A A) (B) C')
```

expects:

``` text
A A
```

Whitespace inside the parentheses is preserved.

### Nested-Looking Content

``` python
first_in_parens('(X(Q) (Y) (Z)')
```

expects:

``` text
X(Q
```

Again, the function stops at the first closing parenthesis following the
initial opening parenthesis.

### Complex Input

The test:

``` python
first_in_parens(')))(1(2(3(4XXXXXXXXXX))))')
```

expects:

``` text
1(2(3(4XXXXXXXXXX
```

This case demonstrates that closing parentheses occurring before the
first opening parenthesis do not determine the extracted substring. The
search for the relevant closing parenthesis begins from the first
opening parenthesis.

## Preconditions and Assertions

The project continues the defensive-programming techniques introduced
earlier.

`matching_parens()` requires:

``` text
s is a string, possibly empty
```

and checks the type with an assertion.

`first_in_parens()` has a stronger precondition:

``` text
s is a string with a matching pair of parentheses
```

The implementation therefore checks both the type and the presence of
the required parentheses before performing the slice.

## String Searching

Both functions rely on:

``` python
introcs.find_str()
```

to identify character positions.

The project demonstrates how a search function's return value can be
used in two different ways.

In `matching_parens()`, the positions are used to construct a Boolean
result.

In `first_in_parens()`, the positions become slice boundaries for
extracting part of the string.

## String Slicing

The core extraction operation is:

``` python
s[first_open_paren+1:first_closed_paren]
```

Adding `1` to the opening-parenthesis position excludes the `(` itself.
Python's slice endpoint excludes the closing-parenthesis position
automatically.

As a result, only the characters between the two delimiters are
returned.

## Testing Strategy

The project maintains the separation between implementation and testing
used throughout the course.

The tests use:

``` python
introcs.assert_equals(expected, result)
```

to compare expected behavior with the actual function result.

The cases include:

-   Standard valid inputs
-   Empty strings
-   Missing parentheses
-   Reversed parentheses
-   Multiple pairs
-   Nested-looking parentheses
-   Whitespace
-   Strings containing several opening and closing parentheses

This variety helps establish exactly what the specifications mean by a
matching pair and the first substring inside parentheses.

## Requirements

-   Python 3
-   `introcs`

No other external packages are used by the supplied project files.

## Running the Tests

The test script imports the implementation with:

``` python
import funcs
```

The uploaded filename preserves the project version as `funcs(9).py`. In
the original course arrangement, the implementation module is expected
to be available as:

``` text
funcs.py
```

The tests can then be run with:

``` bash
python tests.py
```

When all assertions succeed, the script prints:

``` text
Module funcs is working correctly
```

## Key Concepts

### Function Specifications

The docstrings define the exact behavior expected from each function,
including cases that may differ from a more general interpretation of
parentheses matching.

### Preconditions

Assertions enforce assumptions about arguments before the main operation
proceeds.

### Boolean Logic

`matching_parens()` combines two search results into a single Boolean
expression.

### Sentinel Values

The implementation uses `-1` from unsuccessful string searches to
determine whether required characters were found.

### String Searching

`introcs.find_str()` locates delimiters within the input.

### String Slicing

The positions returned by the searches are used to extract the requested
substring.

### Edge-Case Testing

The test suite goes beyond simple examples and includes reversed,
missing, repeated, and nested-looking parentheses.

## Project Structure

``` text
Project-5/
├── funcs(9).py
├── tests(20260824-171622).py
└── README.md
```

## Author

Amelia Litvak

## Course

Cornell CIS 552
