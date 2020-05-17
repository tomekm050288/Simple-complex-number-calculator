from datetime import datetime
from collections import namedtuple
import time


def show_code_author(func):
    def wrapper(*args, **kwargs):
        Result_with_date = namedtuple('Result_with_date', 'result date')
        named_tuple = Result_with_date(func(*args, **kwargs), datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        print(f"Author name: Tomasz Matuszewski")
        print(f"Result generated {str(named_tuple.date)} - result {str(named_tuple.result)}")
        start = time.time()
        value = func(*args, **kwargs)
        stop = time.time()
        print(f'Time of execution {stop - start}')
        return value

    return wrapper


