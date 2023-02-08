from functools import wraps
import typing
import os
import pickle
import time

def pickle_output(data, filename: str):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def pickle_read(filename: str): 
    data = None
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

def memorization_decorator(func: callable)->callable:
    @wraps(func)
    def decorated(*args, **kwargs):
        print(args)
        print(kwargs)
        print(func.__name__)
        # you can MD5 hash this if you want
        filename = str(args) + str(kwargs) + str(func.__name__) + '.pickle'
        if(os.path.exists(filename)):
            return pickle_read(filename)
        else:
            output = func(*args, **kwargs)
            pickle_output(output, filename)
            return output


         
    return decorated


@memorization_decorator
def wrapped_function(p1: int, p2: int):
    print("Long running function")
    time.sleep(10)
    return p1 + p2

wrapped_function(1, 2)
wrapped_function(3, 4)