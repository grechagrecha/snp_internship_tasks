def sort_list(a: list) -> list:
    if len(a) == 0:
        return a

    mn, mx = min(a), max(a)

    for i in range(len(a)):
        if a[i] == mn:
            a[i] = mx
        elif a[i] == mx:
            a[i] = mn

    a.append(mn)

    return a
