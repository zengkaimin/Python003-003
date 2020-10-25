from typing import Callable, Sequence, Iterator

def diy_map(func:Callable , seq:Sequence) -> Iterator :
    return (func(item) for item in seq)

l=[2,4,6,7]
def two(x):
    return 2*x
m=diy_map(two,l)
next(m)
list(m)
