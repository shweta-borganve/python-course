import math

def calculate_circle_area(radius):
    """Calculate the area of a cicle given its radius."""
    area = math.pi * (radius ** 2)
    return area

radius = 5
area = calculate_circle_area(radius)
print(f"the area of a circle with radius {radius} is {area:.2f}")