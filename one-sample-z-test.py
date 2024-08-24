import numpy as np
from scipy.stats import norm

def one_sample_z_test(sample_data, population_mean, population_std):
    """
    Perform a one-sample Z-test.

    Parameters:
    sample_data (list or array): The sample data to test.
    population_mean (float): The mean of the population to compare against.
    population_std (float): The standard deviation of the population.

    Returns:
    z_score (float): The computed Z-score.
    p_value (float): The p-value corresponding to the Z-score.
    """
    sample_mean = np.mean(sample_data)
    sample_size = len(sample_data)
    standard_error = population_std / np.sqrt(sample_size)
    
    z_score = (sample_mean - population_mean) / standard_error
    p_value = 2 * (1 - norm.cdf(abs(z_score)))

    return z_score, p_value

# Example usage
sample_data = [75, 80, 85, 90, 95]  # Sample data
population_mean = 80  # Hypothetical population mean
population_std = 10   # Hypothetical population standard deviation

z_score, p_value = one_sample_z_test(sample_data, population_mean, population_std)

print(f"Z-score: {z_score}")
print(f"P-value: {p_value}")
