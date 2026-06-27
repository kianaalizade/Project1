#comb and perm in python
import math
def math_py(k,n):
    x=math.comb(k,n)
    y=math.perm(k,n)
    print(f" for comb={x} , for perm={y}")
math_py(10,3)
