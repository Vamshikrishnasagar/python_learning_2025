"""
Set:
- A set is a collection of unique elements (no duplicates).
- It is unordered (no indexing, slicing, or order guarantees).
- Sets are mutable (you can add or remove elements).
- Can store elements of different data types, but the elements themselves must be hashable (like numbers, strings, tuples).

"""

set1 = {"Sagar",1, 2, 3, 4, 5, 6, 21.124,214.24, 1.2, 2, 3, 1, 232, 86,4, 2, 3, 4, 6 }
set2 = {4, 5, 6, 21.124, 214.24, 1.2}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
