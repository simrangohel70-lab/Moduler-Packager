def cm_to_meter(cm):
    return cm / 100


def compound_interest(p, r, t):
    amount = p * (1 + r/100)**t
    return round(amount,2)


def area_circle(radius):
    return 3.14 * radius * radius