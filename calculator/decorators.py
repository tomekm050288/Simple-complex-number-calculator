def show_code_author(func):
    def wrapper(*args, **kwargs):
        print(f"Author name: Tomasz Matuszewski")
        value = func(*args, **kwargs)
        return value
    return wrapper


