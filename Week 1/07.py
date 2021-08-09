Imagine a school that children attend for years. In each year, there are a certain number of groups started, marked with the letters. So if years = 7 and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for the last year, the groups are 7a, 7b, 7c, 7d.

Write a function that returns the groups in the school by year (as a string), separated with a comma and space in the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

Examples:

csSchoolYearsAndGroups(years = 7, groups = 4) ➞ "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"
Notes:

1 <= years <= 10
1 <= groups <=26


"""
Understand:
- There are a given number of years notated by y
- for each year, there are a number of groups notated by a letter corresponding to the letter of the alphabet - 1
- each year/group combination is notated by  yearNumbergroupLetter
- in order to iterate through years and/or groups, integer must be converted to string

Plan:
- create groupLetters list indentical to alphabet
# groupLetters = ["a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

- create yearsList list from 1-10
# yearsList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

- create empty list to hold groups by year
# yearsByGroup = []

- slice groupLetters list from left identical to the number of groups
# groupLetters[0:groups]

- slice yearList at integer corresponding to years
# yearList[0:years]

- for each year/index, iterate through groupLetters and attach all letters to year individually

attach one element from groupLetters and append it to new list
# for year in yearsList and letter in groupLetters
    yearsByGroup += f{year}{letter}
"""
def csSchoolYearsAndGroups(years, groups):
    
    groupLetters = "abcdefghijklmnopqrstuvwxyz"
    yearList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    yearsByGroup = []
    
    
    for year in yearList[:years]:
        for letter in groupLetters[:groups]:
            yearGroup = (f"{year}{letter}")
            yearsByGroup.append(yearGroup)
            continue
        continue
    return ", ".join(yearsByGroup)