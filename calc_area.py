import math

# Formula for area of a square: side_length ** 2
def calc_area_square(side_length):
    return side_length ** 2

def calc_area_circle(radius):
    if not isinstance(radius, float):
        raise TypeError(f'radius is {radius} but should be a number')
    if radius < 0:
        raise ValueError(f'radius is {radius} but must be positive')
    return math.pi * radius ** 2

def calc_area_rectangle(side1_length, side2_length):
    if side1_length == side2_length:
        return  side1_length ** 2
    else:
        return side1_length * side2_length