# Mini Project 3 - Polars vs Pandas Comparison

This project compares the performance of Polars and Pandas for performing descriptive statistics and generating data visualizations.

## Dataset

The dataset used for this analysis is the 'medals_total.csv' file, which contains the total medals won by various countries in the Paris 2024 Olympic Games.

## Features

1. **Descriptive Statistics (Polars)**:
   - Mean, median, standard deviation, min, and max of total medals won by all countries.

2. **Data Visualization**:
   - A bar chart showing the total medals won by the top 50 countries.

3. **Output**:
   - Summary statistics for the entire dataset saved as `summary_report.md`.
   - A visualization saved as `total_medals_by_top_50_countries.png`.

## Instructions

1. **Clone the repository**:
    ```bash
    git clone <your-repo-url>
    cd <repo-directory>
    ```

2. **Install the required dependencies**:
    Ensure you have Python 3.6+ installed. Then, install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:
    Run the Python script to generate the summary statistics and the visualization.
    ```bash
    python src/main.py
    ```

4. **CI/CD Pipeline**:
    The CI/CD pipeline automatically runs the script, generates the markdown report and visualization, and pushes them to the repository if there are changes.

## Deliverables

1. **Repository URL**: [Link to the public repository](#)
2. **Summary Report**: The `summary_report.md` file containing descriptive statistics.
3. **Visualization**: The `total_medals_by_top_50_countries.png` showing the total medals won by the top 50 countries.
