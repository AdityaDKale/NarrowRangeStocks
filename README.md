# Narrow Range Stock Analysis

This Python script is designed to perform Narrow Range analysis on a list of stock symbols retrieved from the NSE (National Stock Exchange, India) and save the results to an Excel file. The Narrow Range analysis calculates the percentage difference between the opening and closing prices of a stock for a specified period. If the percentage difference is within a certain threshold (e.g., 1%), the stock is classified as having a "Narrow Range."

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- The `pandas` library (`pip install pandas`)
- The `requests` library (`pip install requests`)

## Usage

1. Clone this repository or copy the script to your project directory.
2. Ensure you have the necessary libraries installed.
3. Run the script using the command: `python Narrow Range 2.0.py`.

## Features

- Retrieves stock symbols from NSE's pre-open market data.
- Performs Narrow Range analysis for each stock based on historical price data.
- Generates a table with columns: Symbol, Narrow Range (True/False), Percentage Difference.
- Saves the results to an Excel file with the date and "Narrow Range.xlsx" as the filename.

## Configuration

- The script fetches stock symbols from NSE's pre-open market data.
- Adjust the threshold percentage for defining a "Narrow Range" by updating the `perc_diff <= 1` condition.

## Notes

- The script uses Yahoo Finance to fetch historical stock price data for analysis.
- This script is provided for educational purposes and basic stock analysis. It can be extended and customized for more advanced analysis and trading strategies.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer:** This script provides basic stock analysis and does not constitute financial advice. Trading and investing involve risks, and decisions should be made based on thorough research and consultation with financial professionals.
