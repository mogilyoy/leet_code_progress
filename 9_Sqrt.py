# Given a non-negative integer x, compute and return the square root of x.

def mySqrt(x: int) -> int:
    a = []
    around = 0
    x_dub = x
    while x_dub > 0:
        a.append(x_dub%10)
        x_dub //= 10

    if len(a)%2 == 0:
        around = 6 * 10**((len(a) - 2) / 2)
    else: 
        around = 2 * 10**((len(a) - 1) / 2)

    while True:
        prev_around = around
        around = 0.5*(around + x/around)
        if round(prev_around) == round(around):
            return int(around//1)

