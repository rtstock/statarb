
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

class output:

    
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
        #print df
        if showplot == True:
            # Plot the two time series
            self.plot_price_series(df, s1, s2,startdatetime,enddatetime)

                #Display a scatter plot of the two time series
            self.plot_scatter_series(df, s1, s2)
        
        
        Y=df[s2].tolist()
        X=df[s1].tolist()
        #print 'got here 1'
        # Calculate optimal hedge ratio "beta"
        #print Y
        #print X
        res = sm.OLS(Y,X)
        #print 'got here 2'
        results = res.fit()
        #print 'got here 3'
        beta_hr = results.params
        #print 'got here 4'
        # Calculate the residuals of the linear combination
        df["res"] = df[s2] - beta_hr*df[s1]

        if showplot == True:
                # Plot the residuals
            self.plot_residuals(df,startdatetime,enddatetime)
                
        # Calculate and output the CADF test on the residuals
        #print 'got here 5'
        #print df["res"]
        cadf = ts.adfuller(df["res"])
        #print 'got here 6'
        #pprint.pprint(cadf)
        #print 'cadf[0]', cadf[0]
        test_null_hypothesis = cadf[0]
        five_percent_value = cadf[4]['5%']
        print ''
        print test_null_hypothesis, 'must be less than',five_percent_value
        mylist = [s1,s2,c1,test_null_hypothesis]
        with open(myfileoutput, 'a') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(mylist)

        if float(test_null_hypothesis) < float(five_percent_value):

            dict_a = {'s1':s1,'s2':s2,'correlation':c1,'test_null_hypothesis':test_null_hypothesis}
            list_of_dicts_result.append(dict_a)
            print '   **** Yes, we can reject null hypothesis'
        else:
            print '   No accept null hypothesis'

        
        #print 'cadf[1]',cadf[1]
        #print 'cadf[4][5%]',cadf[4]['5%']

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


    def plot_scatter_series(self, df, ts1, ts2):
        plt.xlabel('%s Price ($)' % ts1)
        plt.ylabel('%s Price ($)' % ts2)
        plt.title('%s and %s Price Scatterplot' % (ts1, ts2))
        plt.scatter(df[ts1], df[ts2])
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
    pairlist = ['AAP','AAPL']
    o = output(pairlist,'2015-01-01','2017-09-30',True)
