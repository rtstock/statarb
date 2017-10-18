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
    #TickerSignDataframe
    def set_TickerSignDataframe(self,TickerSignDataframe):
        self._TickerSignDataframe = TickerSignDataframe
    def get_TickerSignDataframe(self):
        return self._TickerSignDataframe
    TickerSignDataframe = property(get_TickerSignDataframe, set_TickerSignDataframe)

    def set_SymbolsList(self,SymbolsList):
        self._SymbolsList = SymbolsList
    def get_SymbolsList(self):
        return self._SymbolsList
    SymbolsList = property(get_SymbolsList, set_SymbolsList)

    #SignsList
    def set_SignsList(self,SignsList):
        self._SignsList = SignsList
    def get_SignsList(self):
        return self._SignsList
    SignsList = property(get_SignsList, set_SignsList)
    
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


    #PairPricesBetaHedgeRatioDictionary
    def set_PairPricesBetaHedgeRatioDictionary(self,PairPricesBetaHedgeRatioDictionary):
        self._PairPricesBetaHedgeRatioDictionary = PairPricesBetaHedgeRatioDictionary
    def get_PairPricesBetaHedgeRatioDictionary(self):
        return self._PairPricesBetaHedgeRatioDictionary
    PairPricesBetaHedgeRatioDictionary = property(get_PairPricesBetaHedgeRatioDictionary, set_PairPricesBetaHedgeRatioDictionary)

    #DollarizedComparisonDataframe
    def set_DollarizedComparisonDataframe(self,DollarizedComparisonDataframe):
        self._DollarizedComparisonDataframe = DollarizedComparisonDataframe
    def get_DollarizedComparisonDataframe(self):
        return self._DollarizedComparisonDataframe
    DollarizedComparisonDataframe = property(get_DollarizedComparisonDataframe, set_DollarizedComparisonDataframe)

    #SaveCSVPathName
    def set_SaveCSVPathName(self,SaveCSVPathName):
        self._SaveCSVPathName = SaveCSVPathName
    def get_SaveCSVPathName(self):
        return self._SaveCSVPathName
    SaveCSVPathName = property(get_SaveCSVPathName, set_SaveCSVPathName)

    def __init__(self                 
                 , list_of_tickersigns=[]
                 , closepricesfilepath = ''
                 , fromdate = '2017-01-01'
                 , todate = '2017-12-31'
                 
                 ):

        b1 = self.setclassdictionaries(list_of_tickersigns=list_of_tickersigns,closepricesfilepath = closepricesfilepath,fromdate=fromdate,todate=todate)
        b2 = self.setdollarweightdataframe(parvalue = 40000.0)
        #b2 = self.setdollarizedataframe()
        #setbetahrdataframe_test
        #b2 = self.setbetahrdataframe_test(list_of_symbols=self.SymbolsList,closepricesfilepath = self.SaveCSVPathName,fromdate=fromdate,todate=todate)
        #b2 = self.setbetahrdictionary(list_of_symbols=self.SymbolsList,closepricesfilepath = self.SaveCSVPathName,fromdate=fromdate,todate=todate)
        #b3 = self.createdollarizedcomparisondataframe(useopeningorclosinghedgeratio=useopeningorclosinghedgeratio)
        
        
    


    def runmyportfoliopnl(self,portfolioname='port1'):
        #ddddd    
        list_of_symbols = self.SymbolsList
        df_analyze1 = self.DollarizedComparisonDataframe
        df_analyze2 = pd.DataFrame(index=df_analyze1.index.copy())
        
        listx = self.SignsList
        df_signs = pd.DataFrame([listx],columns = list_of_symbols,index=df_analyze1.index.copy())
        
        df_b = pd.DataFrame(df_analyze1.values*df_signs.values, columns=df_analyze1.columns, index=df_analyze1.index)
        
        df_b['sum'] = df_b.sum(axis=1)

        print df_b
        #stop
        df_analyze2[portfolioname] = df_b['sum']
        #print 'df_analyze2',df_analyze2
        
        mytitle = self.TickerSignDataframe.to_string(header=False) #header=False,
        
        df_analyze2max = df_analyze2.cummax()
        df_analyze2min = df_analyze2.cummin()

        #print 'df_analyze2.index', df_analyze2.index
        #print 'df_analyze2[portfolioname]', df_analyze2[portfolioname]
        plt.plot(df_analyze2.index, df_analyze2[portfolioname], label=mytitle)
        
        plt.legend(fontsize=8) # using a size in points
        plt.show()
        
    def setclassdictionaries(self,list_of_tickersigns = [],closepricesfilepath = '',fromdate = '2017-01-01',todate = '2017-12-31'):
        print 'started def setclassdictionaries'
        df_tickers = pd.DataFrame(list_of_tickersigns, columns = ['ticker','sign','weight'])
        df_tickers.set_index("ticker", drop=True, inplace=True)
        self.TickerSignDataframe = df_tickers
        list_of_symbols = df_tickers.index.tolist()
        self.SymbolsList = list_of_symbols
        list_of_signs = df_tickers['sign'].tolist()
        self.SignsList = list_of_signs
        
        if len(closepricesfilepath) == 0:
            print 'go to pull prices'
            import pullprices as pp
            o = pp.pull()
            o.setclassdataframes(symbols=list_of_symbols,fromdate = fromdate,todate = todate)
            df = o.ClosePricesDataframe
            self.SaveCSVPathName = o.SaveCSVPathName
        else:
            myfile = closepricesfilepath #'C:\Batches\GitStuff\$work\closeprices_sample.csv'
            self.SaveCSVPathName = closepricesfilepath
            df = pd.read_csv(myfile)
            df.set_index("Date", drop=True, inplace=True)
            
        if len(list_of_tickersigns) == 0:
            columns = list(df.columns.values)
        else:
            columns = list_of_symbols
        df = df[columns]
        
        self.ClosePricesDataframe = df

        
        print 'finished def setclassdictionaries'
        
        
        return True

    def setdollarweightdataframe(self,parvalue = 10000.0):
        df = self.ClosePricesDataframe

        #33333

        df_denominator = df.iloc[[0]]
        #sum_of_prices = df_denominator.sum(axis=1).iloc[0] #jjjjj


        list_of_dates = list(df.index)
        list_of_dates_sorted = sorted(list_of_dates)
        df2 = pd.DataFrame({'Date':list_of_dates_sorted})

        #print 'df_denominator', df_denominator
        
        df_openshares = parvalue / df_denominator * self.TickerSignDataframe['weight']
        #print 'df_openshares',df_openshares
        #stop
        df_shares2 = df_openshares.append([df_openshares]*(len(df)-1),ignore_index=True)
        #print 'df_shares2', df_shares2
        #stop
        df_shares3 = pd.concat([df2, df_shares2], axis=1)
        df_shares3.set_index("Date", drop=True, inplace=True)
        #print 'df_shares3',df_shares3
        #stop
        df_dollarized = self.ClosePricesDataframe.multiply(df_shares3, axis=1)
        #print 'df_dollarized',df_dollarized
        #stop
        self.DollarizedComparisonDataframe = df_dollarized
        #print 'df_dollarized',df_dollarized
        #stop
        return True
    
    def setdollarizedataframe(self,parvalue = 10000.0, useopeningorclosinghedgeratio = 'opening'):
        df = self.ClosePricesDataframe

        #33333

        df_denominator = df.iloc[[0]]
        sum_of_prices = df_denominator.sum(axis=1).iloc[0] #jjjjj


        list_of_dates = list(df.index)
        list_of_dates_sorted = sorted(list_of_dates)
        df2 = pd.DataFrame({'Date':list_of_dates_sorted})

        #print 'df_denominator', df_denominator
        
        df_openshares = parvalue / df_denominator
        #print 'df_openshares',df_openshares
        #stop
        df_shares2 = df_openshares.append([df_openshares]*(len(df)-1),ignore_index=True)
        #print 'df_shares2', df_shares2
        #stop
        df_shares3 = pd.concat([df2, df_shares2], axis=1)
        df_shares3.set_index("Date", drop=True, inplace=True)
        #print 'df_shares3',df_shares3
        #stop
        df_dollarized = self.ClosePricesDataframe.multiply(df_shares3, axis=1)
        #print 'df_dollarized',df_dollarized
        self.DollarizedComparisonDataframe = df_dollarized
        #print 'df_dollarized',df_dollarized
        #stop
        return True

##    def createlistofsigns(self,list_of_tickersigns):
##        import itertools
##        list_0 = []
##        i0 = -1
##        for x in list_of_tickersigns:
##            i0 = i0*-1
##            list_0.append(i0)            
##        list_1 = list(itertools.permutations(list_0))
##        list_2 = pd.Series(list_1).drop_duplicates().tolist()
##        list_3 = []
##        i1 = 1
##        for x in list_2:
##            list_3.append(('x'+str(i1),x))
##            i1 += 1
##        self.SignsList = list_3
##        return True
        
if __name__=='__main__':

    '''
        list_of_signs = [
                         ('a',[ 1, 1,-1,-1])
                        ,('b',[-1, 1, 1,-1])
                        ,('c',[-1,-1, 1, 1])
                        ,('d',[ 1,-1,-1, 1])
                        ,('e',[-1, 1,-1, 1])
                        ,('f',[ 1,-1, 1,-1])
                         ]
    '''

    list_of_tickersigns = [
         ['MSFT',1,0.40]
        ,['AAPL',-1,0.25]
        ,['PCLN',-1,0.25]
        ,['CSCO',1,0.10]
        ]

##    list_of_tickersigns = [
##         ['MSFT',-1]
##        ,['AAPL',-1]
##        ,['CRM',-1]
##        ,['BAC',-1]
##        ,['C',-1]
##        ,['PCLN',1]
##        ,['AMZN',1]
##        ,['GOOG',1]
##        ,['JPM',1]
##        ,['MS',1]        
##        ]

    
    #list_of_tickersigns = [
        # ['MSFT',1]
        #,['AAPL',1]
        #,['CRM',1]
        #,['BAC',1]
        #,['C',1]
        #,['PCLN',-1]
        #,['AMZN',-1]
        #,['GOOG',-1]
        #,['JPM',-1]
        #,['MS',-1]
        #,['AAL',-1]
        #,['DAL',-1]
        #,['JBLU',-1]
        #,['LUV',-1]        
        #]
    
    o = find(list_of_tickersigns=list_of_tickersigns,closepricesfilepath = '', fromdate='2015-01-01',todate='2016-03-31')
    
    o.runmyportfoliopnl(portfolioname='port1')

    # = find(list_of_tickersigns=list_of_tickersigns,closepricesfilepath = '', fromdate='2017-03-31',todate='2017-12-31')
    #o.runportfoliopnl(useopeningorclosinghedgeratio='opening')
