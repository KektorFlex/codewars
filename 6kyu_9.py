def bouncing_ball(h, bounce, window):

    if window < 0 or h <= window or bounce >= 1 or bounce <= 0:  # border description
        return -1

    counter = 0
    while h > window:
        counter += 1
        h *= bounce
        if h > window:
            counter += 1

    return counter

