import time

def ex_time(fn):
    def wrap(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()
        print("Time: {}s.".format(end-start))
        return res
    return wrap