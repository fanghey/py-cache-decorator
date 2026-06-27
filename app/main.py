from typing import Callable


def cache(func: Callable) -> Callable:
    saved = {}

    def wrapper(*args):
        if args in saved:
            print('Getting from cache')
            return saved[args]

        print('Calculating new result')
        result = func(*args)
        saved[args] = result
        return result

    return wrapper
