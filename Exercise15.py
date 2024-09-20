import numpy as np

# Define the number of random points for different cases
n_values = [100, 1000, 10000]

# Define the bounds of the circle (radius = 2)
radius = 2
x_min, x_max = 0, radius
y_min, y_max = 0, radius

# Exact area of the quarter circle minus the triangle (which is the excluded region)
# Exact quarter circle area: (pi * r^2) / 4
exact_area_circle = (np.pi * radius**2) / 4
# Area of the triangle: (1/2 * base * height) where base = height = 2
exact_area_triangle = 0.5 * 2 * 2
exact_area_shaded = exact_area_circle - exact_area_triangle

# Monte Carlo simulation
def monte_carlo_area(n):
    # Generate random points within the bounding box
    x = np.random.uniform(x_min, x_max, n)
    y = np.random.uniform(y_min, y_max, n)
    
    # Check if the points are inside the circle and above the line x + y > 2
    inside_circle = (x**2 + y**2) <= radius**2
    above_line = (x + y) > 2
    
    # Count the points that satisfy both conditions
    points_in_region = np.sum(inside_circle & above_line)
    
    # Calculate the proportion of points in the region
    area_fraction = points_in_region / n
    
    # Area of the bounding box is (2 * 2) = 4
    area_estimate = area_fraction * (x_max * y_max)
    return area_estimate

# Run the simulation for n = 100, 1000, and 10000
results = {n: monte_carlo_area(n) for n in n_values}

# Output exact and estimated values
print(f"Exact area of the shaded region: {exact_area_shaded}")
for n, estimate in results.items():
    print(f"Estimated area with n = {n}: {estimate}")
