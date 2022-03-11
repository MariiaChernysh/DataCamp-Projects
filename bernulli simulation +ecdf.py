import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Bernulli trials simulation
def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0
    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random(1)
        # If less than p, it's a success so add one to n_success
        if random_number < p:
            n_success+=1
    return n_success

#Let's say a bank made 100 mortgage loans. It is possible that anywhere between 0 and 100 of the loans will be
# defaulted upon. You would like to know the probability of getting a given number of defaults, given that the
# probability of a default is p = 0.05

# Seed random number generator
np.random.seed(42)

# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100, 0.05)

# Plot the histogram with default number of bins; label your axes
sns.set_theme()
_ = plt.hist(n_defaults, normed=True)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')

# Show the plot
plt.show()

# Compute ECDF: x, y
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n
    return x, y

x, y = ecdf(n_defaults)
# Plot the ECDF with labeled axes. probability that the bank will lose money if 10 or more of its loans are defaulted
plt.plot(x, y, marker = '.', linestyle = 'none')
plt.xlabel('ecdf of loans ')
plt.ylabel('probability')

# Show the plot
plt.show()

# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money = np.sum(n_defaults>= 10)

# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / len(n_defaults))
