import math

angle_degrees = float(input("Enter the angle in degrees: "))

angle_radians = math.radians(angle_degrees)

sin_val = math.sin(angle_radians)
cos_val = math.cos(angle_radians)
tan_val = math.tan(angle_radians)

print(f"\nResults for {angle_degrees}°:")
print(f"Sin: {sin_val}")
print(f"Cos: {cos_val}")
print(f"Tan: {tan_val}")