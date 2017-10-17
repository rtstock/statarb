import statsmodels.tsa.stattools as ts
import numpy as np
import pandas as pd
#import pandas.io.data as wb
from pandas_datareader import data, wb

data1 = data.DataReader('BAC', data_source='yahoo',start='1/1/2016', end='12/31/2017')
data2 = data.DataReader('GOOGL', data_source='yahoo',start='1/1/2016', end='12/31/2017')


data1['key']=data1.index

data2['key']=data2.index

result = pd.merge(data1, data2, on='key')

x1=result['Close_x']
y1=result['Close_y']

#print result

coin_result = ts.coint(y0=x1, y1=y1,return_results=False)
print 't-statistic',coin_result[0]
print 'pvalue',coin_result[1]
print '1%,5%,10%',coin_result[2]
