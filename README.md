# Candlestick Chart Generator for Stocks

Plots a candlestick chart for a given stock. Allows the user to input start date. Also has the option for saving the plot. Written in python3.

---
## How to use

Use -h or --help to get info about arguments.
```python3 candlestick_chart.py -h```

For example to get AAPL stock info from 12th October 2021 till now and save the file as a pdf without displaying the chart in python.
```python3 candlestick_chart.py AAPL 2015 12 10 -tn --noShow -sv example-candlestick-chart.pdf -f pdf```

---
### Dependencies
- datetime
- matplotlib
- pandas_datareader
- mplfinance
