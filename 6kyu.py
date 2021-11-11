'''
Write a function that takes an integer as input,
and returns the number of bits
that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010,
so the function should return 5 in this case
'''
'''
def countBits(n):
    count = 0
    while n > 0:
        if (n & 1) == 1:
            count = count + 1
        n >>= 1
    return count
print countBits(1234)
'''
'''
def countBits(n):
    return len(bin(n).replace("0b","").replace("0",""))
'''
'''
def countBits(n):
    return bin(n).count("1")
'''
def count_bits(n):
    return len(bin(n).replace("0b", "").replace("0", ""))

print(count_bits(1234))