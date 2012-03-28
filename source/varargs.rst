\chapter{0}{Where to put this?}

\section{Functions with variable length arguments and keyword arguments}

Python allows writing functions which takes variable number of arguments. These arguments will be wrapped up in a tuple. Before the variable number of arguments, zero or more normal arguments may occur.

Following is an example of famous `sprintf` function from C programming language.

    def sprintf(format, *args):
        """Implemention C-style sprintf.
        
            >>> sprintf('hello, %s!', 'world')
            'hello, world!'
            >>> sprintf('%d x %d = %d', 2, 3, 6)
            '2 x 3 = 6'
        """
        return format % args
            
Reverse of this situation is when the arguments are already in a list or tuple and a function must be called by unpacking these. The same `*` syntax can be used here too.

    >>> def f(a, b):
    ...    return a + b
    >>> args = [2, 3]
    >>> f(*args)
    5 
 
Just like `*` is used to specify arbitrary positional arguments, the `**` operator can be used to specify arbitrary keyword arguments.

    def dict(**params):
        """Creates a dictionary.
        
            >>> dict(a=2, b=3)
            {'a': 2, 'b': 3}
        """
        return params
   
Again the `**` operator can be used for unpacking a dictionary.

    >>> def f(a, b):
    ...    return a + b
    >>> args = {'a': 2, 'b': 3}
    >>> f(**args)
    5 


