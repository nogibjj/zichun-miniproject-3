import os
import polars as pl
import matplotlib
import matplotlib.pyplot as plt

# Set matplotlib to use 'Agg' backend to work in headless environments
matplotlib.use('Agg')

# Ensure the output directory exists
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the dataset using Polars
data = pl.read_csv('data/medals_total.csv')

# Generate summary statistics for Total Medals (for all data)
summary_stats = data.select([
    pl.col('Total').mean().alias('mean'),
    pl.col('Total').median().alias('median'),
    pl.col('Total').std().alias('std_dev'),
    pl.col('Total').min().alias('min'),
    pl.col('Total').max().alias('max')
])

# Sort the data by 'Total' column in descending order and take the top 50 countries
top_countries = data.sort('Total', reverse=True).head(50)

# Create a bar chart for total medals by top 50 countries
plt.figure(figsize=(10, 6))
plt.bar(top_countries['country'], top_countries['Total'], color='skyblue')
plt.title('Total Medals by Top 50 Countries')
plt.xlabel('Country')
plt.ylabel('Total Medals')
plt.xticks(rotation=90)
plt.tight_layout()

# Save the plot
plt.savefig(f'{output_dir}/total_medals_by_top_50_countries.png')

# Explicitly close the plot
plt.close()

# Save summary statistics for the entire dataset to markdown file
with open(f'{output_dir}/summary_report.md', 'w') as f:
    f.write("# Summary Statistics Report (Entire Dataset using Polars)\n\n")
    f.write(f"## Mean Total Medals: {summary_stats['mean'][0]}\n")
    f.write(f"## Median Total Medals: {summary_stats['median'][0]}\n")
    f.write(f"## Standard Deviation of Total Medals: {summary_stats['std_dev'][0]}\n")
    f.write(f"## Min Total Medals: {summary_stats['min'][0]}\n")
    f.write(f"## Max Total Medals: {summary_stats['max'][0]}\n")
    f.write("## Data Visualization for Top 50 Countries\n")
    f.write("![Total Medals by Top 50 Countries](total_medals_by_top_50_countries.png)\n")

# Print summary statistics for verification
print(summary_stats)
