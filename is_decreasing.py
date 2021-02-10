# Author: Adam Jeffries
# Date: 2/9/2021
# Description: recursive function named is_decreasing that takes as its parameter a list of numbers.
# It should return True if the elements of the list are strictly decreasing but returns False otherwise.

def is_descending(list):
    if len(list) <= 1 or (len(list) == 2 and list[0] > list[1]):
        return True
    else:
        if list[0] > list[1]:
            return is_descending(list[1::])
        else:
            return False
