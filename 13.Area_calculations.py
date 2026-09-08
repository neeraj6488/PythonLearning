# Calculate the Surface Area and Volume of a Cube

side_length = float(input("Enter the side length of the cube: "))

surface_area = 6 * (side_length ** 2)
volume_cube = side_length ** 3

measurements = {"Surface" : "m²" , "Volume" : "m³"}

print(f"The surface area is {surface_area} {measurements['Surface']} and volume is {volume_cube} {measurements['Volume']} for the cube with side length {side_length} m")