"""
Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""

first_points = (float(input("Type the x1 point: ")), float(input("Type the y1 point: ")))
second_points = (float(input("Type the x2 point: ")), float(input("Type the y2 point: ")))

distance = ((second_points[0] - first_points[0])**2 + (second_points[1] - first_points[1])**2)

print(f"Distance = √{distance}\nor {distance**(1/2)}")

