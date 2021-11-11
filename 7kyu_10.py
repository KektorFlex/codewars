def is_square(n):    
    if n < 0:
        return False
    sqrt = n ** 0.5
    return sqrt.is_integer()

# def is_square(n):
#     return n >= 0 and (n ** 0.5).is_integer()