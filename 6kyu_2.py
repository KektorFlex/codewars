'''
In this kata you are required to, given a string,
replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
'''
def alphabet_position(text):
    result = ""
    for l in text.lower():  #for each character 'l' in the lower case 'text'
        if l.isalpha():     #if it meets alphabetical letter
            result += str(ord(l) - 96) + " "  #find it's value, taken from stackoverlfow (ascii)
    result = result.rstrip()       #remove trailing spaces from the right side of a string
    return result