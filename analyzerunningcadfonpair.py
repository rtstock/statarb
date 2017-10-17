
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
    
    def set_PairAnalysisDataframe(self,PairAnalysisDataframe):
        self._PairAnalysisDataframe = PairAnalysisDataframe
    def get_PairAnalysisDataframe(self):
        return self._PairAnalysisDataframe
    PairAnalysisDataframe = property(get_PairAnalysisDataframe, set_PairAnalysisDataframe)

    
    def __init__(self,
                ):
        print 'initialized analyzecadfonpair'
        
    def analyzepair(self,pairlist,fromdate,todate,showplot
                    ):

        s1 = pairlist[0]
        s2 = pairlist[1]
        print '---------------------'
        print 'Doing',s1, s2
    
        #fromdatetime = datetime.datetime(2015, 1, 1)
        #todatetime = datetime.datetime(2017, 9, 30)
        fromdatetime = datetime.datetime.strptime(fromdate,"%Y-%m-%d")
        todatetime = datetime.datetime.strptime(todate,"%Y-%m-%d")
        #print fromdatetime
        #print todatetime
        #stop
        prices1 = data.DataReader(s1, "yahoo", fromdatetime, todatetime)
        prices2 = data.DataReader(s2, "yahoo", fromdatetime, todatetime)

        df_a = pd.DataFrame(index=prices1.index)
        df_a[s1] = prices1["Close"]
        df_a[s2] = prices2["Close"]
        df = df_a.dropna(axis=0, how='any')
        #print df
        if showplot == True:
            # Plot the two time series
            self.plot_price_series(df, s1, s2,fromdatetime,todatetime)

            # Display a scatter plot of the two time series
            self.plot_scatter_series(df, s1, s2)
        
        
        Y=df[s2].tolist()
        X=df[s1].tolist()
        
        i0 = 0
        beta_hr_list = []
        
        for idx, rows in df.iterrows():            
            #print idx
            if i0 >= 0:
                res = sm.OLS(Y[:i0+1],X[:i0+1])
                beta_hr = res.fit().params[0]
                mydict = {'Date':idx,'beta_hr':beta_hr,'actual':Y[i0]/X[i0]}
                beta_hr_list.append(mydict)
            i0 += 1
            #if i0 >= 10:
            #    stop
        df_beta_hr = pd.DataFrame(beta_hr_list)
        df_beta_hr.set_index("Date", drop=True, inplace=True)
        df_b =  pd.concat([df_a, df_beta_hr], axis=1)
        
        df_b['a-b'] = df_b['actual']- df_b['beta_hr']
        df_b["res"] = df_b[s2] - df_b['beta_hr']*df_b[s1]

##        for idx, row in df_b.iterrows():
##            print idx,row['beta_hr'],round(row['a-b'],4)                

        # Calculate and analyze the CADF test on the residuals
        cadf = ts.adfuller(df_b["res"])
        test_null_hypothesis = cadf[0]
        five_percent_value = cadf[4]['5%']
        print ''
        print 'cadf test for cointegration result 5% value:',test_null_hypothesis, 'must be less than',five_percent_value
        self.PairAnalysisDataframe = df_b
        return df_b
##        mylist = [s1,s2,test_null_hypothesis]
##        with open(myfileanalyze, 'a') as myfile:
##            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
##            wr.writerow(mylist)
##
##        if float(test_null_hypothesis) < float(five_percent_value):
##
##            dict_a = {'s1':s1,'s2':s2,'correlation':c1,'test_null_hypothesis':test_null_hypothesis}
##            list_of_dicts_result.append(dict_a)
##            print '   **** Yes, we can reject null hypothesis'
##        else:
##            print '   No accept null hypothesis'

        
        #print 'cadf[1]',cadf[1]
        #print 'cadf[4][5%]',cadf[4]['5%']

    def plot_price_series(self, df, ts1, ts2,fromdate,todate):
        months = mdates.MonthLocator()  # every month
        fig, ax = plt.subplots()
        ax.plot(df.index, df[ts1], label=ts1)
        ax.plot(df.index, df[ts2], label=ts2)
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.set_xlim(fromdate,todate)
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

    def plot_residuals(self, df,fromdate,todate):
        months = mdates.MonthLocator()  # every month
        fig, ax = plt.subplots()
        ax.plot(df.index, df["res"], label="Residuals")
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.set_xlim(fromdate, todate)
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
    pairlist = ['BAC', 'MS']
    #pairlist = ['MSFT','PCLN']
    o = analyze()
    #pairlist,fromdate, todate, showplot = True
    df = o.analyzepair(pairlist = pairlist,fromdate='2015-09-30', todate='2017-10-11',showplot=False)
    print df

    myinput = raw_input("What do you want to do? type 'y' to show graph, enter to skip graph and continue...")
    if myinput == 'y':
            #print ticker1,ticker2
            
            
            #df_0 = self.PairPricesDiffDictionary[ticker1][ticker2].to_frame('diff')
            #df_1 = self.PairMovingAverageDiffDictionary[ticker1][ticker2].to_frame('ma')
            df_0 = pd.concat([
                    o.PairAnalysisDataframe['actual'].to_frame('actual')
                    , o.PairAnalysisDataframe['beta_hr'].to_frame('beta_hr')
                    ], axis=1)
            df_0.plot.line(title=pairlist[0] + ' ' + pairlist[1])
            #df_ma.plot.line(title=ticker1 + ' ' + ticker2)
            
            #plt.plot(label='Sample Label Red')
            plt.show()
            #for idx,row in df_prices.iterrows():
            #    print idx,row['diff']
            raw_input("Press Enter to continue...")
