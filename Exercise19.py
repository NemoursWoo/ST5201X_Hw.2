import numpy as np
import matplotlib.pyplot as plt

# Number of random variables
n = 1000

# Generate a sequence of n uniform random variables between 0 and 1
U = np.random.uniform(0, 1, n)

# Compute S_n = sum of U_1 to U_n for each n
S_n = np.cumsum(U)  # cumulative sum of U

# Create the values for each plot
n_values = np.arange(1, n + 1)  # n = 1, 2, ..., 1000
S_n_div_n = S_n / n_values  # S_n / n
S_n_minus_n_over_2 = S_n - n_values / 2  # S_n - n / 2
S_n_minus_n_over_2_div_n = (S_n - n_values / 2) / n_values  # (S_n - n / 2) / n
S_n_minus_n_over_2_div_sqrt_n = (S_n - n_values / 2) / np.sqrt(n_values)  # (S_n - n / 2) / sqrt(n)

# Plot (a) S_n vs n
plt.figure()
plt.plot(n_values, S_n)
plt.title('$S_n vs n$')
plt.xlabel('$n$')
plt.ylabel('$S_n$')
plt.savefig('Sn_vs_n.png')  # Save the figure
plt.close()  # Close the figure to avoid overlap

# Plot (b) S_n / n vs n
plt.figure()
plt.plot(n_values, S_n_div_n)
plt.title('$S_n / n vs n$')
plt.xlabel('$n$')
plt.ylabel('$S_n / n$')
plt.savefig('Sn_div_n_vs_n.png')  # Save the figure
plt.close()

# Plot (c) S_n - n / 2 vs n
plt.figure()
plt.plot(n_values, S_n_minus_n_over_2)
plt.title('$S_n - n / 2 vs n$')
plt.xlabel('$n$')
plt.ylabel('$S_n - n / 2$')
plt.savefig('Sn-n_div_2_vs_n.png')  # Save the figure
plt.close()

# Plot (d) (S_n - n / 2) / n vs n
plt.figure()
plt.plot(n_values, S_n_minus_n_over_2_div_n)
plt.title('$(S_n - n / 2) / n vs n$')
plt.xlabel('$n$')
plt.ylabel('$(S_n - n / 2) / n$')
plt.savefig('(Sn-n_div_2)_div_n_vs_n.png')  # Save the figure
plt.close()

# Plot (e) (S_n - n / 2) / sqrt(n) vs n
plt.figure()
plt.plot(n_values, S_n_minus_n_over_2_div_sqrt_n)
plt.title('$(S_n - n / 2) / \sqrt{n} vs n$')
plt.xlabel('$n$')
plt.ylabel('$(S_n - n / 2) / \sqrt{n}$')
plt.savefig('(Sn-n_div_2)_div_sqrt_n_vs_n.png')  # Save the figure
plt.close()