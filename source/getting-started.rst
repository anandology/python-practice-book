Getting Started
===============

Running Python Interpreter
--------------------------

Python comes with an interactive interpreter. When you type ``python`` in your shell or command prompt, the python interpreter becomes active with a ``>>>`` prompt and waits for your commands.

.. code-block:: python

    $ python
    Python 2.7.1 (r271:86832, Mar 17 2011, 07:02:35) 
    [GCC 4.2.1 (Apple Inc. build 5664)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Now you can type any valid python expression at the prompt. python reads the typed expression, evaluates it and prints the result.

.. code-block:: python

    >>> 42
    42
    >>> 4 + 2
    6
    
.. problem :: Open a new Python interpreter and use it to find the value of ``2 + 3``.

Running Python Scripts
----------------------

Open your text editor, type the following text and save it as ``hello.py``.

.. code-block:: python

    print "hello, world!"

And run this program by calling ``python hello.py``. Make sure you change to the directory where you saved the file before doing it.

.. code-block:: python

    anand@bodhi ~$ python hello.py
    hello, world!
    anand@bodhi ~$


.. problem :: Create a python script to print  ``hello, world!`` four times.

.. problem :: Create a python script with the following text and see the output.

.. code-block:: python

    1 + 2
    
If it doesn't print anything, what changes can you make to the program to print the value?

Assignments
-----------

It is possible to associate a name with a value. This is called assignment. The associated name is usually called a *variable*.

.. code-block:: python

    >>> x = 4
    >>> x * x
    16

In this example ``x`` is a variable and it's value is `4`.

If you try to use a name that is not associated with any value, python gives an error message.

.. code-block:: python

    >>> foo
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    NameError: name 'foo' is not defined
    >>> foo = 4
    >>> foo
    4

If you reassign a different value to an existing variable, the new value overwrites the old value.

.. code-block:: python

    >>> x = 4
    >>> x
    4
    >>> x = 'hello'
    >>> x
    'hello'
 
It is possible to do multiple assignments at once.

.. code-block:: python

    >>> a, b = 1, 2
    >>> a
    1
    >>> b
    2
    >>> a + b
    3

Swapping values of 2 variables in python is very simple.

.. code-block:: python

    >>> a, b = 1, 2
    >>> a, b = b, a
    >>> a
    2
    >>> b
    1

When executing assignments, python evaluates the right hand side first and then assigns those values to the variables specified in the left hand side.

.. problem:: What will be output of the following program.

.. code-block:: python

    x = 4
    y = x + 1
    x = 2
    print x, y

.. problem:: What will be the output of the following program.

.. code-block:: python

    x, y = 2, 6
    x, y = y, x + 2
    print x, y
    
.. problem:: What will be the output of the following program.

.. code-block:: python

    a, b = 2, 3
    c, b = a, c + 1
    print a, b, c
    
Numbers
-------

We already know how to work with numbers.

.. code-block:: python
 
    >>> 42
    42
    >>> 4 + 2
    6

Python also supports decimal numbers.

.. code-block:: python
 
    >>> 4.2
    4.2
    >>> 4.2 + 2.3
    6.5

Python supports the following operators on numbers.

* ``+`` addition
* ``-`` subtraction
* ``*`` multiplication
* ``/`` division
* ``**`` exponent
* ``%`` remainder

Let's try them on integers.

.. code-block:: python
 
    >>> 7 + 2
    9
    >>> 7 - 2
    5
    >>> 7 * 2
    14
    >>> 7 / 2
    3
    >>> 7 ** 2
    49
    >>> 7 % 2
    1

If you notice, the result ``7 / 2`` is ``3`` not ``3.5``. It is because the ``/`` operator when working on integers, produces only an integer.

.. code-block:: python
 
    >>> 7.0 / 2
    3.5
    >>> 7 / 2.0
    3.5

The operators can be combined. 

.. code-block:: python
 
    >>> 7 + 2 + 5 - 3
    11
    >>> 2 * 3 + 4
    10


It is important to understand how these compound expressions are evaluated. The operators have precedence, a kind of priority that determines which operator is applied first. Among the numerical operators, the precedence of operators is as follows, from low precedence to high.

* `+`, `-`
* `*`, `/`, `%`
* `**`

When we compute ``2 + 3 * 4``, ``3 * 4`` is computed first as the precedence of ``*`` is higher than ``+`` and then the result is added to 2.

.. code-block:: python
 
    >>> 2 + 3 * 4
    14
    
We can use parenthesis to specify the explicit groups.

.. code-block:: python
 
    >>> (2 + 3) * 4
    20

All the operators except `**` are left-associcate, that means that the application of the operators starts from left to right.

.. code-block:: python

    1 + 2 + 3 * 4 + 5
      ↓
      3   + 3 * 4 + 5
              ↓
      3   +   12  + 5  
          ↓
          15      + 5
                  ↓
                 20

.. problem:: What will be output of the following program?

.. code-block:: python

    n = 5
    a = n * n + n
    b = n + n * n
    c = n * (n + n)
    d = (n * n) + n
    e = n + (n * n)
    f = (n + n) * n
    print a, b, c, d, e, f
    
.. problem:: What will be output of the following program?

.. code-block:: python

    print 5/2, 5.0/2, 5/2.0, 5/2.
    print 24/4/2, 24/4*2

.. problem:: What will be output of the following program?

.. code-block:: python
        
    print 8 / 3, 8 % 3
    print -8 / 3, -8 % 3
    print 8 / -3, 8 % -3
    print -8 / -3, -8 % -3

Conditional Expressions
-----------------------

Python provides various operators for comparing values. The result of a comparison is a boolean value, either ``True`` or ``False``.

.. code-block:: python

    >>> 2 < 3
    False
    >>> 2 > 3
    True

Here is the list of available conditional operators.

* ``==`` equal to
* ``!=`` not equal to
* ``<`` less than
* ``>`` greater than
* ``<=`` less than or equal to
* ``>=`` greater than or equal to

It is even possible to combine these operators.

.. code-block:: python

    >>> x = 5
    >>> 2 < x < 10
    True
    >>> 2 < 3 < 4 < 5 < 6
    True
    
The conditional operators work even on strings - the ordering being the lexical order.

.. code-block:: python

    >>> "python" > "perl"
    True
    >>> "python" > "java"
    True
    
There are few logical operators to combine boolean values.

* `a and b` is True only if both `a` and `b` are True.
* `a or b` is True if either `a` or `b` is True.
* `not a` is True only if `a` is False.

.. code-block:: python

    >>> True and True
    True
    >>> True and False
    False
    >>> 2 < 3 and 5 < 4
    False
    >>> 2 < 3 or 5 < 4
    True
    
.. problem:: What will be output of the following program?

.. code-block:: python

    print 2 < 3 and 3 > 1
    print 2 < 3 or 3 > 1
    print 2 < 3 or not 3 > 1
    print 2 < 3 and not 3 > 1
    
.. problem:: What will be output of the following program?

.. code-block:: python

    x = 4
    y = 5
    p = x < y or x < z
    print p
    
.. problem:: What will be output of the following program?

.. code-block:: python

    True, False = False, True
    print True, False
    print 2 < 3
    
The if statement
^^^^^^^^^^^^^^^^

The ``if`` statement is used to execute a piece of code only when a boolean expression is true.

.. code-block:: python

    >>> x = 42
    >>> if x % 2 == 0: print 'even'
    even
    >>>

In this example, ``print 'even'`` is executed only when ``x % 2 == 0`` is ``True``. 

The code associated with ``if`` can be written as a separate indented block of code, which is often the case when there is more than one statement to be executed.    

.. code-block:: python

    >>> if x % 2 == 0:
    ...     print 'even'
    ...
    even
    >>>

Notice the indentation. Python uses indentation to identify code blocks.
The ``...`` is the secondary prompt, which python interpreter uses to denote that it is expecting some more input.

The ``if`` statement can have optional ``else`` clause, which is executed when the boolean expression is ``False``.

.. code-block:: python

    >>> x = 3
    >>> if x % 2 == 0:
    ...     print 'even'
    ... else:
    ...     print 'odd'
    ...
    odd
    >>>

The ``if`` statement can have optional ``elif`` clauses when there are more conditions to be checked. The ``elif`` keyword is short for ``else if``, and is useful to avoid excessive indentation.

.. code-block:: python
        
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
    
.. problem :: What happens when the following code is executed? Will it give any error? Explain the reasons.

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

Functions
---------

Just like a value can be associated with a name, a piece of logic can also be associated with a name by defining a function. 

.. code-block:: python

    >>> def square(x):
    ...    return x * x
    ...
    >>> square(5)
    25
    
The body of the function is indented. Indentation is the Python's way of grouping statements. 

The functions can be used in any expressions.

.. code-block:: python

    >>> square(2) + square(3)
    13
    >>> square(square(3))
    81

We can even create more functions using the existing ones.

.. code-block:: python

    >>> def sum_of_squares(x, y):
    ...    return square(x) + square(y)
    ...
    >>> sum_of_squares(2, 3)
    13

Functions are just like other values, they can assigned, passed as arguments to other functions etc. 

.. code-block:: python

    >>> f = square
    >>> f(4)
    16

    >>> def fxy(f, x, y):
    ...     return f(x) + f(y)
    ...
    >>> fxy(square, 2, 3)
    13

There is another way of creating functions, using the `lambda` operator.    

.. code-block:: python

    >>> cube = lambda x: x ** 3
    >>> fxy(cube, 2, 3)
    35
    >>> fxy(lambda x: x ** 3, 2, 3)
    35

The ``lambda`` operator becomes handy when writing small functions to be 
passed as arguments etc. We'll see more of it as we get into solving more 
serious problems.

.. problem:: How many multiplications are performed when each of the following lines of code is executed?

.. code-block:: python

    print sum_of_squares(5)
    print sum_of_squares(2*5)
    
.. problem:: What will be the output of the following program?

.. code-block:: python

	x = 1
	def f():
		return x
	print x
	print f()

.. problem:: What will be the output of the following program?

.. code-block:: python

	x = 1
	def f():
		x = 2
		return x
	print x
	print f()
	print x

.. problem:: What will be the output of the following program?

.. code-block:: python

	x = 1
	def f():
		y = x
		x = 2
		return x + y
	print x
	print f()
	print x

.. problem:: What will be the output of the following program?

.. code-block:: python

    x = 2
    def f(a):
        x = a * a
        return x
    y = f(3)
    print x, y
	
Functions can be called with keyword arguments.

	>>> def difference(x, y):
	...    return x - y
	...
	>>> difference(5, 2)
	3
	>>> difference(x=5, y=2)
	3
	>>> difference(5, y=2)
	3
	>>> difference(y=2, x=3)
	3
	
And some arguments can have default values.

	>>> def increment(x, amount=1):
	...		return x + amount
	...
	>>> def increment(10)
	1
	>>> increment(10, 5)
	15
	>>> increment(10, amount=2)
	12

Built-in Functions
^^^^^^^^^^^^^^^^^^

Python provides some useful functions as built-ins. 

.. code-block:: python

    >>> min(2, 3)
    2
    >>> max(3, 4)
    4

Methods
^^^^^^^

Methods are special kind of functions that work on an object.

For example, `upper` is a method available on string objects.

.. code-block:: python

    >>> x = "hello"
    >>> print x.upper()
    HELLO
    
As already told, methods are also functions. They can be assigned to other variables can be called separately.

.. code-block:: python

    >>> f = x.upper
    >>> print f()
    HELLO
    
Strings
-------

We've already seen strings in couple of examples before.

Strings are a sequence of characters, enclosed in single quotes or double quotes.

.. code-block:: python

    >>> x = "hello"
    >>> y = 'world'
    >>> print x, y
    hello world
    
Multi-line strings can be written using three single quotes or three double quotes.

.. code-block:: python

    x = """This is a multi-line string
    written in
    three lines."""
    print x
    
    y = '''multi-line strings can be written
    using three single quote characters as well.
    The string can contain 'single quotes' or "double quotes"
    in side it.'''
    print y

String objects have some useful methods. Some of them are:

* ``center`` - center aligns a string
* ``upper`` - converts the string into upper case
* ``lower`` - converts the string into lower case
* ``title`` - converts the string into title case
* ``string`` - strips the leading and trailing white space
* ``replace`` - replace occurance of a text with given replacement
* ``count`` - counts number of occurances of a char or string inside the given string
    
Try try some of them.

.. code-block:: python

    >>> "hello".center(15)
    '     hello     '
    >>> "hello".upper()
    'HELLO'
    >>> "hello".replace('h', 'y')
    'yello'
    >>> "hello".replace('l', 'xx')
    'hexxxxo'
    >>> "hello".count('l')
    2
    >>> " hello   ".strip()
    'hello'

The built-in function `str` coverts any object into its string representation.

.. code-block:: python

    >>> str(12)
    '12'
    >>> str(1.2)
    '1.2'

.. problem:: Write a function to count the number of zeros in a number. Use it to count number of zeros in `2 ** 100` and `5 ** 100`.

.. problem:: Write a function `strcmp` to compare two strings, ignoring the case.

.. code-block:: python

    >>> strcmp('python', 'Python')
    True
    >>> strcmp('LaTeX', 'Latex')
    True
