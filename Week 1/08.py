Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, do not add another 7.

Examples:

csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["G", "F7", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
csMakeItJazzy([]) ➞ []
Notes:

Return an empty list if the given list is empty.
You can expect all the tests to have valid chords.

"""
Understand:
- create a new list called sevens
- iterate through chords checking each chord for 7 as the final character
    - if the final character is seven, append to sevens
    - if the final character is not 7, append 7 to the character and then append that to sevens
- return sevens to the caller
Plan:
"""
def csMakeItJazzy(chords):
    sevens = []
    
    for chord in chords:
        if chord[-1] == "7":
            sevens.append(chord)
        elif chord[-1] != "7":
            # chord += "7"
            sevens.append(chord +"7")
    return sevens