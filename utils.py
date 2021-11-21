import logging
import threading
import yfinance as yf
import pandas_datareader as pdr
import pandas as pd
import json

def get_pchange(letter='BTC-USD', value=20, interval="1d"):
    vars = locals()
    
    tick = yf.Ticker(letter)
    tick_history = pd.DataFrame(tick.history(period="1y", interval=interval))

    x1 = tick_history['Open']
    x2 = tick_history['Close']
    diff = 100*(x2 - x1) / (x1)

    if value < 0:
        aux = diff <= value
    else:
        aux = diff >= value
        
    pdrop_prob = 100*(aux.sum() / diff.count())
    pdrop_prob = round(pdrop_prob, 2)
    vars['prob'] = pdrop_prob
    
    return vars

def get_pchange_history(letter='BTC-USD', value=20, interval=None, tick_history=None):
    vars = locals()
    x1 = tick_history['Open']
    x2 = tick_history['Close']
    diff = 100*(x2 - x1) / (x1)

    if value < 0:
        aux = diff <= value
    else:
        aux = diff >= value
        
    pdrop_prob = 100*(aux.sum() / diff.count())
    pdrop_prob = round(pdrop_prob, 2)
    vars['prob'] = pdrop_prob
    
    return vars


def get_all_intervals(letter='BTC-USD', value=20):
    result = []
    intervals = ["1h", "1d", "5d", "1wk", "1mo", "3mo"]
    tick = yf.Ticker(letter)
    
    for inter in intervals:
        tick_history = pd.DataFrame(tick.history(period="1y", interval=inter))
        v = get_pchange(letter=letter, value=value, interval=inter, tick_history=tick_history)
        result.append(v)
    return result

def get_matrix_change(letter='BTC-USD'):
    print('calculating Matrix....')
    tick = yf.Ticker(letter)
    result = []
    
    # define intervals and values
    intervals = ["1h", "1d", "5d", "1wk", "1mo", "3mo"]
    values = [-10, -5, -3, -2, -1]
    values = values+list(map(abs, values))[::-1]
    
    for inter in intervals:    
        tick_history = pd.DataFrame(tick.history(period="1y", interval=inter))
        for value in values:
            v = get_pchange_history(letter=letter, value=value, interval=inter, tick_history=tick_history)
            result.append(v)
        
    # treat DF
    df = pd.DataFrame.from_dict(result)
    
    df = df.pivot('value','interval','prob')
    df = df[intervals]
    df.index.names = ['change (%)']
    print('done')
    return df

if __name__ == "__main__":    
    # 1 -- get probability of a percentage change in an interval
    # example: what is the prbability that bitcoin drops 10% in 1day?
    a = get_pchange(letter='BTC-USD', value=-10, interval="1d")
    print(a)
    
    # 2 -- get probability of a percentage change
    # example: what is the prbability that bitcoin drops 10%?
    b = get_all_intervals(letter='BTC-USD', value=-10)
    print(b)
    
    # 3 -- get matrix of probability
    # example: what are probabilities of changes for Bitcoin?
    c = get_matrix_change('BTC-USD')
    print(c)
