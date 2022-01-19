def format_duration(seconds):
'''
min = 60 sec
hour = 60 min
day = 24 hour
year = 365 day
'''

    hours = ""
    days = ""
    years = ""
    seconds = ""

    s_num = seconds % 60
    h_num = seconds // (60 * 60)
    d_num = seconds // (60 * 60 * 24)
    y_num = seconds // (days * 365)

    if y_num == 1:
        years = str(y_num) + "year, "
    elif y_num > 1:
        years = str(y_num) + "years, "

    if d_num == 1:
        days = str(d_num) + "day, "
    elif d_num > 1:
        days = str(d_num) + "days, "

    if h_num == 1:
        hours = str(h_num) + "hour "
    elif h_num > 1:
        hours = str(h_num) + "hours "

    if s_num == 1:
        seconds = str(s_num) + "second"
    elif s_num > 1:
        seconds = str(s_num) + "seconds"
