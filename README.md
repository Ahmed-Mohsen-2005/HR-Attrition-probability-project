# HR Analytics Dashboard (Tkinter GUI with Data Visualization)

This is a desktop application built using Python's Tkinter library. It analyzes HR data from a CSV file (`HR-Employee-Attrition.csv`) and provides interactive visualizations and statistical insights like expectation, covariance, correlation, skewness, and binomial probabilities.

---

## 📁 Files Required

- `HR-Employee-Attrition.csv` — The dataset file. Make sure it's in the same directory as the script.
- `WhatsApp Image 2024-12-18 at 2.41.44 AM.jpeg` — Background image used in the application. Place it in the same directory or update the filename in the code.

---

## 🚀 Features

- **Binomial Probability Calculator** (with fixed probability `p = 0.6`, `q = 0.4`)
- **Statistical Metrics**:
  - Expectation (mean of Monthly Income and Monthly Rate)
  - Covariance and Correlation (between Daily Rate and Monthly Rate)
  - Skewness (for Years at Company and Percent Salary Hike)
- **Data Visualizations**:
  - Line chart: Marital Status vs Overtime
  - Bar chart: Monthly Income vs Monthly Rate
  - Scatter plot: Daily Rate vs Monthly Rate
  - Histogram: Years at Company vs Years Since Last Promotion

---

## 📊 Libraries Used

- `pandas` – Data manipulation
- `numpy` – Numeric computations
- `matplotlib` – Plotting and visualizations
- `scipy.stats` – Statistical metrics
- `PIL` (Pillow) – Background image handling
- `tkinter` – GUI framework
- `math` – For binomial coefficient

---

## 🖼️ GUI Details

- Fullscreen window with background image
- Left side: Buttons for all statistical and visualization functions
- Center-right: Chart display area
- Bottom-left: Entry fields and result labels for binomial probability calculation

---

## 🛠️ How to Run

1. Install the required libraries (if not already installed):

    ```bash
    pip install pandas matplotlib scipy pillow
    ```

2. Ensure the following files are in the same folder:
    - The Python script
    - `HR-Employee-Attrition.csv`
    - Background image (`WhatsApp Image 2024-12-18 at 2.41.44 AM.jpeg`)

3. Run the script:

    ```bash
    python your_script_name.py
    ```

---

## 🧮 Sample Input for Binomial Probability

- `n (trials)`: 10
- `x (successes)`: 6
- This will calculate:  
  `P(X=6) = C(10,6) * (0.6)^6 * (0.4)^4`

---

## 📌 Notes

- You can replace the CSV or image file by updating the filenames in the script.
- The GUI is optimized for 1920x1080 screen resolution (fullscreen view).
- If any errors occur (e.g., file not found), appropriate error dialogs will be shown.

---

## 📷 Screenshot


---

## 📄 License

This project is for educational and non-commercial purposes.

