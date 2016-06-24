'''
This module performs nothing and just serves as a dummy.
This module contains a class `mymodule.MyClass` which serves as a template.
'''

import logging

def getLogger():
    '''
    Return a custom logger for this module.

    We should use pythons logging functionality everywhere.
    By using `__name__` as argument to `getLogger`, each log message
    coming from this module will be prepended by "mypackage.mymodule"
    '''
    return logging.getLogger(__name__)

class MyClass(object):
    ''' This class is a template and can compute fibonacci numbers '''

    def __init__(self, limit=None):
        '''
        Construct a MyClass object. By specifying `limit` one can set the highest
        number of which we still compute Fibonacci numbers.

        If `limit` is given, `fibonacci()` will complain if it sees a too high argument.
        '''
        getLogger().info('Constructed MyClass')

        # the underscore denotes class-internal (protected) member variables / functions
        self._limit = limit

    def fibonacci(self, value):
        '''
        Compute the fibonacci number of `value`.
        If limit is given, `value <= self._limit` must be True or a `ValueError` is raised.
        '''
        if self._limit is not None and value > self._limit:
            getLogger().error('{} is too high for {}'.format(value, self._limit))
            raise ValueError('Cannot compute fibonacci number above limit')
        else:
            return self._fibonacciImplementation(value)

    def _fibonacciImplementation(self, value):
        '''
        protected recursive implementation of the fibonacci number which doesn't perform any checks
        '''
        getLogger().debug('computing fibonacci for {}'.format(value))

        if value < 2:
            getLogger().debug('reached end of recursion')
            return value
        return self._fibonacciImplementation(value - 2) + self._fibonacciImplementation(value - 1)
