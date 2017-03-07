""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    if exists(file_name) and not reset:
        f = open(file_name, 'rb+')
        # open the counter file in rb+ if it exists
        # and not resetting the counter
        # r = reading
        # b = binary
        # rb+ binary file in read or write mode
        counter = load(f)
        counter += 1
        # increments
        dump(counter, open(file_name, 'wb'))
        f.close()
        # store the file as text and dump the data
        # so making it not load whenever function runs
        # this generates the permanent text file
    else:
        f = open(file_name, 'wb')
        # wb(writing) mode otherwises
        counter = 1
        dump(counter, f)
        f.close()

    reloaded_copy_of_texts = load(open(file_name, 'rb'))
    return(reloaded_copy_of_texts)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod(verbose=True)
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
