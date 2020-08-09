import pandas as pd
import pandas_datareader.data as web
import datetime
import yfinance as yf
import csv

yf.pdr_override()
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2019, 1, 1)

with open('stock-code.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

total = pd.DataFrame()
for item in data:
    get_data = web.get_data_yahoo(f'{item[0]}.TW', start, end)
    df1 = pd.DataFrame(get_data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
    total = total.append([df1], ignore_index=False)

total.to_csv(r'test.csv', index=True, header=True)
# TCC = web.get_data_yahoo('1101.TW', start, end)
# ACC = web.get_data_yahoo('1102.TW', start, end)
# UPE = web.get_data_yahoo('1216.TW', start, end)
#
# df1 = pd.DataFrame(TCC, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
# df2 = pd.DataFrame(TCC, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
# df3 = pd.DataFrame(TCC, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
#
# res = df1.append([df2, df3], ignore_index=False)
# res.to_csv(r'test.csv', index=True, header=True)
