import time

def show_code_author(func):
    def wrapper(*args, **kwargs):
        print(f"Author name: Tomasz Matuszewski")
        value = func(*args, **kwargs)
        return value
    return wrapper


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        stop = time.time()
        print(f"Time of execution: {stop-start}")
        return value
    return wrapper