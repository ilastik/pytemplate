'''
nosetests picks up all python files that start or end with `test` in their name,
and runs all methods that start or end with `test`.
'''

# pythonpath modification to make mypackage available 
# for import without requiring it to be installed
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import mypackage.mymodule

def test_something():
    # simply use assertions to make sure your code behaves as expected
    assert(True)

def test_myclass_fibonacci():
    fibonacciComputer = mypackage.mymodule.MyClass(20)
    assert(fibonacciComputer.fibonacci(12) == 144)

def test_myclass_above_limit():
    fibonacciComputer = mypackage.mymodule.MyClass(20)
    try:
        fibonacciComputer.fibonacci(21)
        assert(False)
    except ValueError:
        assert(True)