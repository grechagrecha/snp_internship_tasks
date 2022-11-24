def coincidence(lst=None, rng=None) -> list:
    if not lst or not rng:
        return []

    in_range = []
    for i in lst:
        if isinstance(i, (int, float)):
            if rng.start <= i < rng.stop:
                in_range.append(i)

    return in_range
