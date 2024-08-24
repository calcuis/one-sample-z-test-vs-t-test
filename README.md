#### one-sample-z-test
```
py one-sample-z-test.py
```
#### one-sample-t-test
```
py one-sample-t-test.py
```
### (one-sample) z-test vs t-test 
The main difference between a one-sample Z-test and a one-sample T-test lies in the assumptions about the population standard deviation and the sample size:
#### Population Standard Deviation
One-Sample Z-Test:
- Known Population Standard Deviation: The Z-test is used when the population standard deviation (σ) is known.
- Normal Distribution: It's also generally assumed that the population is normally distributed, especially if the sample size is small.

One-Sample T-Test:
- Unknown Population Standard Deviation: The T-test is used when the population standard deviation is unknown. Instead, the sample standard deviation (s) is used as an estimate.
- Small Sample Size: The T-test is particularly suitable for small sample sizes (typically less than 30) because it accounts for the additional uncertainty introduced by estimating the population standard deviation from the sample.
#### Distribution
One-Sample Z-Test:
- Standard Normal Distribution: The Z-test relies on the standard normal distribution (mean = 0, standard deviation = 1). This is because the Z-test uses the known population standard deviation, which allows for precise calculations based on the normal distribution.

One-Sample T-Test:
- T-Distribution: The T-test uses the t-distribution, which is similar to the normal distribution but has heavier tails. The t-distribution accounts for the additional variability that comes from estimating the population standard deviation from the sample. The shape of the t-distribution depends on the degrees of freedom (sample size - 1), becoming closer to the normal distribution as the sample size increases.
#### Sample Size
One-Sample Z-Test:
- Large Sample Size: The Z-test is typically used when the sample size is large (usually n > 30), where the Central Limit Theorem ensures that the sampling distribution of the sample mean is approximately normal, even if the population distribution is not normal.

One-Sample T-Test:
- Small Sample Size: The T-test is more appropriate for small sample sizes because it corrects for the increased uncertainty in estimating the population standard deviation.
#### Summary
- Use a Z-test when the population standard deviation is known and the sample size is large.
- Use a T-test when the population standard deviation is unknown and/or the sample size is small.

In practice, because the population standard deviation is rarely known, the t-test is more commonly used.
