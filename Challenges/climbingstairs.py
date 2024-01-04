"""
How many ways are there to climb a set of stairs if you can climb 1 or 2 stairs at a time?
It's a problem solvable using the Fibonnaci sequence, if you know that the possbilities of
every step is really the sum (OR is addition in combinatorics, so use addition sum) of the 
possibilities of the two stairs below it.
"""
steps = int(input()) + 1
print(round(((((1 + 5 ** 0.5) / 2) ** steps) - (((1 - 5 ** 0.5) / 2) ** steps)) / (5 ** 0.5)))
