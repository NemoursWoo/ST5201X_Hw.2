import scipy.stats as stats

# Given parameters
mean_poisson = 100
std_poisson = mean_poisson**0.5  # standard deviation for the normal approximation
confidence_level = 0.9  # Probability of 90%

# The goal is to find the z-value corresponding to a central confidence level of 90%
# This means we need to find the z-value such that P(-z < Z < z) = 0.9
z_value = stats.norm.ppf((1 + confidence_level) / 2)

# Now solve for delta, delta = z_value * std_poisson
delta = z_value * std_poisson

print(delta)
