#Python’s trigonometric functions operate in radians, not degrees, so converting between the two is a required first step in any geometry task
import math
def math_py(degrees):
    x=math.radians(degrees)
    y=math.cos(x)
    z=math.tan(x)
    print(f"for degrees{degrees}, radians:{x} and cos: {y} and tan: {z}")
math_py(270)
