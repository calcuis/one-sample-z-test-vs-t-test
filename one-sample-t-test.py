import numpy as np
from scipy import stats

def one_sample_t_test(sample_data, population_mean):
    """
    Perform a one-sample t-test.

    Parameters:
    sample_data (list or array): The sample data to test.
    population_mean (float): The mean of the population to compare against.

    Returns:
    t_statistic (float): The computed t-statistic.
    p_value (float): The p-value corresponding to the t-statistic.
    """
    sample_mean = np.mean(sample_data)
    sample_size = len(sample_data)
    sample_std = np.std(sample_data, ddof=1)  # Use ddof=1 to get the sample standard deviation
    
    standard_error = sample_std / np.sqrt(sample_size)
    
    t_statistic = (sample_mean - population_mean) / standard_error
    p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), df=sample_size-1))

    return t_statistic, p_value

# Example usage
sample_data = [75, 80, 85, 90, 95]  # Sample data
population_mean = 80  # Hypothetical population mean

t_statistic, p_value = one_sample_t_test(sample_data, population_mean)

print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
