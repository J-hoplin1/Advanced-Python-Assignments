# table.py
"""Examples on tables. A table is a 2D list of lists where all inner lists have
the same number of elements; each inner list is a row of the table."""

from typing import MutableSequence
def print_all_rows(my_table:MutableSequence):
    """Prints all rows of the table, one row (list) on each line.
    Preconditions:  my_table is a table of numbers (int or float)
                    my_table is not empty
    """
    for i,j in enumerate(my_table):
        print(f"Row {i} : {j}")


def print_all_elements(my_table):
    """Prints all elements in the table, one element on each line.
    Preconditions:  my_table is a table of numbers (int or float)
                    my_table is not empty
    """
    for i in my_table:
        print(*i,end=" ")



def print_all_elements_v2(my_table):
    """Prints all elements in the table, one element on each line, but identify the source row
    Preconditions:  my_table is a table of numbers (int or float)
                    my_table is not empty
    """


def num_positives(my_table):
    """Returns: number of positive values in the given table
    Preconditions:  my_table is a table of numbers (int or float)
                    my_table is not empty
    """
    count= 0
    for row in my_table:
        for item in row:
            if item > 0:
                count= count + 1
    return count


def absolute(my_table):
    """Take the absolute value of all the values in the given table. This
    function modifies the table.
    Preconditions:  my_table is a table of numbers (int or float)
                    my_table is not empty
    """
    num_rows= len(my_table)
    num_cols= len(my_table[0])
    for r in range(num_rows):
        for c in range(num_cols):
            if my_table[r][c] < 0:
                my_table[r][c]= abs(my_table[r][c])


# Script code
d= [[5,4,7,3],[-4,8,-9,7],[5,-1,-2,-3],[-4,1,2,9]]
print('Print all the rows of the table, one list on each line:')
print_all_rows(d)
# print('Print all the elements of the table, one element on each line')
# print_all_elements(d)
# print('Print all the elements of the table, one element on each line')
# print_all_elements_v2(d)
# print('There are '+str(num_positives(d))+' positive values in the table')
# print('Take the absolute value of the table:')
# absolute(d)
# print_all_rows(d)
