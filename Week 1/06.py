Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

Examples:

csWhereIsBob(["Jimmy", "Layla", "Bob"]) ➞ 2
csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
csWhereIsBob(["Jimmy", "Layla", "James"]) ➞ -1
Notes:

Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").

"""
Understand:
- return index location of "Bob"
- return -1 if "Bob isn't in the list

Plan:
iterate through list to search for "Bob"
return "Bob" location to caller
return -1 if no "Bob"
"""

def csWhereIsBob(names):
    if "Bob" in names:
            return names.index("Bob")
    return -1
