import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, binom, norm, lognorm, beta, uniform, skew, kurtosis, ttest_ind

# 1. Load the dataset
file_path = 'HR-Employee-Attrition.csv'  # Replace with your file path
df = pd.read_csv(file_path)

print('Our Probability project')
# Display the first few rows to understand the dataset structure
print("First few rows of the dataset:")
print(df.head())

# 2. Extract relevant columns for analysis
age = df['Age']
distance_from_home = df['DistanceFromHome']
daily_rate = df['DailyRate']
monthly_income = df['MonthlyIncome']
years_at_company = df['YearsAtCompany']
years_since_last_promotion = df['YearsSinceLastPromotion']
job_satisfaction = df['JobSatisfaction']
work_life_balance = df['WorkLifeBalance']

# 3. Statistical Analysis

# Mean and Standard Deviation
mean_age = np.mean(age)
std_age = np.std(age)

mean_income = np.mean(monthly_income)
std_income = np.std(monthly_income)

mean_years_company = np.mean(years_at_company)
std_years_company = np.std(years_at_company)

# Skewness and Kurtosis
skew_age = skew(age)
kurt_age = kurtosis(age)

skew_income = skew(monthly_income)
kurt_income = kurtosis(monthly_income)

# Poisson Distribution: Modeling "YearsSinceLastPromotion"
lambda_promotion = np.mean(years_since_last_promotion)
poisson_promotion = poisson.pmf(np.arange(0, 10), lambda_promotion)

# Binomial Distribution: JobSatisfaction (Assume levels 1 to 4)
n = 4  # Satisfaction levels 1 to 4
p_satisfaction = np.mean(job_satisfaction) / n
binomial_satisfaction = binom.pmf(np.arange(0, 5), n, p_satisfaction)

# Normal Distribution: "MonthlyIncome"
income_range = np.linspace(min(monthly_income), max(monthly_income), 100)
normal_income = norm.pdf(income_range, mean_income, std_income)

# 4. Visualization

plt.figure(figsize=(12, 10))

# Age Distribution
plt.subplot(3, 2, 1)
plt.hist(age, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Monthly Income Distribution with Normal Curve
plt.subplot(3, 2, 2)
plt.hist(monthly_income, bins=15, density=True, alpha=0.6, color='orange', edgecolor='black')
plt.plot(income_range, normal_income, color='red', linestyle='--', label='Normal Curve')
plt.title('Monthly Income Distribution')
plt.xlabel('Monthly Income')
plt.ylabel('Density')
plt.legend()

# Years Since Last Promotion (Poisson)
plt.subplot(3, 2, 3)
plt.hist(years_since_last_promotion, bins=10, color='green', alpha=0.7, edgecolor='black')
plt.plot(np.arange(0, 10), poisson_promotion, 'bo-', label='Poisson PMF')
plt.title('Years Since Last Promotion')
plt.xlabel('Years')
plt.ylabel('Frequency')
plt.legend()

# Job Satisfaction (Binomial)
plt.subplot(3, 2, 4)
plt.bar(np.arange(0, 5), binomial_satisfaction, color='purple', alpha=0.7)
plt.title('Job Satisfaction Distribution (Binomial)')
plt.xlabel('Satisfaction Level')
plt.ylabel('Probability')

# Distance from Home
plt.subplot(3, 2, 5)
plt.hist(distance_from_home, bins=10, color='pink', edgecolor='black', alpha=0.7)
plt.title('Distance from Home Distribution')
plt.xlabel('Distance (in km)')
plt.ylabel('Frequency')

# Work-Life Balance Distribution
plt.subplot(3, 2, 6)
plt.hist(work_life_balance, bins=4, color='cyan', edgecolor='black', alpha=0.7)
plt.title('Work-Life Balance Levels')
plt.xlabel('Balance Level')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# 5. Summary Statistics
print("Statistical Analysis Results:")
print(f"Age: Mean = {mean_age}, Standard Deviation = {std_age}, Skew = {skew_age}, Kurtosis = {kurt_age}")
print(f"Monthly Income: Mean = {mean_income}, Standard Deviation = {std_income}, Skew = {skew_income}, Kurtosis = {kurt_income}")
print(f"Years at Company: Mean = {mean_years_company}, Standard Deviation = {std_years_company}")
print(f"Poisson Distribution (YearsSinceLastPromotion): Lambda = {lambda_promotion}")
print(f"Binomial Distribution (JobSatisfaction): n = {n}, p = {p_satisfaction}")