# height2.py

"""Demonstrate local vs. global variable"""

INCHES_PER_FT = 12
feet = "plural of foot"

def get_feet(ht_in_inches):
    """Return ht_in_inches rounded down to the nearest feet"""
    feet = ht_in_inches // INCHES_PER_FT
    return feet

get_feet(68)
