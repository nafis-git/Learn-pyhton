"""function that accepts some lists-of-lists of numbers and returns one with 
added values of the corresponding numbers of the lists and if the nested lists do not have similar length then return value error"""
# to get the length of a nested lists
def get_len(matrix):
    return [len(matrix_) for matrix_ in matrix]
# get some list of lists and add the corrsponding elements together
def add(*matrices):
  # check if the length of the nested lists are similar
    len_matrix = get_len(matrices[0]) 
    if any (get_len(m) != len_matrix for m in matrices):
        raise ValueError("Given matrices are not the same size.")
    # if length of the nested lists are equal then add the corrosponding values
    # first select the corrosponding lists in the list of lists "rows in zip(*matrices)"
    # then adding corrosponding values of those lists "[sum(values) for values in zip(*rows)]"
    return [
        [sum(values) for values in zip(*rows)] 
        for rows in zip(*matrices)
    ]


""" the function accepts a nested iterator and returns a flattened version of that as a generator
deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]) = [1, 2, 3, 4, 5, 6, 7, 8] 
deep_flatten([[1, [2, 3]], 4, 5]) [1, 2, 3, 4, 5]
list(deep_flatten([['apple', 'pickle'], ['pear', 'avocado']]))
['apple', 'pickle', 'pear', 'avocado']"""

from collections import Iterable 
def deep_flatten(nested):
    for item in nested:
        # to check if the item is still an iterator or str, we use isinstance, for strings we need exclude them from looping otherwise it will loop on every character
        if isinstance(item, Iterable) and not isinstance(item,(str, bytes)):  
            # using yield from to have a genarator and calling the function itself, recursion function as for each item we need to check if it is iterator as so go through all the steps
            yield from deep_flatten(item)
        else:
            yield item


