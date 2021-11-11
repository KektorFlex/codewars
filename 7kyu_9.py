'''
Take 2 strings s1 and s2 including only letters from ato z.
Return a new sorted string, the longest possible,
containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''

def longest(a1, a2):
    a3 = "".join(sorted(a1 + a2))       # joing all strings, and sorting the last one
    result = str(a3[0])                 # creating a string with first letter from
    for l in a3:
        if l != result[-1]:             # soting
            result += l
    return result

longest("aretheyhere", "yestheyarehere")


# Best on codwars:
# def longest(a1, a2):
#     return "".join(sorted(set(a1 + a2)))
