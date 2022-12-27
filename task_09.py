def connect_dicts(dict1: dict, dict2: dict) -> dict:
    dict_lowp, dict_highp = dict1.copy(), dict2.copy()

    if sum(dict_lowp.values()) > sum(dict_highp.values()):
        dict_lowp, dict_highp = dict_highp, dict_lowp

    for key, val in dict_highp.items():
        dict_lowp[key] = val

    dict_final = {key: value for (key, value) in dict_lowp.items() if value >= 10}
    dict_final = dict(sorted(dict_final.items(), key=lambda x: x[1]))

    return dict_final
