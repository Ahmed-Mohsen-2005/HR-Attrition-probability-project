import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

# Create the dataframe globally for testing purposes
df = pd.DataFrame({
    'MonthlyIncome': np.random.randint(3000, 15000, 20),
    'MonthlyRate': np.random.randint(100, 2000, 20),
    'DailyRate': np.random.randint(100, 500, 20),
    'YearsAtCompany': np.random.randint(1, 20, 20),
    'PercentSalaryHike': np.random.uniform(10, 20, 20),
    'YearsSinceLastPromotion': np.random.randint(1, 5, 20),
    'MaritalStatus': np.random.choice(['Single', 'Married', 'Divorced'], 20),
    'OverTime': np.random.choice(['Yes', 'No'], 20)
})

# Dictionary to track whether a plot is shown or not
plots_shown = {}

# Function to clear all displayed widgets
def clear_frame():
    for widget in frame_canvas_inner.winfo_children():
        widget.destroy()

# Function to toggle a plot
def toggle_plot(plot_name, plot_function):
    if plots_shown.get(plot_name, False):
        clear_frame()
        plots_shown[plot_name] = False
    else:
        clear_frame()
        plot_function()
        plots_shown[plot_name] = True

# Chart 1: Marital Status vs Overtime
def plot_marital_overtime():
    marital_overtime_counts = df.groupby(['MaritalStatus', 'OverTime']).size().unstack()
    fig, ax = plt.subplots(figsize=(8, 5))
    marital_overtime_counts.plot(kind='line', marker='o', linewidth=2, markersize=8, ax=ax)
    ax.set_title('Marital Status vs Overtime')
    ax.set_xlabel('Marital Status')
    ax.set_ylabel('Count of Employees')
    canvas = FigureCanvasTkAgg(fig, master=frame_canvas_inner)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=10, pady=10)

# Chart 2: Bar Plot for Monthly Income vs Monthly Rate
def plot_monthly_income_vs_rate():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df['MonthlyIncome'], df['MonthlyRate'], color='blue', width=2000)
    ax.set_title('Monthly Income vs Monthly Rate')
    ax.set_xlabel('Monthly Income')
    ax.set_ylabel('Monthly Rate')
    canvas = FigureCanvasTkAgg(fig, master=frame_canvas_inner)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=10, pady=10)

# Chart 3: Scatter Plot for Daily Rate vs Monthly Rate
def plot_scatter_daily_rate():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df['DailyRate'], df['MonthlyRate'], alpha=0.5, color='purple')
    ax.set_title('Daily Rate vs Monthly Rate')
    ax.set_xlabel('Daily Rate')
    ax.set_ylabel('Monthly Rate')
    canvas = FigureCanvasTkAgg(fig, master=frame_canvas_inner)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=10, pady=10)

# Chart 4: Histogram for Years at Company vs Years Since Last Promotion
def plot_histogram_years():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df['YearsAtCompany'], bins=10, alpha=0.7, label='Years at Company')
    ax.hist(df['YearsSinceLastPromotion'], bins=10, alpha=0.7, label='Years Since Last Promotion')
    ax.set_title('Years at Company vs Years Since Last Promotion')
    ax.set_xlabel('Years')
    ax.set_ylabel('Frequency')
    ax.legend()
    canvas = FigureCanvasTkAgg(fig, master=frame_canvas_inner)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=10, pady=10)

# Binomial Probability and Equations
def show_binomial_probabilities():
    try:
        n = int(entry_n.get())
        p = float(entry_p.get())
        x = int(entry_x.get())
        prob_exactly = stats.binom.pmf(x, n, p)
        prob_at_most = stats.binom.cdf(x, n, p)
        prob_at_least = 1 - stats.binom.cdf(x - 1, n, p)

        result_text = (f"Binomial Probability Results:\n"
                       f"P(X = {x}) = {prob_exactly:.4f}\n"
                       f"P(X ≤ {x}) = {prob_at_most:.4f}\n"
                       f"P(X ≥ {x}) = {prob_at_least:.4f}")

        equation_text = ("P(X = x) = (nCx) * p^x * (1-p)^(n-x)\n"
                         "P(X ≤ x) = Sum[P(X = i) for i=0 to x]\n"
                         "P(X ≥ x) = 1 - P(X < x)")
        label_equation.config(text=equation_text)
        label_result.config(text=result_text)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Show Expectation (Mean)
def show_expectation():
    mean_income = df['MonthlyIncome'].mean()
    mean_rate = df['MonthlyRate'].mean()
    equation_text = "E(X) = Σ[X * P(X)] or Mean = Sum(X) / N"
    result_text = f"Mean Monthly Income: {mean_income:.2f}\nMean Monthly Rate: {mean_rate:.2f}"
    label_equation.config(text=equation_text)
    label_result.config(text=result_text)

# Show Covariance and Correlation
def show_cov_corr():
    covariance = df['DailyRate'].cov(df['MonthlyRate'])
    correlation = df['DailyRate'].corr(df['MonthlyRate'])
    equation_text = ("Cov(X,Y) = Σ[(X-E[X])(Y-E[Y])] / N\n"
                     "Corr(X,Y) = Cov(X,Y) / (σX * σY)")
    result_text = (f"Covariance: {covariance:.2f}\n"
                   f"Correlation: {correlation:.2f}")
    label_equation.config(text=equation_text)
    label_result.config(text=result_text)

# Show Skewness
def show_skewness():
    skew_years = stats.skew(df['YearsAtCompany'])
    skew_salary = stats.skew(df['PercentSalaryHike'])
    equation_text = "Skewness = Σ[(X-μ)^3] / (N * σ^3)"
    result_text = (f"Skewness (Years at Company): {skew_years:.2f}\n"
                   f"Skewness (Percent Salary Hike): {skew_salary:.2f}")
    label_equation.config(text=equation_text)
    label_result.config(text=result_text)

# Tkinter GUI
root = tk.Tk()
root.title("Statistics Visualizations and Calculations")

# Buttons for Charts
frame_buttons = tk.Frame(root)
frame_buttons.pack(padx=10, pady=10)

tk.Button(frame_buttons, text="Toggle Marital Status vs Overtime", command=lambda: toggle_plot("marital_overtime", plot_marital_overtime)).pack(side='left', padx=5)
tk.Button(frame_buttons, text="Toggle Monthly Income vs Rate", command=lambda: toggle_plot("monthly_income_rate", plot_monthly_income_vs_rate)).pack(side='left', padx=5)
tk.Button(frame_buttons, text="Toggle Scatter Plot (DailyRate)", command=lambda: toggle_plot("scatter_daily_rate", plot_scatter_daily_rate)).pack(side='left', padx=5)
tk.Button(frame_buttons, text="Toggle Histogram (Years)", command=lambda: toggle_plot("histogram_years", plot_histogram_years)).pack(side='left', padx=5)

# Buttons for Equations
tk.Button(frame_buttons, text="Show Binomial Probabilities", command=show_binomial_probabilities).pack(side='left', padx=5)
tk.Button(frame_buttons, text="Show Expectation", command=show_expectation).pack(side='left', padx=5)
tk.Button(frame_buttons, text="Show Covariance & Correlation", command=show_cov_corr).pack(side='left', padx=5)
tk.Button(frame_buttons, text="Show Skewness", command=show_skewness).pack(side='left', padx=5)

# Entry Fields for Binomial Probability
tk.Label(root, text="Enter n (trials):").pack()
entry_n = tk.Entry(root)
entry_n.pack()
tk.Label(root, text="Enter p (success probability):").pack()
entry_p = tk.Entry(root)
entry_p.pack()
tk.Label(root, text="Enter x (successes):").pack()
entry_x = tk.Entry(root)
entry_x.pack()

# Canvas for plots
frame_canvas = tk.Frame(root)
frame_canvas.pack(padx=10, pady=10, fill='both', expand=True)
frame_canvas_inner = tk.Frame(frame_canvas)
frame_canvas_inner.pack(fill='both', expand=True)

# Labels for Equations and Results
label_equation = tk.Label(root, text="Equation will be displayed here", justify='left', anchor="w")
label_equation.pack(padx=10, pady=5)
label_result = tk.Label(root, text="Results will be displayed here", justify='left', anchor="w")
label_result.pack(padx=10, pady=5)

root.mainloop()
