import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    ax = plt.axes()
    ax.scatter(
    data=df,
    x='Year',
    y='CSIRO Adjusted Sea Level',
    label='Scatterplot'
    )

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line_of_best_fit = lambda x: (slope * x) + intercept
    sea_level_1880 = line_of_best_fit(1880)
    sea_level_2050 = line_of_best_fit(2050)

    ax.plot(
    [1880, 2050],
    [sea_level_1880, sea_level_2050],
    'r'
    )

    # Create second line of best fit
    df_modern = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_modern['Year'], df_modern['CSIRO Adjusted Sea Level'])
    line_of_best_fit_modern = lambda x: (slope * x) + intercept
    sea_level_2000_modern = line_of_best_fit_modern(2000)
    sea_level_2050_modern = line_of_best_fit_modern(2050)

    ax.plot(
    [2000, 2050],
    [sea_level_2000_modern, sea_level_2050_modern],
    'g'
    )

    # Add lavels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()