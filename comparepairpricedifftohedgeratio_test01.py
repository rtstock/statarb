#C:\Batches\GitStuff\$work\correlation_sample.csv
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import adfuller
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import analyzerunningcadfonpair as ana
class find:

    def set_SymbolsList(self,SymbolsList):
        self._SymbolsList = SymbolsList
    def get_SymbolsList(self):
        return self._SymbolsList
    SymbolsList = property(get_SymbolsList, set_SymbolsList)

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

    #PairPricesHedgeRatioDictionary
    def set_PairPricesHedgeRatioDictionary(self,PairPricesHedgeRatioDictionary):
        self._PairPricesHedgeRatioDictionary = PairPricesHedgeRatioDictionary
    def get_PairPricesHedgeRatioDictionary(self):
        return self._PairPricesHedgeRatioDictionary
    PairPricesHedgeRatioDictionary = property(get_PairPricesHedgeRatioDictionary, set_PairPricesHedgeRatioDictionary)
    
    def __init__(self                 
                 , list_of_tickers=[]
                 , closepricesfilepath = ''
                 , fromdate = '2017-01-01'
                 , todate = '2017-12-31'
                 ):

        #pairlist = ['CA','CHD']
        b = self.setclassdictionaries(list_of_tickers=list_of_tickers,closepricesfilepath = closepricesfilepath,fromdate=fromdate,todate=todate)

        print 'setclassdictionaries',b
    
    def testone(self,ticker1,ticker2,tradedate,triggervalue, maxgain=1000.0):
        print ticker1,ticker2,tradedate,triggervalue
        df_closeprices = self.ClosePricesDataframe
        print df_closeprices[[ticker1]][(df_closeprices.index == tradedate)][ticker1][0]
        #stop
        df_closeprices = df_closeprices[(df_closeprices.index >= tradedate)]
        #df_diffprices = self.PairPricesDiffDictionary[ticker1][ticker2]
        df2 = pd.DataFrame(index=df_closeprices.index.copy())
        print '----------------- ++++'
        df_closeprices = df_closeprices[[ticker1,ticker2]]
        #print df
        opendiffprice = self.PairPricesDiffDictionary[ticker1][ticker2][tradedate]
        print 'opendiffprice','xxx',opendiffprice
        
        columns = list(df_closeprices.columns.values)
        print 'columns',columns
        df_openprices= df_closeprices.iloc[[0]]
        print 'df_openprices', df_openprices
        df_openshares = 10000.0 / df_closeprices.iloc[[0]]
        print 'df_openshares',df_openshares
        print '--------------------------kkkk'
        #df_opendiffprice = df_diffprices.iloc[[0]][0]
        #print 'df_opendiffprice',df_opendiffprice
        
        df_blotter = df_closeprices * df_openshares.loc[tradedate]
        if triggervalue < 0.5:
            sign_for_ticker1 = -1
            sign_for_ticker2 = 1
        else:
            sign_for_ticker1 = 1
            sign_for_ticker2 = -1
            
        list_of_my_dicts = []
        for idx,row in df_blotter.iterrows():
            #print 'a', idx, sign_for_ticker1 * row[ticker1], sign_for_ticker2 * row[ticker2], ( sign_for_ticker1 * row[ticker1] ) + ( sign_for_ticker2 * row[ticker2] ), triggervalue, self.PairPricesDiffDictionary[ticker1][ticker2][idx]
            my_dict = {
                      'date':idx
                    , '01_dollarized1':sign_for_ticker1 * row[ticker1]
                    , '01_dollarized2':sign_for_ticker2 * row[ticker2]
                    , '02_pl':( sign_for_ticker1 * row[ticker1] ) + ( sign_for_ticker2 * row[ticker2] )
                    , '03_triggervalue':triggervalue
                    , '04_opendiffprice':opendiffprice
                    , '05_currentpricediff':self.PairPricesDiffDictionary[ticker1][ticker2][idx]
                    ##, '05_maxpricediff':self.PairRunningMaxDiffDictionary[ticker1][ticker2][idx]
                    ##, '05_minpricediff':self.PairRunningMinDiffDictionary[ticker1][ticker2][idx]
                    , '06_ticker1':ticker1
                    , '06_ticker2':ticker2
                    , '07_openshares_ticker1':df_openshares.iloc[0][ticker1]
                    , '07_openshares_ticker2':df_openshares.iloc[0][ticker2]
                    , '08_openprice_ticker1':df_openprices.iloc[0][ticker1]
                    , '08_openprice_ticker2':df_openprices.iloc[0][ticker2]
                    , '09_currentprice_ticker1':self.ClosePricesDataframe[[ticker1]][(self.ClosePricesDataframe.index == idx)][ticker1][0]
                    , '09_currentprice_ticker2':self.ClosePricesDataframe[[ticker2]][(self.ClosePricesDataframe.index == idx)][ticker2][0]
                    , '10_opentradedate':tradedate
                    , '11_currenttradedate':idx
                    }
            list_of_my_dicts.append(my_dict)
        df_status = pd.DataFrame(list_of_my_dicts)
        df_status.set_index("date", drop=True, inplace=True)
        #print df_status.round(2)
        #stop
        #print '-------------------------------------------------'
        df_entrytrade = df_status.iloc[:1]
        #print df_entrytrade.iloc[0]
                    
                        #if idx > '2016-03-02':
                        #        break
        #print '-------------------------------------------------'
        df_exittrade = df_status[(df_status['02_pl'] >= maxgain)].iloc[:1]
        return df_status



    def setclassdictionaries(self,list_of_tickers = [],closepricesfilepath = '',fromdate = '2017-01-01',todate = '2017-12-31'):
        ana_class = ana.analyze()
        print 'started def setclassdictionaries'
        #import pandas as pd
        if len(closepricesfilepath) == 0:
            print 'go to pull prices'
            import pullprices as pp
            o = pp.pull()
            o.setclassdataframes(symbols=list_of_tickers,fromdate = fromdate,todate = todate)
            df = o.ClosePricesDataframe
        else:
            myfile = closepricesfilepath #'C:\Batches\GitStuff\$work\closeprices_sample.csv'
            df = pd.read_csv(myfile)
            df.set_index("Date", drop=True, inplace=True)
            
        if len(list_of_tickers) == 0:
            columns = list(df.columns.values)
        else:
            columns = list_of_tickers
        df = df[columns]
        
        
        self.ClosePricesDataframe = df
        self.SymbolsList = columns
        print 'self.SymbolsList = columns', self.SymbolsList
        dict_pairdiff_prices = {}
        dict_pairhr_prices = {}
        i2 = 0
        for s1 in columns:
            print 'setclassdictionaries',s1
            df_diff_prices = df[columns].sub(df[s1], axis=0)
            dict_pairdiff_prices[s1] = df_diff_prices
            i3 = 0
            for s2 in columns:
                if not s1 == s2:
                    df_hr_prices = df[columns].div(df[s1], axis=0)
                    dict_pairhr_prices[s1] = df_hr_prices
                    i2 +=1
                    #stop
            i2 +=1
        self.PairPricesDiffDictionary = dict_pairdiff_prices
        self.PairPricesHedgeRatioDictionary = dict_pairhr_prices
        
        
        print 'finished def setclassdictionaries'
        

        return True

    def dollarizedataframe(self,mydataframe,parvalue = 10000.0):
        df = mydataframe
        list_of_dates = list(df.index)
        list_of_dates_sorted = sorted(list_of_dates)
        df2 = pd.DataFrame({'Date':list_of_dates_sorted})
        df_openshares = parvalue / df.iloc[[0]]
        df_shares2 = df_openshares.append([df_openshares]*(len(df)-1),ignore_index=True)
        df_shares3 = pd.concat([df2, df_shares2], axis=1)
        df_shares3.set_index("Date", drop=True, inplace=True)
        df_dollarized = df.multiply(df_shares3, axis=1)
        return df_dollarized 


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
    
    #list_of_tickers = [ 'AAPL','PCLN','MSFT','GOOG']
    #list_of_tickers = [ 'LUV','AAL','DAL','UAL']
    list_of_tickers = [ 'MS','BAC','C','JPM']
    #list_of_tickers = [ 'PCLN','MSFT']
    
    o = find(list_of_tickers=list_of_tickers,closepricesfilepath = '', fromdate='2014-01-01',todate='2017-12-31')
    #o = find(list_of_tickers=list_of_tickers,closepricesfilepath = 'C:\\Batches\\GitStuff\\$work\\closeprices_sample.csv')    
    #b = o.setadvancedclassvariables()
##    print '----------------'
##    print 'AAPL PairPricesDiffDictionary'
##    print o.PairPricesDiffDictionary['AAPL']
##    print '---------------------------------------------'
##    print 'AAPL PairPricesHedgeRatioDictionary'
##    print o.PairPricesHedgeRatioDictionary['AAPL']
    
    df_analyze1 = pd.DataFrame(index=o.ClosePricesDataframe.index.copy())
    for s1 in list_of_tickers:
        print '---'
        #print s1
        #df = o.PairPricesDiffDictionary[s1]
        df = o.PairPricesHedgeRatioDictionary[s1]
        #print s1,df.round(3)
        df_dollarized = o.dollarizedataframe(df,10000.0)
        df_dollarized['sum'] = df_dollarized.sum(axis=1)
        df_analyze1[s1] = df_dollarized['sum']
        #print s1, df_dollarized.round(0)
        #stop
        #for idx, row in df.iterrows():
    print df_analyze1
    list_of_signs = [
                     ('a',[ 1, 1,-1,-1])
                    ,('b',[-1, 1, 1,-1])
                    ,('c',[-1,-1, 1, 1])
                    ,('d',[ 1,-1,-1, 1])
                    ,('e',[-1, 1,-1, 1])
                    ,('f',[ 1,-1, 1,-1])
                     ]
    df_analyze2 = pd.DataFrame(index=df_analyze1.index.copy())
    for a in list_of_signs:
        listid = a[0]
        listx = a[1]
        print list_of_tickers
        print listx
        #stop
        #df_a = pd.DataFrame(np.array(listx), columns = list_of_tickers)
        df_a = pd.DataFrame([listx],columns = list_of_tickers,index=df_analyze1.index.copy())
        #print df_a
        #stop
        #print 'got here 1'
        df_b = pd.DataFrame(df_analyze1.values*df_a.values, columns=df_analyze1.columns, index=df_analyze1.index)
        #print 'got here 2'
        df_b['sum'] = df_b.sum(axis=1)
        #print 'got here 3'
        df_analyze2[a[0]] = df_b['sum']
        #print 'got here 4'
        #print a, df_b
    print df_analyze2
    df_analyze2max = df_analyze2.cummax()
    print df_analyze2max
    df_analyze2min = df_analyze2.cummin()
    print df_analyze2min
    i0 = 0
    
    for a in list_of_signs:
        label = a[0] + ': ' + str(a[1][0]) + list_of_tickers[0] +', ' + str(a[1][1])+ list_of_tickers[1] +', ' + str(a[1][2])+ list_of_tickers[2] +', ' + str(a[1][3])+ list_of_tickers[3] 
        listid = a[0]
        plt.plot(df_analyze2.index, df_analyze2[listid], label=label)
        i0+=1
    plt.legend()
    plt.show()
    #df_analyze2.plot()
    #plt.show()
    #df_status = o.testone(ticker1='AMZN',ticker2='PCLN',tradedate='2017-09-28',triggervalue=0, maxgain=500.0)
    #print df_status
    #stop
    

