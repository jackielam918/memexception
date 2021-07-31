from functools import wraps
from memexception.constants import *
from memexception.helpers import output_meme


def doge_exception_handle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            output_meme(DOGE, 'wow such exception')
            raise e

    return wrapper


def pepe_exception_handle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            output_meme(PEPE, 'exception.... feels bad man')
            raise e

    return wrapper


def pikachu_exception_handle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            output_meme(PIKA, 'didnt work')
            raise e

    return wrapper

