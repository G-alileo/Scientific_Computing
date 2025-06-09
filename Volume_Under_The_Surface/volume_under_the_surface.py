# Calculate the volume under z = x^2 + y^2 over 0 ≤ x, y ≤ 1 using list comprehensions

def surface(x, y):
    return x**2 + y**2

steps = 100
dx = 1.0 / steps
dy = 1.0 / steps

# Create lists of x and y values
x_values = [i * dx for i in range(steps)]
y_values = [j * dy for j in range(steps)]

# Use a double list comprehension to sum the volumes
volume = sum(
    surface(x, y) * dx * dy
    for x in x_values
    for y in y_values
)

print(f"Approximate volume under z = x^2 + y^2 over 0 ≤ x, y ≤ 1: {volume}")