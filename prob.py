import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, binom, norm, lognorm, beta, uniform, skew, ttest_ind
import math

# 1. Load the dataset

file_path = 'HR-Employee-Attrition.csv'  # Replace with your file path
df = pd.read_csv(file_path)
print('Our Probability project')




# Display the first few rows to understand the dataset structure

print("First few rows of the dataset:")
print(df.head())



# 2. Extract relevant columns for analysis

MaritalStatus=df['MaritalStatus']
OverTime=df['OverTime']
daily_rate = df['DailyRate']
monthly_income = df['MonthlyIncome']
MonthlyRate=df['MonthlyRate']
years_at_company = df['YearsAtCompany']
years_since_last_promotion = df['YearsSinceLastPromotion']
job_satisfaction = df['JobSatisfaction']
YearsAtCompany=df['YearsAtCompany']
PercentSalaryHike=df['PercentSalaryHike']
TotalWorkingYears=df['TotalWorkingYears']





#MaritalStatus  &  OverTime ----->distribution (lec 4 slide 6)
#monthly_income  &  MonthlyRate ---->expictation(line chart)
#daily_rate   &   MonthlyRate -------->covarince&correlation(scatter plot)
#years_at_company  &  years_since_last_promotion ----------> (freq histogram)
#years_at_company  &  PercentSalaryHike --------> skewness(curved graph)
#TotalWorkingYears   &   job_satisfaction --------------> 







# 3. Statistical Analysis

#first releation
def calculate_probability(n, p, x):
    """
    Calculate the probability of exactly 'x' non-defective chips
    in 'n' trials with a success probability 'p' for each trial
    """
    # Binomial probability: P(X = x)
    probability_exactly_x = stats.binom.pmf(x, n, p)
    return probability_exactly_x

def probability_at_most(n, p, x):
    """
    Calculate the probability of at most 'x' non-defective chips
    (i.e., P(X <= x))
    """
    probability_at_most_x = stats.binom.cdf(x, n, p)
    return probability_at_most_x

def probability_at_least(n, p, x):
    """
    Calculate the probability of at least 'x' non-defective chips
    (i.e., P(X >= x)) = 1 - P(X < x)
    """
    probability_at_least_x = 1 - stats.binom.cdf(x-1, n, p)
    return probability_at_least_x

# User input example
n = int(input("Enter the number of chips (n): "))
p = float(input("Enter the probability of a non-defective chip (p): "))
x = int(input("Enter the number of non-defective chips for the calculation (x): "))

# Calculate probabilities
prob_exactly_x = calculate_probability(n, p, x)
prob_at_most_x = probability_at_most(n, p, x)
prob_at_least_x = probability_at_least(n, p, x)

# Display the results
print(f"\nFor a total of {n} chips with probability {p} of being non-defective:")
print(f"i. The probability of exactly {x} non-defective chips is: {prob_exactly_x:.4f}")
print(f"ii. The probability of at least {x} non-defective chips is: {prob_at_least_x:.4f}")
print(f"iii. The probability of at most {x} non-defective chips is: {prob_at_most_x:.4f}")


#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
#second releation
#  Calculate the Expectation (Mean) for MonthlyIncome and MonthlyRate
mean_monthly_income = np.mean(df['MonthlyIncome'])
mean_monthly_rate = np.mean(df['MonthlyRate'])
print(f"Expected Monthly Income (Mean): {mean_monthly_income}")
print(f"Expected Monthly Rate (Mean): {mean_monthly_rate}")
#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------





#                                                                            4. Visualization
#first
marital_overtime_counts = df.groupby(['MaritalStatus', 'OverTime']).size().unstack()

# Plotting
plt.figure(figsize=(10, 6))
marital_overtime_counts.plot(kind='line', marker='o', linewidth=2, markersize=8)

# Add titles and labels
plt.title('Relation Between Marital Status and OverTime')
plt.xlabel('Marital Status')
plt.ylabel('Count of Employees')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend(title='OverTime', loc='upper left', labels=['No Overtime', 'Overtime'])

# Show the plot
plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------

plt.figure(figsize=(10, 6))

# Plotting line chart to show relationship between MonthlyIncome and MonthlyRate
plt.plot(df['MonthlyIncome'], df['MonthlyRate'], label='Monthly Income vs Monthly Rate', color='blue', linestyle='-', marker='o')

# Adding Titles and Labels
plt.title('Relationship between Monthly Income and Monthly Rate', fontsize=14)
plt.xlabel('Monthly Income', fontsize=12)
plt.ylabel('Monthly Rate', fontsize=12)

# Display the plot
plt.grid(True)
plt.legend()
plt.show()

# 4. Scatter Plot for Better Visualization
plt.figure(figsize=(10, 6))
plt.scatter(df['MonthlyIncome'], df['MonthlyRate'], alpha=0.5, color='green')

plt.title('Scatter Plot of Monthly Income vs Monthly Rate', fontsize=14)
plt.xlabel('Monthly Income', fontsize=12)
plt.ylabel('Monthly Rate', fontsize=12)
plt.grid(True)