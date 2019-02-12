# S-expression calculator
=======================

This is a command line program that acts as a simple calculator: it takes a
single argument as an expression and prints out the integer result of
evaluating it.

Invocations look like:

    $ ./calc.py 123
    123

    $ ./calc.py "(add 12 12)"
    24

Expression syntax
-----------------

Since the expression is passed in as a command line argument, it is a string.
The syntax resembles [S-expressions][sexp] but the rules are simplified. An
expression can be in one of two forms:

### Integers

An integer is just a sequence of base 10 digits. For example:

    "123"

### Function calls

A function call takes the following form:

    (FUNCTION EXPR EXPR)

A function call is always delimited by parenthesis `(` and `)`.

The `FUNCTION` is one of `add` or `multiply`.

The `EXPR` can be any arbitrary expression, i.e. it can be further function
calls or integer expressions.

Whitespace is used to delimit the expressions but is otherwise ignored.

For example:

    "(add 123 456)"

    "(multiply (add 1 2) 3)"

Expression grammar
------------------

A formal grammar specified in [EBNF][ebnf]:

    DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";

    EXPR = INTEGER | ADD | MULTIPLY;

    INTEGER = DIGIT, { DIGIT };

    ADD = "(", "a", "d", "d", " ", EXPR, " ", EXPR, ")";

    MULTIPLY = "(", "m", "u", "l", "t", "i", "p", "l", "y", " ", EXPR, " ", EXPR, ")";

Expression semantics
--------------------

The goal is to write an integer calculator that supports the `add` and
`multiply` functions. The program should take an expression string as a command
line argument and print out the result of evaluating the expression.

The examples follow the convention:

    "INPUT"
    => OUTPUT

Where `INPUT` is the expression string passed as a single argument and `OUTPUT`
is the output printed to stdout by your program.

### Integers

Integers should be evaluated as the number they represent:

    "123"
    => 123

    "0"
    => 0

### Add

The `add` function should:

1. accept exactly 2 sub-expressions
2. fully evaluate the 2 sub-expressions
3. return the result of adding the 2 sub-expressions together

```
"(add 1 1)"
=> 2

"(add 0 (add 3 4))"
=> 7

"(add 3 (add (add 3 3) 3))"
=> 12
```

### Multiply

The `multiply` function should:

1. accept exactly 2 sub-expressions
2. fully evaluate the 2 sub-expressions
3. return the result of multiplying the 2 sub-expressions together

```
"(multiply 1 1)"
=> 1

"(multiply 0 (multiply 3 4))"
=> 0

"(multiply 2 (multiply 3 4))"
=> 24

"(multiply 3 (multiply (multiply 3 3) 3))"
=> 81
```

Examples
--------

Besides the examples already provided above, it should be possible to mix and
match integers and function calls to build arbitrary calculations:

    "(add 1 (multiply 2 3))"
    => 7

    "(multiply 2 (add (multiply 2 3) 8))"
    => 28

Assumptions
-----------

A list of assumptions:

- Since numbers are specified by digits only, It doesn't have to deal with
  inputting negative numbers.
- There will always be a single space between the function arguments.

  The tested examples cover:

  - Parenthesis are always be balanced.
  - Only the `add` and `multiply` functions are called.
  
[sexp]: https://en.wikipedia.org/wiki/S-expression
[ebnf]: https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form
