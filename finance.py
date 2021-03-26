import yfinance as yf
import numpy as np

def get_series_values(currency):
    msft_func = yf.Ticker(currency)
    hist_func = msft_func.history(period="1mo")
    time = list(hist_func.index.values.astype(np.int64) / 1.0e9) #0
    open = list(hist_func["Open"].values) #1
    close = list(hist_func["Close"].values) #2
    high = list(hist_func["High"].values) #3
    low = list(hist_func["Low"].values) #4
    return [time, open, close, high, low]
