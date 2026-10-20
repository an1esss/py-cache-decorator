from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper_func(*args):
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            print("Calculating new result")
            cache_dict[args] = func(*args)
            return cache_dict[args]
    return wrapper_func
