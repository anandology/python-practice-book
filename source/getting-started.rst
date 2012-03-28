Getting Started
---------------

Python is a high-level programming language that can be used for many kinds of software development. It is often compared with lisp in its power of expression. Many Python programmers report substantial productivity gains and feel the language encourages the development of higher quality, more maintainable code.

==========================
Using Python as calculator
==========================

Python comes with an interactive interpreter. When you type ``python`` in your shell, the python interpreter becomes active with a ``>>>`` prompt and awaits for your commands.

.. code-block:: python

    $ python
    Python 2.4.3 (#1, Mar 30 2006, 11:02:15) 
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Now you can type any valid python expression at the prompt. python reads the typed expression, evaluates it and prints the result.

Lets start using python as a simple calculator. 

    >>> 2 + 3
    5
    >>> 0.5 * 3
    1.5

The + and * operators have their usual meaning, add and multiply.

Lets look at some more examples.

    >>> 2 + 3 * 4
    14
    >>> 3 * 4 + 2
    14

No matter what order you write the expression, multiplication is always performed before addition. This is because in python ``*`` operator has higher precedence than ``+``. 

Parenthesis can be used for grouping expressions.

    >>> (2 + 3) * 4
    20

In python, strings can be handled as easily as numbers.

    >>> 'hello, world!'
    'hello, world!'
    >>> 'hello,' + ' world!'
    'hello, world!'
    >>> 'hello' * 2
    'hellohello'
    
Strings can be enclosed in "double quotes" or 'single quotes'. 
It is also possible to write multiline strings using 3 double quotes or 3 single quotes. 

===========
Assignments
===========

It is possible to associate a name with a value. This is called assignment. Often the associated name is called a *variable*.

    >>> x = 4
    >>> x * x
    16

If you try to use a name that is not associated with any value, python gives an error message.

    >>> foo
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    NameError: name 'foo' is not defined
    >>> foo = 4
    >>> foo
    4

If you reassign a different value to an existing variable, the new value overwrites the old value.

    >>> x = 4
    >>> x
    4
    >>> x = 'hello'
    >>> x
    'hello'
 
It is possible to do multiple assignments at once.

    >>> a, b = 1, 2
    >>> a
    1
    >>> b
    2
    >>> a + b
    3

Swapping values of 2 variables in python is very simple.

    >>> a, b = 1, 2
    >>> a, b = b, a
    >>> a
    2
    >>> b
    1

When executing assignments, python evaluates the right hand side first and then assigns those values to the variables specified in the left hand side.

.. problem:: What will be the values of ``a`` and ``b`` after executing the following statements?

   >>> a, b = 0, 1
   >>> a, b = b, a+b

.. problem::  What will be the value of ``b`` after executing the following statements?

    >>> a = 1
    >>> b = a
    >>> a = 2

=================
Executing scripts
=================

Instead of writing python code in the interpreter, it is also possible to write it in a file and ask ``python`` to execute it.

.. code-block:: python

    $ cat square.py
    x = 4
    y = x * x
    print y
    $ python square.py
    16
    $
    
Unlike in the interpreter, script execution will not print the values of the expressions automatically. The ``print`` statement should be used explicitly.

For example, the following script will not print anything.

.. code-block:: python

    $ cat foo.py
    4 * 4
    $ python foo.py
    $

============
Conditionals
============

The expressive power of a language is very limited unless there is a way to make tests and perform different operations based on the result of a test.

Result of a test in python is a boolean value. Python has 2 boolean values, ``True`` and ``False``,  to represent truth and falsehood respectively.

Here are some examples of numeric comparisons.

    >>> 4 < 3
    False
    >>> 3 < 4
    True
    >>> a = 2
    >>> a + a == a * a
    True

Boolean expressions can be combined with ``and``, ``or`` and ``not`` operators.

    >>> True and False
    False
    >>> True or False
    True
    >>> not False
    True
    >>> x = 9
    >>> x % 3 == 0 or x % 5 == 0
    True
    
The ``if`` statement is used to execute a piece of code only when a boolean expression is true.

    >>> x = 42
    >>> if x % 2 == 0: print 'even'
    even
    >>>

In this example, ``print 'even'`` is executed only when ``x % 2 == 0`` is ``True``. 

The code associated with ``if`` can be written as a separate indented block of code, which is often the case when there are more than one statement to be executed.    

    >>> if x % 2 == 0:
    ...     print 'even'
    ...
    even
    >>>

Notice the indentation. Python uses indentation to identify code blocks.
The ``...`` is the secondary prompt, which python uses to denote that it is expecting some more input.

The ``if`` statement can have optional ``else`` clause, which is executed when the boolean expression is ``False``.

    >>> x = 3
    >>> if x % 2 == 0:
    ...     print 'even'
    ... else:
    ...     print 'odd'
    ...
    odd
    >>>

The ``if`` statement can have optional ``elif`` clauses when there are more conditions to be checked. The ``elif`` keyword is short for ``else if``, and is useful to avoid excessive indentation.
        
    >>> x = 42
    >>> if x < 10: 
    ...        print 'one digit number'
    ... elif x < 100:
    ...     print 'two digit number'
    ... else: 
    ...     print 'big number'
    ...
    two digit number
    >>>

.. problem :: What happens the following code is executed? Will it give any error? Explain the reasons.

.. code-block:: python

    x = 2
    if x == 2:
        print x
    else:
        print y

.. problem :: What happens the following code is executed? Will it give any error? Explain the reasons.

.. code-block:: python

    x = 2
    if x == 2:
        print x
    else:
        x +

=========
Functions
=========

Just like a value can be associated with a name, a piece of logic can also be associated with a name by defining a function. Lets look at some built-in functions before we start writing our own.

The built-in function ``min`` finds the minimum value from the given numbers.

    >>> min(5, 4)
    4

A function takes a list of values, called arguments, as input and returns the computed result back. In this example, the ``min`` function has taken 2 arguments, ``5`` and ``4`` and returned ``4``.

Now, lets define a function to compute square of a number.

    >>> def square(x):
    ...     return x * x
    ...
    >>>

The keyword ``def`` is used to define a function and it must be followed by the function name and parenthesized list of formal parameters. Formal parameters are the names used to access the arguments passed when the function is called. Just like the ``if`` statement, body of the function must be indented. The ``return`` keyword is used to specify the return value.

Lets see what happens when we call the ``square`` function.

    >>> square(4)
    16

Arguments to a function can also be expressions, which are evaluated before the function is called.

    >>> a = 1
    >>> square(a + 2)
    9
    
Functions calls can be used in any expressions.

    >>> 1 + square(2) + square(3) - 2
    12

Function calls can be nested.

    >>> square(square(4))
    256

New functions can be defined using existing functions.

    >>> def sum_of_squares(a, b):
    ...     return square(a) + square(b)
    ...
    >>> sum_of_squares(2, 3)
    13
    
Functions are not really very different from numbers and strings. They can be assigned to variables and passed as arguments to other functions.

    >>> square
    <function square at 0x7a930>
    >>> sqr = square
    >>> sqr
    <function square at 0x7a930>
    >>> sqr(4)
    16
    >>> def magic(f):
    ...     return f(2) + f(3)
    ...
    >>> magic(square)
    13

The ``lambda`` keyword can be used to create small anonymous functions.

	>>> f = lambda x: x+1
	>>> f(4)
	5
	>>> magic(lambda x: x*x)
	13

We can also pass named arguments to a function.

	>>> def sub(a, b): return a-b
	...
	>>> sub(4, 2)
	2
	>>> sub(a=4, b=2)
	2
	>>> sub(b=2, a=4)
	2
	
It is possible to specify default values for arguments.

	>>> def join(a, b, delim=' '):
	...	    return a + delim + b
	>>> join('hello, 'world', ',')
	'hello,world'
	>>> join('hello', 'world')
	'hello world'
    
You might have already noticed that the names used inside function need not be different from the names used outside.

    >>> x = 1
    >>> y = 2
    >>> def f(x):
    ...        y = x + x
    ...     return y
    ...
    >>> f(4)
    8
    >>> x
    1
    >>> y
    2
    
Python manages variables inside a function separately from the variables outside. The variables defined inside a function are called local variables and the variables defined outside are called global variables. The formal parameters are also considered as local variables. While finding value of a variable, python first tries to look for a local variable with that name and if doesn't find then it looks in the global variables.

    >>> x = 1
    >>> y = 2
    >>> def f(x):
    ...        z = x + y # here x is local and y is global
    ...        return z
    >>> f(4)
    6
    >>> y = 6
    >>> f(5)
    11

However, to modify a global variable, it must be declared as global inside the function definition.

    >>> y = 1
    >>> def f(x):
    ...        global y
    ...        y = y + x
    >>> f(2)
    >>> y
    3

.. problem :: How many times the ``+`` and ``*`` operations are performed in evaluating the following expression.

    >>> sum_of_squares(1+1, 1+2)
    13

.. problem :: Write a function ``absolute`` to compute absolute value of a number.

     >>> absolute(4)
     4
     >>> absolute(-3)
     3
     >>> absolute(0)
     0

.. problem :: Write functions ``minimum`` and ``maximum`` to compute minimum and maximum values of 2 given numbers respectively.

    >>> minimum(2, 3)
    2
    >>> mininum(3, -2)
    -2
    >>> maximum(2, 3)
    3
    >>> maximum(3, -2)
    3

.. problem :: What happens if you pass 2 strings as arguments to the ``minimum`` and ``maximum`` functions defined in the above problem? Explain why.

.. problem :: A novice programmer has tried to implement ``absolute`` function using a function ``newif`` instead of using the ``if`` statement directly.

    >>> def newif(condition, if_value, else_value)
    ...     if condition: 
    ...         return if_value
    ...     else:
    ...         return else_value
    ...
    >>> def absolute(a):
    ...     return newif(a > 0, a, -a)
    ...

Do you see any problem with the ``newif`` function? Can you give an example where the ``newif`` function and the ``if`` statement behave differently?

.. problem :: What will the output of calling function ``g`` in the following 2 places. Justify your answer.

    >>> def f(x): return x + x
    >>> def g(): return f(5)
    >>> g()
    ???
    >>> def f(x): return x * x
    >>> g()
    ???
    
.. problem :: Can you implement ``swap`` function in python?

=======
Modules
=======

Just like functions allow us to group and reuse a piece of logic, modules allow us to group and reuse useful functions in other programs  

--Just like we can write scripts and execute them multiple times, we can write useful functions --in a file and reuse them in other scripts and interpreter. 

To reuse the function in 
Suppose you want to reuse the square function that we have written previously. We can write that in a file square.py. 

which can be imported 

    - what is a module
    - import

Python provides a way of documenting code. 

    - docstrings and pydoc
    - __name__
    - doctest

.. code-block:: python

    $ cat square.py
    """Square module."""

    def square(x):
        """Squares a number.

            >>> square(4)
             16
            >>> square(-3)
            9
        """
        return x * x

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
    $ python square.py
    $
    
We shall use doctests for all problems we are going to solve from now on.

.. problem :: Write a module ``number.py`` with ``minimum`` and ``maximum`` functions from the previous problems and add doctests to it.
