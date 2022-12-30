import datetime as dt


def date_in_future(days: int) -> str:
    date_format = '%d-%m-%Y %H:%M:%S'
    curr_time = dt.datetime.now()

    if not isinstance(days, int):
        return curr_time.strftime(date_format)

    return (curr_time + dt.timedelta(days=days)).strftime(date_format)
