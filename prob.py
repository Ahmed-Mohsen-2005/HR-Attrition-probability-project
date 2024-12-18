import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox
from math import comb  # For calculating the binomial coefficient
from PIL import Image, ImageTk  # For adding a background image

# Load the CSV data
def load_data():
    global df
    try:
        df = pd.read_csv("HR-Employee-Attrition.csv")  # Replace with your CSV file
        print("Data loaded successfully!")
    except Exception as e:
        messagebox.showerror("File Load Error", f"Error loading the data: {e}")
        df = pd.DataFrame()  # Empty DataFrame on error

# Initialize dataframe
load_data()

# Function to clear previous charts
def clear_frame():
    for widget in chart_area.winfo_children():
        widget.destroy()

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

# Chart 1: Marital Status vs Overtime
def plot_marital_overtime():
    counts = df.groupby(['MaritalStatus', 'OverTime']).size().unstack()
    fig, ax = plt.subplots(figsize=(12, 8))
    counts.plot(kind='line', marker='o', ax=ax)
    ax.set_title("Marital Status vs Overtime")
    ax.set_xlabel("Marital Status")
    ax.set_ylabel("Count")
    embed_chart(fig)

# Chart 2: Aggregated Bar Plot for Monthly Income vs Monthly Rate
def plot_monthly_income_vs_rate():
    df['IncomeRange'] = pd.cut(df['MonthlyIncome'], bins=np.arange(0, df['MonthlyIncome'].max(), 1000))
    grouped = df.groupby('IncomeRange')['MonthlyRate'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(grouped['IncomeRange'].astype(str), grouped['MonthlyRate'], color='blue')
    ax.set_title("Monthly Income vs Monthly Rate (Aggregated)")
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout() 
    embed_chart(fig)

# Chart 3: Scatter Plot for Daily Rate vs Monthly Rate
def plot_scatter_daily_rate():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(df['DailyRate'], df['MonthlyRate'], alpha=0.6, color='purple')
    ax.set_title("Daily Rate vs Monthly Rate")
    ax.set_xlabel("Daily Rate")
    ax.set_ylabel("Monthly Rate")
    embed_chart(fig)

# Chart 4: Histogram for Years at Company
def plot_histogram_years():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.hist(df['YearsAtCompany'], bins=10, alpha=0.7, label="Years at Company")
    ax.hist(df['YearsSinceLastPromotion'], bins=10, alpha=0.7, label="Years Since Last Promotion")
    ax.set_title("Years at Company vs Years Since Last Promotion")
    ax.legend()
    embed_chart(fig)

# Function to embed Matplotlib charts into Tkinter
def embed_chart(fig):
    clear_frame()
    canvas = FigureCanvasTkAgg(fig, master=chart_area)
    canvas.draw()
    canvas.get_tk_widget().pack()

# GUI Setup
root = tk.Tk()
root.title("Full-Page Background with Widgets")
root.state('zoomed')  # Make the window fullscreen

# Background Image
bg_image = Image.open("WhatsApp Image 2024-12-18 at 2.41.44 AM.jpeg")  # Replace with your image file
bg_image = bg_image.resize((1920, 1080), Image.LANCZOS)  # Resize image to fit full screen
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas for background
canvas = tk.Canvas(root, width=1920, height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")  # Place background image

# Buttons and Input Widgets
btn_style = {
    "font": ("Helvetica", 12, "bold"),  # Larger font size
    "bg": "#4CAF50",  # Green background
    "fg": "white",  # White text
    "relief": "raised",
    "padx": 10,  # Padding inside the button
    "pady": 5,   # Padding inside the button
    "width": 25,  # Button width (in characters)
    "height": 3   # Button height (in lines)
}
button_y = 50  # Starting Y position for buttons

tk.Button(root, text="Calculate Binomial Probabilities", command=show_binomial_probabilities, **btn_style).place(x=50, y=button_y)
tk.Button(root, text="Expectation", command=show_expectation, **btn_style).place(x=50, y=button_y + 50)
tk.Button(root, text="Covariance & Correlation", command=show_cov_corr, **btn_style).place(x=50, y=button_y + 100)
tk.Button(root, text="Skewness", command=show_skewness, **btn_style).place(x=50, y=button_y + 150)
tk.Button(root, text="Marital Status vs Overtime", command=plot_marital_overtime, **btn_style).place(x=50, y=button_y + 200)
tk.Button(root, text="Monthly Income vs Rate", command=plot_monthly_income_vs_rate, **btn_style).place(x=50, y=button_y + 250)
tk.Button(root, text="Scatter Plot (Daily Rate)", command=plot_scatter_daily_rate, **btn_style).place(x=50, y=button_y + 300)
tk.Button(root, text="Histogram (Years)", command=plot_histogram_years, **btn_style).place(x=50, y=button_y + 350)

# Input Fields for Binomial Probability (below buttons)
tk.Label(root, text="n (trials):", font=("Helvetica", 10, "bold"), bg="white").place(x=50, y=button_y + 450)
entry_n = tk.Entry(root, width=10, font=("Helvetica", 10))
entry_n.place(x=150, y=button_y + 450)

tk.Label(root, text="x (successes):", font=("Helvetica", 10, "bold"), bg="white").place(x=50, y=button_y + 500)
entry_x = tk.Entry(root, width=10, font=("Helvetica", 10))
entry_x.place(x=150, y=button_y + 500)

# Label to display results (below inputs)
label_result = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="white", fg="black", justify="left")
label_result.place(x=50, y=button_y + 600)

# Chart Area to the left (fills remaining space)
chart_area = tk.Frame(root, bg="gray", relief="ridge", bd=2)
chart_area.place(x=1000, y=50, width=900, height=700)

# Run the GUI
root.mainloop()
