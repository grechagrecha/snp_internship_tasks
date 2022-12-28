import datetime as dt


def date_in_future(days: int) -> str:
    curr_time = dt.datetime.now()

    if not isinstance(days, int):
        return curr_time.strftime('%Y-%m-%d %H:%M:%S')

    return (curr_time + dt.timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')
