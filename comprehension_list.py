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
