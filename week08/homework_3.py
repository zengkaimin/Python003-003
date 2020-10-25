from time import time
import numpy as np
def timer(func):
    def inner(*args,**kargs):
        time1=time()
        ret=func(*args,**kargs)
        print(f'The runtime of the function is {time()-time1}')
        return ret
    return inner

@timer
def diy_sum(*args,**kargs):
    result=0
    for i in args:
        result+=sum(i)
    return result

diy_sum(list((range(100))))
