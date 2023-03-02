# JEPI-ETF-Analysis-and-Predictor


Introduction:
This is a Python script for analyzing the daily stock prices of JP Morgan Equity Premium Income ETF (JEPI) and S&P 500 Index (SPY). The script includes data cleaning, merging of dataframes, creation of new columns, and visualization of the data.

Dependencies:
numpy
pandas
matplotlib
seaborn
datetime
sklearn
xgboost

Usage:
To use this script, first download the required data files, which are in CSV format, and replace the file paths in the script with your own file paths.
Run the script using a Python interpreter or IDE.
The output will be visualizations of the stock prices and returns of the two assets.
Process
Import the required libraries and suppress warnings.
Import the stock price data for JEPI and SPY from CSV files.
Convert the date columns of both dataframes to datetime format.
Create basic plots of JEPI and SPY daily closing prices.
Get the SPY time frame that matches JP Morgan ETF data.
Merge the dataframes to begin plotting comparisons and calculate the daily returns of each asset.
Output summary statistics of the returns.
Visualize the adjusted close for the JP Morgan ETF and SPY500 in a single plot.
Plot barplots of returns to compare means.
Conclusion
This script provides a basic analysis of the daily stock prices of JP Morgan Equity Premium Income ETF and S&P 500 Index. By visualizing the data, one can see the trends and patterns of each asset and compare their performance over time. It can be modified and expanded to suit more specific research needs.