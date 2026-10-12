square_area = lambda a: a**2
rectangle_area = lambda l, b: l * b
triangle_area = lambda ba, h: 0.5 * ba * h

a = int(input("Enter the side of the square: "))
print("Area of the square:", square_area(a))

ba = int(input("Enter the length: "))
h = int(input("Enter the breadth: "))
print("Area of the triangle:", triangle_area(ba, h))

l = int(input("Enter the base: "))
b = int(input("Enter the height: "))
print("Area of the rectangle:", rectangle_area(l, b))
