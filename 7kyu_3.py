'''
You are given a string of letters and an array of numbers.
The numbers indicate positions of letters that must be removed, in order,
starting from the beginning of the array.
After each removal the size of the string decreases (there is no empty space).
Return the only letter left.

Example:

let str = "zbk", arr = [0, 1]
    str = "bk", arr = [1]
    str = "b", arr = []
    return 'b'

Notes
The given string will never be empty.
The length of the array is always one less than the length of the string.
All numbers are valid.
There can be duplicate letters and numbers.
'''
def last_survivor(letters, coords):
    list = []
    for l in letters:       #making a list with letters
        list.append(l)
    while len(list) > 1:
        for n in coords:
            list.pop(n)
    print(list[0])

last_survivor("dfgr", [0,2,1])