# height3.py

"""Demonstrate
    - use of global variable
    - local vs. global variable
    - calling a function and storing the returned result for further use"""

INCHES_PER_FT = 12
feet= "Plural of foot"

def get_feet(ht_in_inches):
    """Return ht_in_inches rounded down to the nearest feet"""
    feet = ht_in_inches // INCHES_PER_FT
    return feet

def get_inches(ht_in_feet):
    """Return ht_in_feet in inches"""
    return ht_in_feet * INCHES_PER_FT

input_inches = 68
result= get_feet(input_inches)
print(str(input_inches)  + " inches rounds down to " + str(result) + " feet")
print(feet)
