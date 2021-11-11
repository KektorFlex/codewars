'''
Write a function, which takes a non-negative integer (seconds)
as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''

def make_readable(seconds):
    f_num = seconds // 3600
    s_num = (seconds - f_num * 3600) // 60
    t_num = seconds - f_num * 3600 - s_num * 60
    return "%02d" % f_num + ":" + "%02d" % s_num + ":" + "%02d" % t_num


make_readable(35900)

# best on codewars
# def make_readable(s):
#     return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)