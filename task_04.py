def sort_list(a: list) -> list:
    if len(a) == 0:
        return a

    mn, mx = min(a), max(a)

    for i in range(len(a)):
        a[i] = mx if a[i] == mn else mn if a[i] == mx else a[i]

    a.append(mn)

    return a
