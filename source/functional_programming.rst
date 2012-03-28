
**********************
Functional Programming
**********************

Recursion
=========

"It always takes longer than you expect, even when you take into account Hofstadter's Law." - *Hofstadter's Law*

Defining solution of a problem in terms of the same problem, typically of smaller size, is called recursion. Recursion makes it possible to express solution of a problem very concisely and elegantly. 

A function is called recursive if it makes call to itself. Typically, a recursive function will have a terminating condition and one or more recursive calls to itself.

**Example: Computing Power**
 
Mathematically we can define power of a number in terms of its smaller power.

.. code-block:: python

    def power(x, n):
        """
        Computes the result of x raised to the power of n.
        
            >>> power(2, 3)
            8
            >>> power(3, 2)
            9
        """
        if n == 0:
            return 1
        else:
            return x * power(x, n-1)
                        
Number of calls to the above ``power`` function is proportional to size of the problem, which is ``n`` here. There are some recursive functions where the number of calls grow exponentially with the input size. The former kind of recursion is called linear recursion and the latter tree recursion.  

        
.. problem :: The above implementation of ``power`` function takes O(n) operations to compute the ``power``. It is possible to compute ``power`` in O(ln(n)) operations. Can you provide an implementation for that?

.. problem :: Implement a function ``add`` to add 2 numbers recursively using the following ``increment`` and ``decrement`` functions.

    def increment(n): return n+1
    def decrement(n): return n-1

**Example: Flatten a list**

Consider the problem where you have a nested list and want to flatten it. 

.. code-block:: python

    def flatten_list(a, result=None):
        """Flattens a nested list.
        
            >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
            [1, 2, 3, 4, 5, 6, 7]
        """"
        if result is None:
            result = []
            
        for x in a:
            if isinstance(x, list):
                flatten_list(x, result)
            else:
                result.append(x)
                
        return result

.. problem :: Write a function ``flatten_dict`` to flatten a nested dictionary by joining the keys with ``.`` character.

    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
    {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
    
.. problem :: Write a function ``unflatten_dict`` to do reverse of ``flatten_dict``.

        >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
        {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
    
.. problem :: Write a function ``treemap`` to map a function over nested list.

    >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5] ] ])
    [1, 4, [9, 16, [25] ] ]
    
.. problem :: Write a function ``tree_reverse`` to reverse elements of a nested-list recursively.

    >>> tree_reverse([[1, 2], [3, [4, 5]], 6])
    [6, [[5, 4], 3], [2, 1]]
    
.. problem :: Write a function ``count_change`` to count the number of ways to change any given amount. Available coins are also passed as argument to the function.

    >>> count_change(10, [1, 5])
    3
    >>> count_change(10, [1, 2])
    6
    >>> count_change(100, [1, 5, 10, 25, 50])
    292
    
.. problem :: Write a function ``permute`` to compute all possible permutations of elements of a given list.

    >>> permute([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

**Example: Binary Trees**

Binary tree is a hierarchical data structure in which every node contains a value and at most 2 children. 

We need to choose a data structure to be able to perform operations on binary trees. However, we can assume functions to create node, access the children and value of a node to implement all the operations.

Let us assume that the following functions are available.

.. code-block:: python

    def leftchild(self, node):
        """Returns the left child of the given node.
        If the left child is absent, None is returned.
        """
        pass
        
    def rightchild(self, node):
        """Returns the right child of the given node.
        If the right child is absent, None is returned.
        """
        pass
        
    def getvalue(self, node):
        """Return the node value."""
        pass
        
    def makenode(self, value, left=None, right=None):
        """Creates a node with given value and left and right children.

        >>> a = makenode(1, makenode(2), makenode(3))
        >>> getvalue(a)
        1
        >>> getvalue(leftchild(a))
        2
        >>> getvalue(rightchild(a))
        3
        """
        pass
        
Now given these functions, we can write a module for doing operations on binary trees.

Lets start with a simple function to test whether a node is leaf.

.. code-block:: python

    def is_leaf(node):
        """Tests whether a node is leaf.
        
        >>> a = make_node(1, make_node(2), None)
        >>> is_leaf(a)
        False
        >>> is_leaf(leftchild(a))
        True
        """
        return leftchild(node) is None and rightchild(node) is None

The following function computes the leaf count of a tree.

.. code-block:: python

    def leafcount(root):
        """Computes number of leaf nodes in a binary tree.
        
            >>> leafcount(make_node(1))
            1
            >>> leafcount(make_node(1, make_node(2), make_node(3)))
            2
        """
        if root is None:
            return 0
        elif is_leaf(root):
            return 1
        else:
            return leafcount(leftchild(root)) + leafcount(rightchild(root))

.. problem :: Write a function ``treeheight`` to compute height of a binary tree.

.. code-block:: python
    
    >>> treeheight(make_node(1))
    1
    >>> a = make_node(1, make_node(2), make_node(3, make_node(4), None))
    >>> treeheight(a)
    3
    >>> treeheight(leftchild(a))
    1
    >>> treeheight(rightchild(a))
    2
    
**Example: In-order traversal**

.. code-block:: python

    def inorder_traversal(root):
        """Returns values of all the nodes of a tree 
        in the order of inorder traversal."""
        if root is None:
            return []
        else:
            return [getvalue(root)] + \
                inorder_traversal(leftchild(root)) + \
                inorder_traversal(rightchild(root))

.. problem :: Write a function ``preorder_traversal`` to return values of nodes in the order of preorder traversal.

.. problem :: Write a function ``postorder_traversal`` to return values of nodes in the order of postorder traversal.

.. problem :: The above implementation of ``inorder_traversal`` is very inefficient because it creates many temporary lists. Can you improve the performance of that function by appending values to a single list.

Higher Order Functions
======================

In Python, functions are first-class objects. They can be passed as arguments to other functions and a new functions can be returned from a function call.


Nested Functions
^^^^^^^^^^^^^^^^

.. code-block:: python

    def sum_of_squares(a, b):
        def square


Tracing Function Calls
^^^^^^^^^^^^^^^^^^^^^^

For example, consider the following ``fib`` function.

.. code-block:: python

    def fib(n):
        if n is 0 or n is 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

Suppose we want to trace all the calls to the ``fib`` function.
We can write a higher order function to return a new function, which prints whenever ``fib`` function is called.

.. code-block:: python

    def trace(f):
        def g(x):
            print f.__name__, x
            value = f(x)
            print 'return', repr(value)
            return value
        return g

    fib = trace(fib)
    print fib(3)
    
This produces the following output.

.. code-block:: text

    fib 3
    fib 2
    fib 1
    return 1
    fib 0
    return 1
    return 2
    fib 1
    return 1
    return 3
    3

To make the output more readable, let us indent the function calls.

.. code-block:: python

    def trace(f):
        f.indent = 0
        def g(x):
            print '|  ' * f.indent + '|--', f.__name__, x
            f.indent += 1
            value = f(x)
            print '|  ' * f.indent + '|--', 'return', repr(value)
            f.indent -= 1
            return value
        return g

    fib = trace(fib)
    print fib(4)

It produces the following output.

.. code-block:: text

    $ python fib.py
    |-- fib 4
    |  |-- fib 3
    |  |  |-- fib 2
    |  |  |  |-- fib 1
    |  |  |  |  |-- return 1
    |  |  |  |-- fib 0
    |  |  |  |  |-- return 1
    |  |  |  |-- return 2
    |  |  |-- fib 1
    |  |  |  |-- return 1
    |  |  |-- return 3
    |  |-- fib 2
    |  |  |-- fib 1
    |  |  |  |-- return 1
    |  |  |-- fib 0
    |  |  |  |-- return 1
    |  |  |-- return 2
    |  |-- return 5
    5

**Example: Memoize**

In the above example, it is clear that number of function calls are growing exponentially with the size of input and there is lot of redundant computation that is done.

Suppose we want to get rid of the redundant computation by caching the result of ``fib`` when it is called for the first time and reuse it when it is needed next time. Doing this is very popular in functional programming world and it is called ``memoize``.

.. code-block:: python

    def memoize(f):
        cache = {}
        def g(x):
            if x not in cache:
                cache[x] = f(x)
            return cache[x]
        return g

    fib = trace(fib)
    fib = memoize(fib)
    print fib(4)

If you notice, after ``memoize``, growth of ``fib`` has become linear.

.. code-block:: text

    |-- fib 4
    |  |-- fib 3
    |  |  |-- fib 2
    |  |  |  |-- fib 1
    |  |  |  |  |-- return 1
    |  |  |  |-- fib 0
    |  |  |  |  |-- return 1
    |  |  |  |-- return 2
    |  |  |-- return 3
    |  |-- return 5
    5

.. problem :: Write a function ``profile``, which takes a function as argument and returns a new function, which behaves exactly similar to the given function, except that it prints the time consumed in executing it.

.. code-block:: python

    >>> fib = profile(fib)
    >>> fib(20)
    time taken: 0.1 sec
    10946

.. problem :: Write a function ``vectorize`` which takes a function ``f`` and return a new function, which takes a list as argument and calls ``f`` for every element and returns the result as a list. 

.. code-block:: python

    >>> def square(x): return x * x
    ...
    >>> f = vectorize(square)
    >>> f([1, 2, 3])
    [1, 4, 9]
    >>> g = vectorize(len)
    >>> g(["hello", "world"])
    [5, 5]
    >>> g([[1, 2], [2, 3, 4]])
    [2, 3]

exec and eval
=============

Python is a dynamic language. It is possible to take a string and execute it as some python code.

For example:

    >>> exec("x = 1")
    >>> x
    1

By default ``exec`` works in the current environment, so it updated the globals in the above example. 
It is also possible to specify an environment to ``exec``.

    >>> env = {'a' : 42}
    >>> exec('x = a+1', env)
    >>> print env['x']
    43
    
It is also possible to create functions or classes dynamically using ``exec``.

    >>> code = 'def %s(): print "Hello %s"'
    >>> for name in ['guido van rossum', 'linus torvalds', 'larry wall']:
    ...     exec(code % (name.replace(' ', '_'), name.title()))
    ...
    >>> guido_van_rossum()
    Hello Guido Van Rossum
    >>> linus_torvalds()
    Hello Linus Torvalds
    >>> larry_wall()
    Hello Larry Wall

``eval`` is like ``exec`` but it takes an expression and returns its value.

    >>> eval("2+3")
    5
    >>> a = 2
    >>> eval("a * a")
    4
    >>> env = {'x' : 42}
    >>> eval('x+1', env)
    43
