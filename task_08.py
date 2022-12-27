from string import digits


def multiply_numbers(*inputs):
    if not inputs:
        return None

    ans = 1
    digit_string = ''

    for sym in str(inputs):
        if sym in digits:
            digit_string += sym

    if not digit_string:
        return None

    for i in digit_string:
        ans *= int(i)
    return ans
