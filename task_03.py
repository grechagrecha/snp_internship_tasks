def max_odd(a: list):
    seq = [i for i in a if isinstance(i, (int, float)) and i % 2 == 1]

    if seq:
        return max(seq)
    return None
