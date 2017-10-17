#C:\Batches\GitStuff\$work\correlation_sample.csv
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class find:

    def set_SymbolsList(self,SymbolsList):
        self._SymbolsList = SymbolsList
    def get_SymbolsList(self):
        return self._SymbolsList
    SymbolsList = property(get_SymbolsList, set_SymbolsList)

    def set_PairRunningMaxDiffDictionary(self,PairRunningMaxDiffDictionary):
        self._PairRunningMaxDiffDictionary = PairRunningMaxDiffDictionary
    def get_PairRunningMaxDiffDictionary(self):
        return self._PairRunningMaxDiffDictionary
    PairRunningMaxDiffDictionary = property(get_PairRunningMaxDiffDictionary, set_PairRunningMaxDiffDictionary)

    def set_PairRunningMinDiffDictionary(self,PairRunningMinDiffDictionary):
        self._PairRunningMinDiffDictionary = PairRunningMinDiffDictionary
    def get_PairRunningMinDiffDictionary(self):
        return self._PairRunningMinDiffDictionary
    PairRunningMinDiffDictionary = property(get_PairRunningMinDiffDictionary, set_PairRunningMinDiffDictionary)
    
#dict_pairdiff_betweenmaxmin    
    def set_PairBetweenMaxMinDiffDictionary(self,PairBetweenMaxMinDiffDictionary):
        self._PairBetweenMaxMinDiffDictionary = PairBetweenMaxMinDiffDictionary
    def get_PairBetweenMaxMinDiffDictionary(self):
        return self._PairBetweenMaxMinDiffDictionary
    PairBetweenMaxMinDiffDictionary = property(get_PairBetweenMaxMinDiffDictionary, set_PairBetweenMaxMinDiffDictionary)
 
    def set_PairRunningPctDiffDictionary(self,PairRunningPctDiffDictionary):
        self._PairRunningPctDiffDictionary = PairRunningPctDiffDictionary
    def get_PairRunningPctDiffDictionary(self):
        return self._PairRunningPctDiffDictionary
    PairRunningPctDiffDictionary = property(get_PairRunningPctDiffDictionary, set_PairRunningPctDiffDictionary)
 

    #PairPricesDiffDictionary
    def set_PairPricesDiffDictionary(self,PairPricesDiffDictionary):
        self._PairPricesDiffDictionary = PairPricesDiffDictionary
    def get_PairPricesDiffDictionary(self):
        return self._PairPricesDiffDictionary
    PairPricesDiffDictionary = property(get_PairPricesDiffDictionary, set_PairPricesDiffDictionary)
    
    def set_ClosePricesDataframe(self,ClosePricesDataframe):
        self._ClosePricesDataframe = ClosePricesDataframe
    def get_ClosePricesDataframe(self):
        return self._ClosePricesDataframe
    ClosePricesDataframe = property(get_ClosePricesDataframe, set_ClosePricesDataframe)
    
    def set_PairDollarizedDiffDictionary(self,PairDollarizedDiffDictionary):
        self._PairDollarizedDiffDictionary = PairDollarizedDiffDictionary
    def get_PairDollarizedDiffDictionary(self):
        return self._PairDollarizedDiffDictionary
    PairDollarizedDiffDictionary = property(get_PairDollarizedDiffDictionary, set_PairDollarizedDiffDictionary)

    def set_PairMovingAverageDiffDictionary(self,PairMovingAverageDiffDictionary):
        self._PairMovingAverageDiffDictionary = PairMovingAverageDiffDictionary
    def get_PairMovingAverageDiffDictionary(self):
        return self._PairMovingAverageDiffDictionary
    PairMovingAverageDiffDictionary = property(get_PairMovingAverageDiffDictionary, set_PairMovingAverageDiffDictionary)

    def set_PairMovingStdevDiffDictionary(self,PairMovingStdevDiffDictionary):
        self._PairMovingStdevDiffDictionary = PairMovingStdevDiffDictionary
    def get_PairMovingStdevDiffDictionary(self):
        return self._PairMovingStdevDiffDictionary
    PairMovingStdevDiffDictionary = property(get_PairMovingStdevDiffDictionary, set_PairMovingStdevDiffDictionary)
    
    def __init__(self                 
                 , closepricesfilepath = []
                 ,list_of_tickers=[]
                 ):

        #pairlist = ['CA','CHD']
        b = self.setclassdictionaries(closepricesfilepath = closepricesfilepath,list_of_tickers=list_of_tickers)
        #self.regressiondifferences(pairlist=pairlist)
        #dict1 = self.calculateslopeandbetahr(closepricesfilepath)
        print 'setclassdictionaries',b
        
    def calculateslopeandbetahr(self,
                    ):
        print 'started calculateslopeandbetahr'
        df = self.ClosePricesDataframe
        
        from datetime import datetime

        list_of_dict_of_slopes = []
        list_of_dict_of_betahr = []
        #dict_of_dfs ={}
        columns = self.SymbolsList
        i2 = 0
        df_slope = pd.DataFrame(index = self.SymbolsList)
        df_betahr = pd.DataFrame(index = self.SymbolsList)
        for column in columns:
            print 'calculateslopeandbetahr',column
            s1 = column
            #df_diff = df[columns].sub(df[column], axis=0)
            
            df_pp = pd.DataFrame(index = df.index)
            if not s1 in self.PairPricesDiffDictionary:
                print s1,'not found'
            else:
                df_pp = self.PairPricesDiffDictionary[s1]
                #print 'got here 1'
                df_pp.reset_index(level=0, inplace=True)
                #print 'got here 2'
                df_pp['Date'] = pd.to_datetime(df_pp['Date'])
                startdate = df_pp['Date'][0]
                df_pp['days_since'] = (df_pp['Date']- pd.to_datetime(startdate) ).astype('timedelta64[D]')
                #print df_pp
                #stop
                list_of_dict_of_slopes = []
                list_of_dict_of_betahr = []

                for s2 in self.SymbolsList:
                    res = smf.ols( s2 + ' ~ days_since', data=df_pp[['days_since',s2]] ).fit().params
                    dict_of_slopes = {'ticker':s2,s1:res['days_since']}
                    list_of_dict_of_slopes.append(dict_of_slopes)
                    
                    Y=df[s2].tolist()
                    X=df[s1].tolist()
                    results = sm.OLS(Y, X).fit()
                    betahr_value = results.params
                    betahr_value = float(betahr_value[0])
                    dict_of_betahr = {'ticker':s2,s1:betahr_value} 
                    list_of_dict_of_betahr.append(dict_of_betahr)
                
                df_slope_x = pd.DataFrame(list_of_dict_of_slopes)
                df_slope_x.set_index("ticker", drop=True, inplace=True)
                df_slope[column] = df_slope_x

                df_betahr_x = pd.DataFrame(list_of_dict_of_betahr)
                df_betahr_x.set_index("ticker", drop=True, inplace=True)
                df_betahr[column] = df_betahr_x

        
        return {'df_slope':df_slope,'df_betahr':df_betahr}
        #return dict_of_dfs
                

##    def regressiondifferences(self,ticker1,ticker2):
##        
##        ser = self.PairPricesDiffDictionary[ticker1][ticker2]
##        #plt.plot(ser)
##        #plt.ylabel('some numbers')
##        #plt.show()
##
##        df = ser.to_frame('diff')
##        df.reset_index(level=0, inplace=True)
##        #print df
##        #print smf.ols( 'diff ~ Date', data=df ).fit().params
##        #stop
##        
##        startdate = df['Date'][0]
##        
##        df['Date'] = pd.to_datetime(df['Date'])
##        df['days_since'] = (df['Date']- pd.to_datetime(startdate) ).astype('timedelta64[D]')
##        #print df
##        
##        res = smf.ols( 'diff ~ days_since', data=df ).fit().params
##        return {'slope':res['days_since'],'intercept':res['Intercept']}
##        
##
####        x = df['days_since']
####        y = df['diff']
####        fig, ax = plt.subplots()
####        fit = np.polyfit(x, y, deg=1)
####        ax.plot(x, fit[0] * x + fit[1], color='red')
####        ax.scatter(x, y)
####        fig.show()

        
        #stop
        #print self.ClosePricesDataframe
        #self.test_stationarity(self.PairPricesDiffDictionary[ticker1][ticker2])


    def test_stationarity(self,timeseries):
        
        #Determing rolling statistics
        rolmean = pd.rolling_mean(timeseries, window=12)
        rolstd = pd.rolling_std(timeseries, window=12)

        #Plot rolling statistics:
        orig = plt.plot(timeseries, color='blue',label='Original')
        mean = plt.plot(rolmean, color='red', label='Rolling Mean')
        std = plt.plot(rolstd, color='black', label = 'Rolling Std')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show(block=False)
        
        #Perform Dickey-Fuller test:
        print 'Results of Dickey-Fuller Test:'
        dftest = adfuller(timeseries, autolag='AIC')
        dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
        for key,value in dftest[4].items():
            dfoutput['Critical Value (%s)'%key] = value
        print dfoutput

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
        

    def setclassdictionaries(self,closepricesfilepath,list_of_tickers = []):
        
        print 'started def setclassdictionaries'
        #import pandas as pd
        myfile = closepricesfilepath #'C:\Batches\GitStuff\$work\closeprices_sample.csv'
        df = pd.read_csv(myfile)
        print df
        df.set_index("Date", drop=True, inplace=True)
        self.ClosePricesDataframe = df
        if len(list_of_tickers) == 0:
            columns = list(df.columns.values)
        else:
            columns = list_of_tickers
        self.SymbolsList = columns
        print 'self.SymbolsList = columns', self.SymbolsList
        #stop
##        #columns = ['CA',     'CHD']
##        df_openshares = 10000.0 / df.iloc[[0]]
##        #print df_openshares
##        #stop
##        df_shares2 = df_openshares.append([df_openshares]*(len(df)-1),ignore_index=True)
##        df_shares3 = pd.concat([df2, df_shares2], axis=1)
##        df_shares3.set_index("Date", drop=True, inplace=True)
##
##        df_dollarized = df.multiply(df_shares3, axis=1)
##        dict_pairdiff_runningmax = {}
##        dict_pairdiff_runningmin = {}
##        dict_pairdiff_betweenmaxmin = {}
##        dict_pairdiff_runningpct = {}
        dict_pairdiff_prices = {}
##        dict_pairdiff_dollarized = {}
##        dict_pairdiff_movingaverage = {}
##        dict_pairdiff_standarddeviation = {}
##        
##        
##        print 'started creating class dictionaries...'
##        
        i2 = 0
        for column in columns:
##            df_diff_runningmax = pd.DataFrame(index = df.index)
##            df_diff_runningmin = pd.DataFrame(index = df.index)
##            df_diff_movingaverage = pd.DataFrame(index = df.index)
##            df_diff_stdev = pd.DataFrame(index = df.index)
##            
            print 'setclassdictionaries',column
##            df_diff = df[columns].sub(df[column], axis=0)
##            i3 = 0
##            for column1 in columns:
##                df_diff1 = df_diff[column1].to_frame(column1)
##                df_diff_runningmax[column1] = df_diff1[column1].cummax().to_frame(column1)
##                df_diff_runningmin[column1] = df_diff1[column1].cummin().to_frame(column1)
##                df_diff_movingaverage[column1] = df_diff1.rolling(window=movingaveragewindow).mean()
##                df_diff_stdev[column1] = df_diff1.rolling(window=movingaveragewindow).std()
##                i3 += 1
            #print 'got here 1'
            df_diff_prices = df[columns].sub(df[column], axis=0)
            #print 'got here 2'
##            df_diff_betweenmaxmin = df_diff_runningmax[columns].sub(df_diff_runningmin[columns], axis=0)
##            df_diff_runningpct = ( df_diff_prices - df_diff_runningmin ) / ( df_diff_runningmax - df_diff_runningmin)             
##            
##            df_diff_dollarized = df_dollarized[columns].sub(df_dollarized[column], axis=0)
##
            dict_pairdiff_prices[column] = df_diff_prices
##            
##            dict_pairdiff_runningmax[column] = df_diff_runningmax
##            dict_pairdiff_runningmin[column] = df_diff_runningmin
##            dict_pairdiff_betweenmaxmin[column] = df_diff_betweenmaxmin
##            dict_pairdiff_runningpct[column] = df_diff_runningpct
##            dict_pairdiff_dollarized[column] = df_diff_dollarized
##            dict_pairdiff_movingaverage[column] = df_diff_movingaverage
##            dict_pairdiff_standarddeviation[column] = df_diff_stdev
            i2 +=1
            #if i2 >= 6:
            #    break
##        print 'finished creating class dictionaries...'
        self.PairPricesDiffDictionary = dict_pairdiff_prices
        cachedfilepathname_ppdd_pcln = 'C:\\Batches\\GitStuff\\$work\\ppdd_pcln.csv'
        self.PairPricesDiffDictionary['PCLN'].to_csv(cachedfilepathname_ppdd_pcln,columns=(list(self.PairPricesDiffDictionary['PCLN'].columns.values)))

        cachedfilepathname_ppdd_acn = 'C:\\Batches\\GitStuff\\$work\\ppdd_acn.csv'
        self.PairPricesDiffDictionary['ACN'].to_csv(cachedfilepathname_ppdd_acn,columns=(list(self.PairPricesDiffDictionary['ACN'].columns.values)))
        STOP
##        self.PairRunningMaxDiffDictionary = dict_pairdiff_runningmax
##        self.PairRunningMinDiffDictionary = dict_pairdiff_runningmin
##        self.PairBetweenMaxMinDiffDictionary = dict_pairdiff_betweenmaxmin
##        self.PairRunningPctDiffDictionary = dict_pairdiff_runningpct
##        self.PairDollarizedDiffDictionary = dict_pairdiff_dollarized
##        self.PairMovingAverageDiffDictionary = dict_pairdiff_movingaverage
##        self.PairMovingStdevDiffDictionary = dict_pairdiff_standarddeviation
        print 'finished def setclassdictionaries'
        

        return True
if __name__=='__main__':

    symbols_and_signs_list = [
    ['AAL','S'],
    ['ADM','S'],
    ['AES','L'],
    ['AGN','S'],
    ['ALKS','S'],
    ['AMAT','L'],
    ['AMD','S'],
    ['AMGN','L'],
    ['APD','L'],
    ['ARNC','S'],
    ['AVT','S'],
    ['AXP','L'],
    ['AXS','S'],
    ['BAC','L'],
    ['BC','S'],
    ['BEN','L'],
    ['CA','L'],
    ['CAH','S'],
    ['CASY','S'],
    ['CELG','L'],
    ['CL','L'],
    ['CMCSA','S'],
    ['COLM','S'],
    ['CRI','S'],
    ['CSCO','L'],
    ['CVS','L'],
    ['CVX','L'],
    ['CXO','S'],
    ['DIS','S'],
    ['DISH','S'],
    ['EGN','S'],
    ['ETR','L'],
    ['F','S'],
    ['FCNCA','S'],
    ['FLS','S'],
    ['FSLR','S'],
    ['FTI','S'],
    ['GE','S'],
    ['GPC','S'],
    ['GPS','L'],
    ['GRMN','L'],
    ['GWR','S'],
    ['GWW','S'],
    ['HAIN','S'],
    ['HAS','S'],
    ['HD','L'],
    ['HHC','S'],
    ['HOG','S'],
    ['HPE','S'],
    ['HRL','S'],
    ['INTC','L'],
    ['JLL','S'],
    ['JNJ','L'],
    ['JWN','L'],
    ['KHC','S'],
    ['KMB','L'],
    ['KMI','S'],
    ['KSS','L'],
    ['LAZ','L'],
    ['LEG','S'],
    ['LLY','L'],
    ['LMT','L'],
    ['LNG','S'],
    ['LOW','L'],
    ['LPX','L'],
    ['LUK','S'],
    ['LVLT','S'],
    ['LYB','L'],
    ['M','L'],
    ['MAS','L'],
    ['MD','S'],
    ['MDLZ','S'],
    ['MDT','S'],
    ['MLM','S'],
    ['MMM','L'],
    ['MO','L'],
    ['MS','L'],
    ['MUR','S'],
    ['NFX','S'],
    ['NKE','S'],
    ['NUAN','S'],
    ['NWL','S'],
    ['NWS','S'],
    ['OTEX','S'],
    ['PAG','S'],
    ['PCLN','L'],
    ['PDCO','S'],
    ['PEP','L'],
    ['PM','L'],
    ['QCOM','S'],
    ['RPM','S'],
    ['RTN','L'],
    ['S','S'],
    ['SEE','S'],
    ['SJM','S'],
    ['SKX','S'],
    ['SLB','S'],
    ['SNA','S'],
    ['SON','S'],
    ['STX','L'],
    ['SWKS','L'],
    ['T','L'],
    ['TAP','S'],
    ['TGT','L'],
    ['TRIP','S'],
    ['TWTR','S'],
    ['UAL','S'],
    ['UHS','S'],
    ['UNP','L'],
    ['VIA','S'],
    ['VMC','S'],
    ['VRSK','S'],
    ['VSAT','S'],
    ['WAB','S'],
    ['WHR','S'],
    ['WPX','S'],
    ['WTM','S'],
    ['XOM','S'],
    ['XRAY','S'],
    ['Y','S']
    ]
    
    list_of_tickers = []
    for x1 in symbols_and_signs_list:
        list_of_tickers.append(x1[0])
    print list_of_tickers
    
    #list_of_tickers = [ 'AAL','AAPL','ABBV','CA','CHD','GOOG','GOOGL','MSFT','AMZN' ]


    
    o = find(closepricesfilepath = 'C:\\Batches\\GitStuff\\$work\\closeprices_sample.csv', list_of_tickers=[])#list_of_tickers)
    d2 = o.calculateslopeandbetahr()
    print '----------------'
    print 'df_slope'
    print d2['df_slope'].round(3)
    print '----------------'
    print 'df_betahr'
    print d2['df_betahr'].round(3)

    cachedfilepathname_slope = 'C:\\Batches\\GitStuff\\$work\\slopes.csv'
    d2['df_slope'].to_csv(cachedfilepathname_slope,columns=(list(d2['df_slope'].columns.values)))

    cachedfilepathname_betahr = 'C:\\Batches\\GitStuff\\$work\\betahr.csv'
    d2['df_betahr'].to_csv(cachedfilepathname_betahr,columns=(list(d2['df_betahr'].columns.values)))


