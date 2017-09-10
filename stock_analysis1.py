import numpy as np 
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pylab as plt
import datetime
import pandas_datareader as pdweb

prices=pdweb.get_data_yahoo(['CVX','XOM','BP'], start=datetime.datetime(2010,1,1),end=datetime.datetime(2013,1,1))['Adj Close']
#volume=pdweb.get_data_yahoo(['CVX','XOM','BP'], start=datetime.datetime(2010,1,1),end=datetime.datetime(2013,1,1))['Volume']



rets = prices.pct_change()

prices.plot()

plt.show()