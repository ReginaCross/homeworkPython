import math

def square(side):
    area = side * side
    return area if isinstance(side, int) else math.ceil(area)

side_length = float(input("Введите длину стороны квадрата: "))
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result}")