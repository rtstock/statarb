
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:18:11 2015

@author: justin.malinchak
"""
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
#import pandas.io.data as web
from pandas_datareader import data, wb
import pprint
import statsmodels.tsa.stattools as ts
#from pandas.stats.api import ols
import statsmodels.api as sm
import datetime


class analyze:

    
    def __init__(self,
                 pairlist,startdate, enddate, showplot = True):
        df = self.analyzepair(pairlist, startdate, enddate, showplot)
        

    def analyzepair(self,pairlist,startdate,enddate,showplot
                    ):

        s1 = pairlist[0]
        s2 = pairlist[1]
        print '---------------------'
        print 'Doing',s1, s2
    
        #startdatetime = datetime.datetime(2015, 1, 1)
        #enddatetime = datetime.datetime(2017, 9, 30)
        startdatetime = datetime.datetime.strptime(startdate,"%Y-%m-%d")
        enddatetime = datetime.datetime.strptime(enddate,"%Y-%m-%d")
        #print startdatetime
        #print enddatetime
        #stop
        prices1 = data.DataReader(s1, "yahoo", startdatetime, enddatetime)
        prices2 = data.DataReader(s2, "yahoo", startdatetime, enddatetime)

        df_a = pd.DataFrame(index=prices1.index)
        df_a[s1] = prices1["Close"]
        df_a[s2] = prices2["Close"]
        df = df_a.dropna(axis=0, how='any')
        
        y = prices1["Close"]
        y.name = s1
        X = prices2["Close"]
        X.name = s1
        X = sm.add_constant(X)
        
        res_ols = sm.OLS(y, X).fit()
        intercept = res_ols.params[0]
        slope = res_ols.params[1]
        print res_ols.params
        self.plot_scatter_series(df, s2, s1,slope,intercept)
        

    def plot_price_series(self, df, ts1, ts2,startdate,enddate):
        months = mdates.MonthLocator()  # every month
        fig, ax = plt.subplots()
        ax.plot(df.index, df[ts1], label=ts1)
        ax.plot(df.index, df[ts2], label=ts2)
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.set_xlim(startdate,enddate)
        ax.grid(True)
        fig.autofmt_xdate()

        plt.xlabel('Month/Year')
        plt.ylabel('Price ($)')
        plt.title('%s and %s Daily Prices' % (ts1, ts2))
        plt.legend()
        plt.show()


    def plot_scatter_series(self, df, ts1, ts2,slope,intercept):
        plt.xlabel('%s Price ($)' % ts1)
        plt.ylabel('%s Price ($)' % ts2)
        plt.title('%s and %s Price Scatterplot' % (ts1, ts2))
        
##        
##        x = df[ts1]
##        a, b = np.polyfit(df[ts1], df[ts2], deg=1)
##        f = lambda x: a*x - b
##        print f(x)
        plt.scatter(df[ts1], df[ts2])
        f = lambda x: slope*x + intercept
        x = df[ts1]
        plt.plot(x,f(x),lw=2.5, c="k",label="regression line")
        plt.show()


        # cadf.py

    def plot_residuals(self, df,startdate,enddate):
        months = mdates.MonthLocator()  # every month
        fig, ax = plt.subplots()
        ax.plot(df.index, df["res"], label="Residuals")
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.set_xlim(startdate, enddate)
        #datetime.datetime(2012, 1, 1)
        #datetime.datetime(2013, 1, 1)
        ax.grid(True)
        fig.autofmt_xdate()

        plt.xlabel('Month/Year')
        plt.ylabel('Price ($)')
        plt.title('Residual Plot')
        plt.legend()

        plt.plot(df["res"])
        plt.show()


if __name__=='__main__':
    #pairlist = ['AAP','AAPL']
    #pairlist = ['CA',     'CHD']
    #pairlist = ['MSFT','PCLN']
    #pairlist = ['PCLN','MSFT']
    pairlist = ['BA','MSFT']
    o = analyze(pairlist,'2015-09-30','2017-09-30',True)
