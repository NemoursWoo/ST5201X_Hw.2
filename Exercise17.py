import scipy.stats as stats

# Problem 1: Probability of getting a six between 15 and 20 times
n = 100  # number of trials
p = 1/6  # probability of success (getting a six)
mu_binomial = n * p  # mean of the binomial distribution
sigma_binomial = (n * p * (1 - p))**0.5  # standard deviation of the binomial distribution

# Applying continuity correction and finding Z-scores
z_15 = (14.5 - mu_binomial) / sigma_binomial
z_20 = (20.5 - mu_binomial) / sigma_binomial

# Probability that the number of sixes is between 15 and 20
prob_binomial = stats.norm.cdf(z_20) - stats.norm.cdf(z_15)

# Problem 2: Probability that the sum of the face values of 100 rolls is less than 300
mu_sum = 100 * 3.5  # expected sum of 100 rolls
sigma_sum = (100 * (35 / 12))**0.5  # standard deviation of the sum

# Finding Z-score for sum < 300
z_300 = (300 - mu_sum) / sigma_sum

# Probability that the sum is less than 300
prob_sum = stats.norm.cdf(z_300)

# Output the results
print(f"Probability of getting a six between 15 and 20 times: {prob_binomial}")
print(f"Probability that the sum of face values is less than 300: {prob_sum}")
