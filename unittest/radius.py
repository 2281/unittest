from math import pi

def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius can't be negative")

    if type(radius) not in [int, float]:
        raise TypeError("Type is not int or float")

    return pi*radius**2


#print(circle_area(-5))

# r_list = [1,0,-1,2+3j, True, [2], "seven"]
# message = "Площадь окружности с радиусом {radius} --> {area}"
#
# for r in r_list:
#     s = circle_area(r)
#     print(message.format(radius = r, area = s))