# pythonpath modification to make hytra available 
# for import without requiring it to be installed
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# standard imports
import logging
import argparse
import mypackage.mymodule

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Compute the fibonacci number of the supplied number',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--number', required=True, type=int, dest='number',
                        help='number')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False)

    # parse command line
    args = parser.parse_args()

    # configure the basic logging level
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    fibonacciComputer = mypackage.mymodule.MyClass(20)
    result = fibonacciComputer.fibonacci(args.number)
    print(result)