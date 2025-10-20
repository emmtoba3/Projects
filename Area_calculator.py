#Area Calculator
"""
Program that calculates the area of one of the following shapes:
- Square
- Rectangle
- Triangle
- Circle
"""
from math import pi
import random

# --- AREA FUNCTIONS ---
def square_area(side):
    return round(side ** 2, 2)
def rectangle_area(length, width):
    return round(length * width, 2)
def triangle_area(base, height):
    return round(base * height/2, 2)
def circle_area(radius):
    return round(pi * radius ** 2, 2)

# --- PLUS RANDOM FACTS ---
square_data = ["All sides are equal in length.",
    "Diagonals are perpendicular only in a square and a rhombus.",
    "Each interior angle is 90°.",
    "A square is a special case of a rectangle and a rhombus.",
    "Its symmetry group is D4."]
rectangle_data = ["Opposite sides are equal and parallel.",
    "All interior angles are 90°.",
    "Diagonals are equal in length.",
    "Perimeter is 2 × (length + width).",
    "Area grows linearly with each side."]
triangle_data = ["Sum of interior angles equals 180° (in Euclidean geometry).",
    "Heron's formula uses the three sides to compute area.",
    "Equilateral triangles have all sides equal.",
    "Isosceles triangles have two equal sides.",
    "Scalene triangles have all sides different."]
circle_data = ["Circumference equals 2πr.",
    "Area equals πr².",
    "All radii have the same length.",
    "A circle has infinite lines of symmetry.",
    "π is irrational and non-repeating."]

# --- MAIN PROGRAM LOOP ---
while True:
    print("═══════════════════════════════════")
    print("🧮  GEOMETRIC CALCULATOR  🧮")
    print("═══════════════════════════════════\n")
    print("Let's get started! Pick a shape from the list below: ")
    print("1️⃣ Triangle\n2️⃣ Rectangle\n3️⃣ Square\n4️⃣ Circle\n")
    print("💡 Type 'exit', 'quit', or '0' at any time to close the program.""\n")

    shape = input("👉 Enter the number corresponding to the shape you want to calculate: ")
    if   shape.lower() in ("exit", "quit", "0"):
         print("Exiting the calculator. Goodbye! 👋\n")
         break
    elif shape == "1":
         base = float(input("Enter the base of the triangle: "))
         height = float(input("Enter the height of the triangle: "))
         print("\n===================================")
         print("📊 Calculation Results")
         print("===================================\n")
         print(f"The base is: {base}\nThe height is: {height}\nThe area of the triangle:", triangle_area(base, height))
         print("🧠 Fun fact:", random.choice(triangle_data), "\n\n")
    elif shape == "2":
         length = float(input("Enter the length of the rectangle: "))
         width = float(input("Enter the width of the rectangle: "))
         print("\n===================================")
         print("📊 Calculation Results")
         print("===================================\n")
         print(f"The length is: {length}\nThe width is: {width}\nArea of the rectangle:", rectangle_area(length, width))
         print("🧠 Fun fact:", random.choice(rectangle_data), "\n\n")
    elif shape == "3":
         side = float(input("Enter the side length of the square: "))
         print("\n===================================")
         print("📊 Calculation Results")
         print("===================================\n")
         print(f"The side is: {side}\nArea of the square:", square_area(side))
         print("🧠 Fun fact:", random.choice(square_data), "\n\n")
    elif shape == "4":
         radius = float(input("Enter the radius of the circle: "))
         print("\n===================================")
         print("📊 Calculation Results")
         print("===================================\n")
         print(f"The radius is: {radius}\nArea of the circle:", circle_area(radius))
         print("🧠 Fun fact:", random.choice(circle_data), "\n\n")  
    
    elif shape != "1" and shape != "2" and shape != "3" and shape != "4": 
         print("\nI think you made a mistake. Please select a number between 1 and 4.\n")
    