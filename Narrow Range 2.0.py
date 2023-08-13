# !/usr/bin/env python
# coding: utf-8


# Importing Libraries

import datetime
import pandas as pd
from time import sleep
from sys import stdout
import requests
import os


# Datetime to timestamp


print('Collecting Dates.....')
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=10)
string = str(yesterday)
element = datetime.datetime.strptime(string, "%Y-%m-%d")

timestamp = datetime.datetime.timestamp(element)
period1 = int(timestamp)

tomorrow = today - datetime.timedelta(days=-1)
string = str(tomorrow)
element = datetime.datetime.strptime(string, "%Y-%m-%d")

timestamp = datetime.datetime.timestamp(element)
period2 = int(timestamp)


print('Creating blank table......')

# Generating Blank Table

table = pd.DataFrame(
    columns=['Symbol', 'Narrow Range', 'Percentage Difference'])


print('Getting Stock List......')
print()


# Progress Bar


def drawProgressBar(percent, barLen=20):
    # percent float from 0 to 1.
    stdout.write("\r")
    stdout.write("[{:<{}}] {:.0f}%".format(
        "=" * int(barLen * percent), barLen, percent * 100))
    stdout.flush()

# List of stocks


try:
    print("Getting Stock List from NSE..")
    h1 = {"Host": "www.nseindia.com",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept":
              "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
              "Referer": r"https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market"
          }

    r = requests.get(h1["Referer"], headers=h1).cookies
    query = r'https://www.nseindia.com/api/market-data-pre-open?key=NIFTY&csv=true'
    a = requests.get(query, headers=h1, cookies=r)
except:
    print("Unable to get Stock List from NSE")

# Creating a Temporary txt file
print("")
print("Creating Temporary file..")
with open('tempFile.txt', 'w') as f:
    f.write(str(a.text))
print("Loading Stock List")
try:
    db = pd.read_csv("tempFile.txt")
except:
    print("Unable to load Stock List into csv")
print("Removing temp file")
os.remove('tempFile.txt')

print("Loading Stock List Database")
print("Creating Symbols..")

# Creating Pre-Open database

SYMBOLS = db.iloc[:, 0].to_list()

print()
print('Collecting and adding data to the table......')

# Get and append data to Pandas

progress = 0
for stock in SYMBOLS:
    query = f'https://query1.finance.yahoo.com/v7/finance/download/{stock}.NS?period1={period1}&period2={period2}&interval=1d&events=history&includeAdjustedClose=true'
    df = pd.read_csv(query)
    df.sort_index(ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    perc_diff = ((abs(df['Close'][0] - df['Open'][2])) /
                 ((df['Close'][0] + df['Open'][2])/2)) * 100
    is_narrow_range = perc_diff <= 1
    table = table.append({'Symbol': stock, 'Narrow Range': is_narrow_range,
                         'Percentage Difference': round(perc_diff, 2)}, ignore_index=True)
    progress = progress + 0.02
    drawProgressBar(progress, 100)

    sleep(0.1)


# Saving to csv

print()
print('Saving file...')
table.to_excel(f'{today} - Narrow Range.xlsx', index=False)
print(table)
input('Press enter to exit.. ')
