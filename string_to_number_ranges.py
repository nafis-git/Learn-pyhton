""" 
function which accepts a string containing ranges of numbers or single number and returns an iterable of ranges between those numbers.
The numeric ranges in the string will consist of two numbers separated by hyphens or a single value
and each of the ranges, or single values, will be separated by commas and any number of spaces.

>>> parse_ranges('1-2,4-4,8')
[1, 2, 4, 8
>>> parse_ranges('0-0, 4-8, 20-20, 43-45')
[0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
"""

def parse_ranges(string):
  #here I use partition as it gives me alwayes three values which include start, seperator and the stop point,so if they are not available it returns None
    groups = [pair.partition('-') for pair in string.split(',')]
    pairs = [(start, stop) if stop else (start, start) for (start, _, stop) in groups ] 
    for start, stop in pairs:
        yield from range(int(start), int(stop)+1) 
 
