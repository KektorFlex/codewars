'''
100th Kata
You are given a message (text) that you choose to read in
a mirror (weirdo). Return what you would see, complete with
the mirror frame.
Example:
'Hello World'

would give:
"*********\n* olleH *\n* dlroW *\n*********"

Words in your solution should be left-aligned.
'''

def mirror(text):
    list = text.split()                 # making a list
    n_list = []
    count = len(max(list, key=len))     # finding out a longest word
    for w in list:
        w = w[::-1]                     # reversing the word
        if len(w) < count:              # adding spaces depending on the longest word
            w += " " * (count - len(w))
        n_list.append(w)
    result = "*" * (count + 4) + "\n* " + " *\n* ".join(n_list) + " *\n" + "*" * (count + 4)    # adding frames

    return result

# # Best solution on codwars:    !!! I need to use more '.format' !!!
# def mirror(text):
#     words = [w[::-1] for w in text.split()]
#     max_len = max(map(len, words))
#     border = ['*' * (max_len + 4)]
#     words = ['* {} *'.format(w.ljust(max_len)) for w in words]
#     return '\n'.join(border + words + border)