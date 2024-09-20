import numpy as np
import scipy.stats as stats

# Function to compute the Monte Carlo estimate of an integral
def monte_carlo_integral(f, a, b, n):
    x = np.random.uniform(a, b, n)
    fx = f(x)
    return (b - a) * np.mean(fx)

# Function definitions
f1 = lambda x: np.cos(2 * np.pi * x)
f2 = lambda x: np.cos(2 * np.pi * x**2)

# Exact value of the first integral
exact_integral_f1 = 0

# Problem 1: Monte Carlo estimates for \int_0^1 cos(2πx) dx
n_values = [100, 1000]
estimates_f1 = [monte_carlo_integral(f1, 0, 1, n) for n in n_values]

# Problem 2: Monte Carlo estimates for \int_0^1 cos(2πx^2) dx
estimates_f2 = [monte_carlo_integral(f2, 0, 1, n) for n in n_values]

# Problem 3: Using central limit theorem to find delta
n = 1000
sample_f1 = [f1(np.random.uniform(0, 1)) for _ in range(n)]
mean_f1 = np.mean(sample_f1)
std_f1 = np.std(sample_f1) / np.sqrt(n)  # Standard error of the mean

# For 95% confidence, we use the 1.96 Z-score
z_score = stats.norm.ppf(0.975)
delta = z_score * std_f1

# Output the results
print("Problem 1: Monte Carlo estimates for ∫_0^1 cos(2πx) dx")
for i, n in enumerate(n_values):
    print(f"n = {n}, Estimate = {estimates_f1[i]}, Exact = {exact_integral_f1}")

print("\nProblem 2: Monte Carlo estimates for ∫_0^1 cos(2πx^2) dx")
for i, n in enumerate(n_values):
    print(f"n = {n}, Estimate = {estimates_f2[i]}")

print(f"\nProblem 3: Using CLT, delta for 95% confidence with n = 1000 is {delta}")
