import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox
from math import comb  # For calculating the binomial coefficient

# Load the CSV data
def load_data():
    global df
    try:
        df = pd.read_csv("HR-Employee-Attrition.csv")  # Load your actual CSV file here
        print("Data loaded successfully!")
    except Exception as e:
        messagebox.showerror("File Load Error", f"Error loading the data: {e}")
        df = pd.DataFrame()  # Empty DataFrame on error

# Initialize dataframe
load_data()

# Dictionary to track toggle status
plots_shown = {}

# Function to clear previous charts
def clear_frame():
    for widget in chart_area.winfo_children():
        widget.destroy()

# Function to toggle plots
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
    counts = df.groupby(['MaritalStatus', 'OverTime']).size().unstack()
    fig, ax = plt.subplots(figsize=(8, 5))
    counts.plot(kind='line', marker='o', ax=ax)
    ax.set_title("Marital Status vs Overtime")
    ax.set_xlabel("Marital Status")
    ax.set_ylabel("Count")
    embed_chart(fig)

# Chart 2: Aggregated Bar Plot for Monthly Income vs Monthly Rate
def plot_monthly_income_vs_rate():
    df['IncomeRange'] = pd.cut(df['MonthlyIncome'], bins=np.arange(0, df['MonthlyIncome'].max(), 1000))
    grouped = df.groupby('IncomeRange')['MonthlyRate'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(grouped['IncomeRange'].astype(str), grouped['MonthlyRate'], color='blue')
    ax.set_title("Monthly Income vs Monthly Rate (Aggregated)")
    ax.tick_params(axis='x', rotation=45)
    embed_chart(fig)

# Chart 3: Scatter Plot for Daily Rate vs Monthly Rate
def plot_scatter_daily_rate():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df['DailyRate'], df['MonthlyRate'], alpha=0.6, color='purple')
    ax.set_title("Daily Rate vs Monthly Rate")
    ax.set_xlabel("Daily Rate")
    ax.set_ylabel("Monthly Rate")
    embed_chart(fig)

# Chart 4: Histogram for Years at Company
def plot_histogram_years():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df['YearsAtCompany'], bins=10, alpha=0.7, label="Years at Company")
    ax.hist(df['YearsSinceLastPromotion'], bins=10, alpha=0.7, label="Years Since Last Promotion")
    ax.set_title("Years at Company vs Years Since Last Promotion")
    ax.legend()
    embed_chart(fig)

# Binomial Probability Calculation
def show_binomial_probabilities():
    try:
        n = int(entry_n.get())
        x = int(entry_x.get())
        p = 0.6  # Fixed probability for non-defective
        q = 0.4  # Fixed probability for defective

        binomial_coefficient = comb(n, x)
        probability = binomial_coefficient * (p ** x) * (q ** (n - x))

        result_text = (f"Binomial Probability:\n"
                       f"P(X = {x}) = C({n}, {x}) * p^{x} * q^{n-x}\n"
                       f"P(X = {x}) = {binomial_coefficient} * (0.6)^{x} * (0.4)^{n-x}\n"
                       f"P(X = {x}) ≈ {probability:.4f}")
        label_result.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for n and x.")

# Expectation (Mean)
def show_expectation():
    mean_income = df['MonthlyIncome'].mean()
    mean_rate = df['MonthlyRate'].mean()
    result_text = f"Expectation (Mean):\nMean Monthly Income: {mean_income:.2f}\nMean Monthly Rate: {mean_rate:.2f}"
    label_result.config(text=result_text)

# Covariance and Correlation
def show_cov_corr():
    covariance = df['DailyRate'].cov(df['MonthlyRate'])
    correlation = df['DailyRate'].corr(df['MonthlyRate'])
    result_text = f"Covariance and Correlation:\nCovariance: {covariance:.2f}\nCorrelation: {correlation:.2f}"
    label_result.config(text=result_text)

# Skewness
def show_skewness():
    skew_years = stats.skew(df['YearsAtCompany'])
    skew_salary = stats.skew(df['PercentSalaryHike'])
    result_text = (f"Skewness:\nSkewness (Years at Company): {skew_years:.2f}\n"
                   f"Skewness (Percent Salary Hike): {skew_salary:.2f}")
    label_result.config(text=result_text)

# Embed Matplotlib charts into Tkinter
def embed_chart(fig):
    canvas = FigureCanvasTkAgg(fig, master=chart_area)
    canvas.draw()
    canvas.get_tk_widget().pack()

# GUI Setup
root = tk.Tk()
root.title("Statistics Visualizations and Calculations")
root.configure(bg="#f0f0f0")

# Frame for Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

btn_style = {"font": ("Helvetica", 10), "bg": "#4CAF50", "fg": "white", "relief": "raised", "padx": 5, "pady": 5}
tk.Button(button_frame, text="Marital Status vs Overtime", command=lambda: toggle_plot("marital", plot_marital_overtime), **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Monthly Income vs Rate", command=lambda: toggle_plot("income_rate", plot_monthly_income_vs_rate), **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Scatter Plot (Daily Rate)", command=lambda: toggle_plot("scatter", plot_scatter_daily_rate), **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Histogram (Years)", command=lambda: toggle_plot("histogram", plot_histogram_years), **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Expectation", command=show_expectation, **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Covariance & Correlation", command=show_cov_corr, **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Skewness", command=show_skewness, **btn_style).pack(side=tk.LEFT, padx=5)

# Frame for Binomial Input
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)
tk.Label(input_frame, text="n (trials):", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
entry_n = tk.Entry(input_frame, width=10)
entry_n.grid(row=0, column=1, padx=5)
tk.Label(input_frame, text="x (successes):", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
entry_x = tk.Entry(input_frame, width=10)
entry_x.grid(row=1, column=1, padx=5)
tk.Button(input_frame, text="Calculate Binomial Probabilities", command=show_binomial_probabilities, **btn_style).grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
label_result = tk.Label(root, text="", bg="#f0f0f0", font=("Helvetica", 10), justify="left")
label_result.pack(pady=10)

# Frame for Chart Area
chart_area = tk.Frame(root, bg="white", relief="ridge", bd=2)
chart_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Run the GUI Loop
root.mainloop()
