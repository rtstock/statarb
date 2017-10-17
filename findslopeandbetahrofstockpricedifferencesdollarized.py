#C:\Batches\GitStuff\$work\correlation_sample.csv
import pandas as pd
import numpy as np
from scipy import stats
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

##    def set_PairRunningMaxDiffDictionary(self,PairRunningMaxDiffDictionary):
##        self._PairRunningMaxDiffDictionary = PairRunningMaxDiffDictionary
##    def get_PairRunningMaxDiffDictionary(self):
##        return self._PairRunningMaxDiffDictionary
##    PairRunningMaxDiffDictionary = property(get_PairRunningMaxDiffDictionary, set_PairRunningMaxDiffDictionary)
##
##    def set_PairRunningMinDiffDictionary(self,PairRunningMinDiffDictionary):
##        self._PairRunningMinDiffDictionary = PairRunningMinDiffDictionary
##    def get_PairRunningMinDiffDictionary(self):
##        return self._PairRunningMinDiffDictionary
##    PairRunningMinDiffDictionary = property(get_PairRunningMinDiffDictionary, set_PairRunningMinDiffDictionary)
    
###dict_pairdiff_betweenmaxmin    
##    def set_PairBetweenMaxMinDiffDictionary(self,PairBetweenMaxMinDiffDictionary):
##        self._PairBetweenMaxMinDiffDictionary = PairBetweenMaxMinDiffDictionary
##    def get_PairBetweenMaxMinDiffDictionary(self):
##        return self._PairBetweenMaxMinDiffDictionary
##    PairBetweenMaxMinDiffDictionary = property(get_PairBetweenMaxMinDiffDictionary, set_PairBetweenMaxMinDiffDictionary)
## 
##    def set_PairRunningPctDiffDictionary(self,PairRunningPctDiffDictionary):
##        self._PairRunningPctDiffDictionary = PairRunningPctDiffDictionary
##    def get_PairRunningPctDiffDictionary(self):
##        return self._PairRunningPctDiffDictionary
##    PairRunningPctDiffDictionary = property(get_PairRunningPctDiffDictionary, set_PairRunningPctDiffDictionary)
 

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

    def set_SlopeOfDiffsDataframe(self,SlopeOfDiffsDataframe):
        self._SlopeOfDiffsDataframe = SlopeOfDiffsDataframe
    def get_SlopeOfDiffsDataframe(self):
        return self._SlopeOfDiffsDataframe
    SlopeOfDiffsDataframe = property(get_SlopeOfDiffsDataframe, set_SlopeOfDiffsDataframe)

    def set_BetaHedgeRatioDataframe(self,BetaHedgeRatioDataframe):
        self._BetaHedgeRatioDataframe = BetaHedgeRatioDataframe
    def get_BetaHedgeRatioDataframe(self):
        return self._BetaHedgeRatioDataframe
    BetaHedgeRatioDataframe = property(get_BetaHedgeRatioDataframe, set_BetaHedgeRatioDataframe)
    
    def set_PairDollarizedDiffDictionary(self,PairDollarizedDiffDictionary):
        self._PairDollarizedDiffDictionary = PairDollarizedDiffDictionary
    def get_PairDollarizedDiffDictionary(self):
        return self._PairDollarizedDiffDictionary
    PairDollarizedDiffDictionary = property(get_PairDollarizedDiffDictionary, set_PairDollarizedDiffDictionary)

#PairDollarizedHedgeRatioDictionary
    def set_PairDollarizedHedgeRatioDictionary(self,PairDollarizedHedgeRatioDictionary):
        self._PairDollarizedHedgeRatioDictionary = PairDollarizedHedgeRatioDictionary
    def get_PairDollarizedHedgeRatioDictionary(self):
        return self._PairDollarizedHedgeRatioDictionary
    PairDollarizedHedgeRatioDictionary = property(get_PairDollarizedHedgeRatioDictionary, set_PairDollarizedHedgeRatioDictionary)

#SlopeOfPairsDollarizedDataframe
    def set_SlopeOfPairsDollarizedDataframe(self,SlopeOfPairsDollarizedDataframe):
        self._SlopeOfPairsDollarizedDataframe = SlopeOfPairsDollarizedDataframe
    def get_SlopeOfPairsDollarizedDataframe(self):
        return self._SlopeOfPairsDollarizedDataframe
    SlopeOfPairsDollarizedDataframe = property(get_SlopeOfPairsDollarizedDataframe, set_SlopeOfPairsDollarizedDataframe)

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

#dollarizedhedgeratiodataframes
    def set_PairDollarizedHedgeRatioDiffDictionary(self,PairDollarizedHedgeRatioDiffDictionary):
        self._PairDollarizedHedgeRatioDiffDictionary = PairDollarizedHedgeRatioDiffDictionary
    def get_PairDollarizedHedgeRatioDiffDictionary(self):
        return self._PairDollarizedHedgeRatioDiffDictionary
    PairDollarizedHedgeRatioDiffDictionary = property(get_PairDollarizedHedgeRatioDiffDictionary, set_PairDollarizedHedgeRatioDiffDictionary)
    
    def __init__(self                 
                 , list_of_tickers=[]
                 , closepricesfilepath = ''
                 , fromdate = '2017-01-01'
                 , todate = '2017-12-31'
                 ):

        #pairlist = ['CA','CHD']
        b = self.setclassdictionaries(list_of_tickers=list_of_tickers,closepricesfilepath = closepricesfilepath,fromdate=fromdate,todate=todate)
        b = self.setadvancedclassvariables()
        b = self.setdollarizedhedgeratiodiffdictionary()
        b = self.setslopeofpairsdollarizedtodataframe()
        #self.regressiondifferences(pairlist=pairlist)
        #dict1 = self.setadvancedclassvariables(closepricesfilepath)
        print 'setclassdictionaries',b
    def setdollarizedhedgeratiodiffdictionary(self,
                                            ):
        dict_pairdiff_dollarizedhedgeratiodataframes = {}                                   
        for k,v in self.PairDollarizedHedgeRatioDictionary.items():
            print '||',k,'||'
            df_diff_dollarizedhr = v.sub(self.ClosePricesDataframe, axis=0).round(4)
            dict_pairdiff_dollarizedhedgeratiodataframes[k] = df_diff_dollarizedhr
            
        self.PairDollarizedHedgeRatioDiffDictionary = dict_pairdiff_dollarizedhedgeratiodataframes        
        return True
    
    def setslopeofpairsdollarizedtodataframe(self,
                                        ):
        df = self.ClosePricesDataframe
        #df_dollarized = self.PairDollarizedHedgeRatioDictionary
        #df_dollarized = self.PairDollarizedHedgeRatioDiffDictionary
        df_dollarized = self.PairDollarizedDiffDictionary
        df_slope = pd.DataFrame(index = self.SymbolsList)
        columns = self.SymbolsList
        for s1 in columns:
            df_pp = pd.DataFrame(index = df.index)
            if not s1 in df_dollarized:
                print s1,'not found'
            else:
                print 'Doing',s1
                df_diff = df_dollarized[s1] 

                df_diff.reset_index(level=0, inplace=True)
                df_diff['Date'] = pd.to_datetime(df_diff['Date'])
                startdate = df_diff['Date'][0]
                df_diff['days_since'] = (df_diff['Date']- pd.to_datetime(startdate) ).astype('timedelta64[D]')
                list_of_dict_of_slopes = []
                #for idx,row in df_diff.iterrows():
                #    print row['Date'],row['MSFT']
                
                for s2 in self.SymbolsList:
                    if not s1 == s2:
                        res = smf.ols( s2 + ' ~ days_since', data=df_diff[['days_since',s2]] ).fit().params
                        slope_value = res['days_since']
                        slope, intercept, r_value, p_value, std_err = stats.linregress(df_diff['days_since'],df_diff[s2])
                        print  s1,s2, 'slope_value',slope_value
                        print  s1,s2, 'slope',slope
                        print  s1,s2, 'intercept',intercept
                        print  s1,s2, 'r squared',r_value ** 2
                        print  s1,s2, 'p value', round(p_value,5)
                    
                        dict_of_slopes = {'ticker':s2,s1:slope_value}
                        list_of_dict_of_slopes.append(dict_of_slopes)
                #stop
                df_slope_x = pd.DataFrame(list_of_dict_of_slopes)
                df_slope_x.set_index("ticker", drop=True, inplace=True)
                df_slope[s1] = df_slope_x
        self.SlopeOfPairsDollarizedDataframe = df_slope
        return True


    def setslopeofpairsdollarizedtodataframe_old(self,
                                        ):
        df = self.ClosePricesDataframe
        df_slope = pd.DataFrame(index = self.SymbolsList)
        columns = self.SymbolsList
        for s1 in columns:
            df_pp = pd.DataFrame(index = df.index)
            if not s1 in self.PairDollarizedHedgeRatioDictionary:
                print s1,'not found'
            else:
                print 'Doing',s1
                df_bhr = self.PairDollarizedHedgeRatioDictionary[s1] #these are s1 prices in dollar terms of s2
                #print df_bhr
                #print '-----------------------------------------------------'
                #print '-----------------------------------------------------'
                df_cc = df[columns]
                #print df_cc
                #stop
                #print df_bhr[columns]
                #stop
                #df_diff = df_bhr[columns].sub(df_bhr[s1], axis=0).round(6)
                df_diff = df_bhr.sub(df_cc, axis=0).round(6)
                #print df_diff
                #stop
                df_diff.reset_index(level=0, inplace=True)
                df_diff['Date'] = pd.to_datetime(df_diff['Date'])
                startdate = df_diff['Date'][0]
                df_diff['days_since'] = (df_diff['Date']- pd.to_datetime(startdate) ).astype('timedelta64[D]')
                list_of_dict_of_slopes = []
                for s2 in self.SymbolsList:
                    
##                    if s1 == 'AAPL':
##                        if s2 == 'AMZN':
##                            print s1,'vs.',s2,'A1******************'
##                            print self.PairDollarizedHedgeRatioDictionary['AAPL']
##                            print s1,'vs.',s2,'A2******************'
##                            print self.PairDollarizedHedgeRatioDictionary['AMZN']
##                            print s1,'vs.',s2,'A3******************'
##                            print self.PairDollarizedHedgeRatioDictionary[s1][s2]
##                            print self.PairDollarizedHedgeRatioDictionary[s2][s2]
##                            #STOP
##                        #stop
##                    if s1 == 'AMZN':
##                        if s2 == 'AAPL':
##                            print s1,'vs.',s2,'B******************'
##                            print df_bhr
##                        #stop

                    res = smf.ols( s2 + ' ~ days_since', data=df_diff[['days_since',s2]] ).fit().params
                    slope_value = res['days_since']
                    dict_of_slopes = {'ticker':s2,s1:slope_value}
                    list_of_dict_of_slopes.append(dict_of_slopes)
                df_slope_x = pd.DataFrame(list_of_dict_of_slopes)
                df_slope_x.set_index("ticker", drop=True, inplace=True)
                df_slope[s1] = df_slope_x
        self.SlopeOfPairsDollarizedDataframe = df_slope
        return True
    
    def setadvancedclassvariables(self,
                    ):
        print 'started setadvancedclassvariables'
        df = self.ClosePricesDataframe
        
        from datetime import datetime

        list_of_dict_of_slopes = []
        list_of_dict_of_betahr = []
        #dict_of_dfs ={}
        columns = self.SymbolsList
        i2 = 0
        df_slope = pd.DataFrame(index = self.SymbolsList)
        df_betahr = pd.DataFrame(index = self.SymbolsList)
        dict_pairdiff_dollarizedhedgeratio = {}
        for column in columns:
            print 'setadvancedclassvariables',column
            df_diff_dollarizedhedgeratio = pd.DataFrame(index = df.index)    
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
                    slope_value = res['days_since']
                    dict_of_slopes = {'ticker':s2,s1:slope_value}
                    list_of_dict_of_slopes.append(dict_of_slopes)
                    
                    Y=df[s2].tolist()
                    X=df[s1].tolist()
                    results = sm.OLS(Y, X).fit()
                    betahr_value = results.params
                    betahr_value = float(betahr_value[0])
                    dict_of_betahr = {'ticker':s2,s1:betahr_value} 
                    list_of_dict_of_betahr.append(dict_of_betahr)
                    ser_1 = df[s1] * betahr_value
                    df_1 = ser_1.to_frame(s2)
                    df_diff_dollarizedhedgeratio =  pd.concat([df_diff_dollarizedhedgeratio, df_1], axis=1)
                #print 'df_diff_dollarizedhedgeratio','================================================='
                #print df_diff_dollarizedhedgeratio
                
                df_slope_x = pd.DataFrame(list_of_dict_of_slopes)
                df_slope_x.set_index("ticker", drop=True, inplace=True)
                df_slope[s1] = df_slope_x

                df_betahr_x = pd.DataFrame(list_of_dict_of_betahr)
                df_betahr_x.set_index("ticker", drop=True, inplace=True)
                df_betahr[s1] = df_betahr_x
                #print 'About to create',s1
                dict_pairdiff_dollarizedhedgeratio[s1] = df_diff_dollarizedhedgeratio
                
        self.PairDollarizedHedgeRatioDictionary = dict_pairdiff_dollarizedhedgeratio
        self.SlopeOfDiffsDataframe = df_slope
        self.BetaHedgeRatioDataframe = df_betahr
        print 'finished with setadvancedclassvariables'
        return True

    def setclassdictionaries(self,list_of_tickers = [],closepricesfilepath = '',fromdate = '2017-01-01',todate = '2017-12-31'):
        
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
            print df
            df2 = df["Date"]
            df.set_index("Date", drop=True, inplace=True)
        
        if len(list_of_tickers) == 0:
            columns = list(df.columns.values)
        else:
            columns = list_of_tickers
        df = df[columns]
        
        self.ClosePricesDataframe = df
        self.SymbolsList = columns
        print 'self.SymbolsList = columns', self.SymbolsList

        df_openshares = 10000.0 / df.iloc[[0]]
        df_shares2 = df_openshares.append([df_openshares]*(len(df)-1),ignore_index=True)
        df_shares3 = pd.concat([df2, df_shares2], axis=1)
        df_shares3.set_index("Date", drop=True, inplace=True)
        df_dollarized = df.multiply(df_shares3, axis=1)
        dict_pairdiff_dollarized = {}

        dict_pairdiff_prices = {}
        i2 = 0
        for column in columns:
            print 'setclassdictionaries',column
            df_diff_prices = df[columns].sub(df[column], axis=0)
            dict_pairdiff_prices[column] = df_diff_prices
            df_diff_dollarized = df_dollarized[columns].sub(df_dollarized[column], axis=0)
            dict_pairdiff_dollarized[column] = df_diff_dollarized
            i2 +=1
            #if i2 >= 6:
            #    break

        self.PairPricesDiffDictionary = dict_pairdiff_prices
        self.PairDollarizedDiffDictionary = dict_pairdiff_dollarized
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
    
    list_of_tickers = [ 'AAL','AAPL','PCLN','CA','CHD','GOOG','GOOGL','MSFT','AMZN' ]
    #list_of_tickers = [ 'PCLN','MSFT']

##        self.PairDollarizedHedgeRatioDictionary = dict_pairdiff_dollarizedhedgeratio
##        self.SlopeOfDiffsDataframe = df_slope
##        self.BetaHedgeRatioDataframe = df_betahr

    
    #o = find(closepricesfilepath = 'C:\\Batches\\GitStuff\\$work\\closeprices_sample.csv', list_of_tickers=list_of_tickers)
    #o = find(list_of_tickers=list_of_tickers,closepricesfilepath = '', fromdate='2017-07-01',todate='2017-12-31')
    o = find(list_of_tickers=list_of_tickers,closepricesfilepath = 'C:\\Batches\\GitStuff\\$work\\closeprices_sample.csv')
    
    b = o.setadvancedclassvariables()
    print 'done',b
    print '----------------'
    print 'df_slope'
    print o.SlopeOfDiffsDataframe.round(3)
    cachedfilepathname = 'C:\\Batches\\GitStuff\\$work\\slopes.csv'
    o.SlopeOfDiffsDataframe.to_csv(cachedfilepathname,columns=(list(o.SlopeOfDiffsDataframe.columns.values)))
    
    print '----------------'
    print 'df_betahr'
    print o.BetaHedgeRatioDataframe.round(3)
    cachedfilepathname = 'C:\\Batches\\GitStuff\\$work\\betahr.csv'
    o.BetaHedgeRatioDataframe.to_csv(cachedfilepathname,columns=(list(o.BetaHedgeRatioDataframe.columns.values)))
    
    #print '----------------'
    #print 'df_dollarizedbetahedgereturn AAPL'
    #print o.PairDollarizedHedgeRatioDictionary['AAPL']
    #for k, v in o.PairDollarizedHedgeRatioDictionary.items():
    #    print '================================================================'
    #    print 'Key',k
    #    print v
    

##    print '----------------'
##    for k,v in o.PairDollarizedHedgeRatioDiffDictionary.items():
##        print '||',k,'||'
##        print v

    
    print 'SlopeOfPairsDollarizedDataframe'
    #print 'This shows the slope of the price differences between stock A''s [close price] * [beta hedge ratio with stock B] vs stock B''s [close price].'
    print 'This shows the slope of dollarized price differences between all stock comparisons: A and B.'
    print o.SlopeOfPairsDollarizedDataframe
    ticker1 = 'PCLN'
    ticker2 = 'MSFT'
    ticker1_closeprice = o.ClosePricesDataframe[-1:][ticker1].iloc[0]
    ticker2_closeprice = o.ClosePricesDataframe[-1:][ticker2].iloc[0]
    print 'PairDollarizedDiffDictionary',ticker1,ticker2
    print o.PairDollarizedDiffDictionary[ticker1][ticker2]
    df_0 = pd.concat([
                            o.PairDollarizedDiffDictionary[ticker1][ticker2].to_frame('diff')
                            #, self.PairMovingAverageDiffDictionary[ticker1][ticker2].to_frame('ma')
                            #, self.PairRunningMaxDiffDictionary[ticker1][ticker2].to_frame('max')
                            #, self.PairRunningMinDiffDictionary[ticker1][ticker2].to_frame('min')
                    ], axis=1)
    df_0.plot.line(title=ticker2 +'='+str(round(ticker2_closeprice,2)) + ' ' + ticker1+'='+str(round(ticker1_closeprice,2)))
                        #df_ma.plot.line(title=ticker1 + ' ' + ticker2)
                        
                        #plt.plot(label='Sample Label Red')
    plt.show()

        
##        
    
##    for column in list(o.ClosePricesDataframe.columns):
##        
##        for k,v in o.PairDollarizedHedgeRatioDictionary.items():
##            print '++++++++++++++++++++++++++++++++'
##            print column, '++',k,'++'
##            print o.ClosePricesDataframe[column].to_frame(column+' actual')
##            print o.PairDollarizedHedgeRatioDictionary[k][column].to_frame(k+' in '+ column + ' terms')
##            #print v[k].to_frame(k)
##            stop
            #pd.concat(df_0, df_1], axis=1)
    
##    cachedfilepathname_slope = 'C:\\Batches\\GitStuff\\$work\\slopes.csv'
##    d2['df_slope'].to_csv(cachedfilepathname_slope,columns=(list(d2['df_slope'].columns.values)))
##
##    cachedfilepathname_betahr = 'C:\\Batches\\GitStuff\\$work\\betahr.csv'
##    d2['df_betahr'].to_csv(cachedfilepathname_betahr,columns=(list(d2['df_betahr'].columns.values)))

    #cachedfilepathname_SlopeOfDollarizedHedgeRatio = 'C:\\Batches\\GitStuff\\$work\\SlopeOfDollarizedHedgeRatio.csv'
    #o.SlopeOfPairsDollarizedDataframe.to_csv(cachedfilepathname_SlopeOfDollarizedHedgeRatio,columns=(list(o.SlopeOfPairsDollarizedDataframe.columns.values)))

