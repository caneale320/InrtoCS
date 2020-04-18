# Caleb Neale, can4ku


def mean(a, b, c):
    return (a + b + c)/3


def median(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)

    if a == b and b == c:
        return b
    elif a <= b and a <= c:
        if b < c:
            return b
        elif c < b:
            return c
    elif b <= a and b <= c:
        if a < c:
            return a
        elif c < a:
            return c
    elif c <= a and c <= b:
        if a < b:
            return a
        elif b < a:
            return b



def rms (a, b, c):
    a_sq = a**2
    b_sq = b**2
    c_sq = c**2
    temp_meansq = mean(a_sq, b_sq, c_sq)
    return temp_meansq**(1/2)


def middle_average(a, b, c):
    temp_mean = mean(a, b, c)
    temp_median = median(a, b, c)
    temp_rms = rms(a, b, c)
    return median(temp_mean, temp_median, temp_rms)










