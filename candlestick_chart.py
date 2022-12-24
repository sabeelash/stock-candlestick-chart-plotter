# importing required modules
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import argparse

# Taking arguments parsing
parser = argparse.ArgumentParser(description='Gets a candlestick chart for a stock between a period of time')

parser.add_argument('stock', metavar='stock-ticker', type=str, help='stock ticker symbol')
parser.add_argument('start_year', metavar='start-year', type=int, help='start year')
parser.add_argument('start_month', metavar='start-month', type=int, help='start month')
parser.add_argument('start_day', metavar='start-day', type=int, help='start day')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--end', type=int, nargs=3, metavar=('YEAR', 'MONTH', 'DATE'),
                   help='plots chart till this date')
group.add_argument('-tn', '--till_now', action='store_true', help='shows plot till now')

parser.add_argument('-sv', '--savefile', metavar='FILENAME', type=str, default=False, help='save plot as a png file')
parser.add_argument('-ns', '--noShow', action='store_true', default=False, help='skips showing plot in python')
parser.add_argument('-f', '--format', type=str, default='png', metavar='FILE_FORMAT', help='file format for saved file')
args = parser.parse_args()

# saving parsed arguments into integers
save = args.savefile
noShow = args.noShow
till_now = args.till_now
file_format = args.format
start_year = args.start_year
start_month = args.start_month
start_day = args.start_day

# Setting timeframes
start = dt.datetime(start_year, start_month, start_day)

if not till_now:
    end = args.end
    end_year = end[0]
    end_month = end[1]
    end_day = end[2]
    end = dt.datetime(end_year, end_month, end_day)
else:
    end = dt.datetime.now()

# Load Data
stock_ticker = args.stock
data = web.DataReader(stock_ticker, 'yahoo', start, end)
data = data[['Open', 'High', 'Low', 'Close']]
data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)

# Plot the graph
ax = plt.subplot()
# Plot parameters
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title(stock_ticker + ' Stock Chart', color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='both', labelsize=5)
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width=0.1, colorup='#8ceb34')

# does not show graph if specified by the user
if not noShow:
    plt.show()

# to save file
if save != False:
    plt.savefig(save, format=file_format)
