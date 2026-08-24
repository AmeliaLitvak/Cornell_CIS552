# Cornell CIS 552: Python Functions, Testing, and Debugging
      
## Overview

This repository contains coursework and projects from Cornell
University's **CIS 552**, taught by Professor Walker White. The course
focuses on one of the core elements of Python programming:
**functions**.

Functions initiate actions, organize information, simplify programs, and
can serve many different purposes. Because they are multipurpose,
programmers need to understand not only how to call functions, but also
how to design them so that a program behaves as intended.

The course develops those skills through specification writing, function
design, testing, debugging, error interpretation, assertions, and
string-processing exercises. It emphasizes the programming skills and
technical vocabulary needed to work with Python in a business context.

## Course Goals

During the course, students learn to:

-   Identify how functions work
-   Build a technical vocabulary
-   Visualize Python executions
-   Follow rules for writing functions
-   Recognize a properly formatted specification
-   Identify strategies for effective debugging
-   Turn an English description into code
-   Read and interpret error messages
-   Write informative error messages

## Repository Projects

This repository is organized around five projects that progressively
develop the course concepts.

### Project 1: Functions, Procedures, and Dice

Project 1 introduces the transition from simple Python scripts to
reusable functions.

The exercises use dice simulations to explore:

-   User input
-   Random number generation
-   Procedures
-   Functions and return values
-   Parameters
-   Default arguments
-   Global variables
-   Boolean return values
-   Function decomposition
   
The project culminates in a simple two-player dice roll-off that
separates dice generation from the game logic.

### Project 2: Testing and String Functions

Project 2 introduces systematic testing and debugging through small
string-processing functions.

Topics include:

-   Assertions
-   Expected vs. actual results
-   Positive and negative test cases
-   Test procedures
-   Vowel detection
-   Position-sensitive string behavior
-   String searching and slicing
-   Replacing the first occurrence of a substring
-   Separating implementation code from testing code

The exercises demonstrate how a function specification can guide the
creation of useful test cases.

### Project 3: Function Design and Decomposition

Project 3 focuses on developing functions from specifications and
breaking larger problems into smaller components.

Topics include:

-   Function stubs
-   Specification-driven development
-   Backwards design
-   Incremental implementation
-   String parsing
-   Delimiter searching
-   Whitespace removal
-   Helper functions
-   Functional decomposition
-   Dependency-aware testing

The final exercise parses an `hh:mm:ss` time string with separate helper
functions for hours, minutes, and seconds before converting the complete
time to seconds since midnight.

### Project 4: Errors, Assertions, and Input Validation

Project 4 shifts the emphasis toward debugging and defensive
programming.

The exercises cover:

-   Reading Python error messages
-   Diagnosing runtime failures
-   Preconditions
-   Assertions
-   Descriptive assertion messages
-   Type checking
-   Structured input validation
-   Reusing validation logic
-   Testing malformed inputs

The project extends earlier string and time-processing functions by
turning documented assumptions into executable checks.

### Project 5: Parentheses and String Processing

Project 5 serves as the course project and combines many of the
techniques developed throughout the course.

It implements functions that:

-   Determine whether a string contains an opening parenthesis followed
    by a closing parenthesis
-   Extract the substring between the first opening parenthesis and the
    first subsequent closing parenthesis

The project brings together:

-   Function specifications
-   Preconditions
-   Assertions
-   Boolean expressions
-   String searching
-   Sentinel values
-   String slicing
-   Edge-case testing

The exercises intentionally follow the exact behavior defined by their
specifications rather than implementing a general balanced-parentheses
parser.

## Learning Progression

The five projects form a progression from basic function use to
specification-driven and defensively programmed functions:

``` text
Basic Python Statements
        ↓
Procedures and Functions
        ↓
Parameters and Return Values
        ↓
Testing and Assertions
        ↓
Specifications
        ↓
Backwards Design
        ↓
Helper Functions
        ↓
Functional Decomposition
        ↓
Error Interpretation
        ↓
Preconditions
        ↓
Input Validation
        ↓
Course Project
```

## Function Specifications

A major theme throughout the course is that a function should have a
clearly defined contract.

The project docstrings commonly describe:

-   What the function returns
-   How the function behaves
-   Examples of expected behavior
-   Parameters
-   Preconditions

These specifications provide a bridge between an English description of
a problem and its Python implementation.

They also provide a basis for testing: expected behavior described in a
specification can be translated into assertions in a test script.

## Testing

Testing becomes increasingly important as the projects progress.

The coursework uses the `introcs` package and assertions such as:

``` python
introcs.assert_equals(expected, result)
```

Implementation and testing are generally kept in separate modules. Later
projects organize related tests into dedicated procedures such as:

``` python
test_has_a_vowel()
test_second_in_list()
test_get_hours()
test_matching_parens()
```

Tests include both typical inputs and edge cases designed to clarify the
precise behavior required by the function specification.

## Debugging and Error Messages

The course explicitly develops strategies for effective debugging.

Rather than treating an error message simply as a failure, the exercises
encourage reading and interpreting the information Python provides.
Later exercises add assertions and increasingly informative messages so
that invalid function usage can be identified more clearly.

This progression connects several related skills:

``` text
Observe unexpected behavior
        ↓
Read the error message
        ↓
Identify the source of the problem
        ↓
Understand the violated assumption
        ↓
Express assumptions as preconditions
        ↓
Enforce them with assertions
        ↓
Provide useful diagnostic information
```

## Backwards Design

Several exercises use backwards design to translate an English
specification into working code.

Instead of attempting to solve an entire problem in a single step, the
desired output is considered first and the intermediate operations
required to produce it are identified.

For example, extracting an item from a comma-separated string can be
decomposed into:

``` text
Find delimiter
      ↓
Find next delimiter
      ↓
Extract substring
      ↓
Remove surrounding whitespace
      ↓
Return result
```

This approach helps turn a written specification into a sequence of
manageable programming operations.

## Functional Decomposition

The course also emphasizes breaking larger functions into smaller helper
functions.

The time-conversion project demonstrates this structure:

``` text
              str_to_seconds()
                     |
        +------------+------------+
        |            |            |
   get_hours()  get_minutes()  get_seconds()
```

Each helper performs one specific task and can be implemented and tested
independently before being used by the primary function.

## Repository Structure

``` text
CIS-552/
├── Project-1/
│   ├── Python source files
│   └── README.md
│
├── Project-2/
│   ├── Python source and test files
│   └── README.md
│
├── Project-3/
│   ├── Python source and test files
│   └── README.md
│
├── Project-4/
│   ├── Python source and test files
│   └── README.md
│
├── Project-5/
│   ├── Python source and test files
│   └── README.md
│
└── README.md
```

Each project directory contains its own README with a more detailed
explanation of the source files, implementation, tests, and concepts
demonstrated in that stage of the course.

## Technologies

-   Python 3
-   `introcs`
-   Python standard library, including `random`
-   Anaconda
-   Python code editor

The course recommends installing Anaconda and a Python code editor.
Pulsar is one of the recommended editors.

## Course Environment

The original course includes a virtual programming environment.
According to the course guidance, that environment should be accessed
from a computer rather than a tablet or mobile device.

Recommended browser/platform combinations include:

-   Chrome or Edge on Windows
-   Chrome or Firefox on macOS

Safari is not supported by the course's virtual programming environment.

## Key Skills Demonstrated

By completing the projects in this repository, the coursework develops
experience with:

-   Python function definition and invocation
-   Parameters and arguments
-   Return values
-   Procedures
-   Default parameters
-   Global variables
-   Function specifications
-   Preconditions
-   Assertions
-   Unit-style testing
-   Debugging
-   Error interpretation
-   Informative error messages
-   String searching
-   String indexing and slicing
-   String manipulation
-   Boolean expressions
-   Helper functions
-   Functional decomposition
-   Backwards design
-   Input validation
-   Translating written requirements into code

## Author

Amelia Litvak

## Course

**Cornell University CIS 552**

Instructor: **Professor Walker White**
