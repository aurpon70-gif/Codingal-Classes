import math

angle_degrees = float(input("Enter the angle in degrees: "))

angle_radians = math.radians(angle_degrees)

sine_val = math.sin(angle_radians)
cosine_val = math.cos(angle_radians)
tangent_val = math.tan(angle_radians)

print(f"\nResults for {angle_degrees}°:")
print(f"Sine: {sine_val}")
print(f"Cosine: {cosine_val}")
print(f"Tangent: {tangent_val}")