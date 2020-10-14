"""
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
"""


def convert(n, base):
    q, r = divmod(n, base)
    if q == 0:
        return [r]
    else:
        return convert(q, base) + [r]
