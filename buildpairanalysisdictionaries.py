import pandas as pd
class build:
    def __init__(self,pairdataframe, movingaveragewindow = 70):
        print 'intialized buildpairanalysisdictionaries'
        self.setclassdictionaries(pairdataframe=pairdataframe, movingaveragewindow = movingaveragewindow)
        print 'done buildpairanalysisdictionaries'
    def set_SymbolsList(self,SymbolsList):
        _SymbolsList = SymbolsList
    def get_SymbolsList(self):
        return _SymbolsList
    SymbolsList = property(get_SymbolsList, set_SymbolsList)

    def set_PairRunningMaxDiffDictionary(self,PairRunningMaxDiffDictionary):
        _PairRunningMaxDiffDictionary = PairRunningMaxDiffDictionary
    def get_PairRunningMaxDiffDictionary(self):
        return _PairRunningMaxDiffDictionary
    PairRunningMaxDiffDictionary = property(get_PairRunningMaxDiffDictionary, set_PairRunningMaxDiffDictionary)

    def set_PairRunningMinDiffDictionary(self,PairRunningMinDiffDictionary):
        _PairRunningMinDiffDictionary = PairRunningMinDiffDictionary
    def get_PairRunningMinDiffDictionary(self):
        return _PairRunningMinDiffDictionary
    PairRunningMinDiffDictionary = property(get_PairRunningMinDiffDictionary, set_PairRunningMinDiffDictionary)

    def set_PairBetweenMaxMinDiffDictionary(self,PairBetweenMaxMinDiffDictionary):
        _PairBetweenMaxMinDiffDictionary = PairBetweenMaxMinDiffDictionary
    def get_PairBetweenMaxMinDiffDictionary(self):
        return _PairBetweenMaxMinDiffDictionary
    PairBetweenMaxMinDiffDictionary = property(get_PairBetweenMaxMinDiffDictionary, set_PairBetweenMaxMinDiffDictionary)

    def set_PairRunningPctDiffDictionary(self,PairRunningPctDiffDictionary):
        _PairRunningPctDiffDictionary = PairRunningPctDiffDictionary
    def get_PairRunningPctDiffDictionary(self):
        return _PairRunningPctDiffDictionary
    PairRunningPctDiffDictionary = property(get_PairRunningPctDiffDictionary, set_PairRunningPctDiffDictionary)

    def set_PairPricesDiffDictionary(self,PairPricesDiffDictionary):
        _PairPricesDiffDictionary = PairPricesDiffDictionary
    def get_PairPricesDiffDictionary(self):
        return _PairPricesDiffDictionary
    PairPricesDiffDictionary = property(get_PairPricesDiffDictionary, set_PairPricesDiffDictionary)

    def set_ClosePricesDataframe(self,ClosePricesDataframe):
        _ClosePricesDataframe = ClosePricesDataframe
    def get_ClosePricesDataframe(self):
        return _ClosePricesDataframe
    ClosePricesDataframe = property(get_ClosePricesDataframe, set_ClosePricesDataframe)


    def set_PairMovingAverageDiffDictionary(self,PairMovingAverageDiffDictionary):
        _PairMovingAverageDiffDictionary = PairMovingAverageDiffDictionary
    def get_PairMovingAverageDiffDictionary(self):
        return _PairMovingAverageDiffDictionary
    PairMovingAverageDiffDictionary = property(get_PairMovingAverageDiffDictionary, set_PairMovingAverageDiffDictionary)

    def set_PairMovingStdevDiffDictionary(self,PairMovingStdevDiffDictionary):
        _PairMovingStdevDiffDictionary = PairMovingStdevDiffDictionary
    def get_PairMovingStdevDiffDictionary(self):
        return _PairMovingStdevDiffDictionary
    PairMovingStdevDiffDictionary = property(get_PairMovingStdevDiffDictionary, set_PairMovingStdevDiffDictionary)



    def setclassdictionaries(self,pairdataframe, movingaveragewindow = 70):
        
        print 'started def setclassdictionaries'
        import pullstackedprices as pp1
        df = pairdataframe
        
        import pandas as pd

        
        list_of_dates = list(df.index)
        list_of_dates_sorted = sorted(list_of_dates)
        df2 = pd.DataFrame({'Date':list_of_dates_sorted})

        columns = list(df.columns.values)

        dict_pairdiff_runningmax = {}
        dict_pairdiff_runningmin = {}
        dict_pairdiff_betweenmaxmin = {}
        dict_pairdiff_runningpct = {}
        dict_pairdiff_prices = {}
        dict_pairdiff_movingaverage = {}
        dict_pairdiff_standarddeviation = {}
        
        
        print 'started creating class dictionaries...'
        
        i2 = 0
        for column in columns:
            df_diff_runningmax = pd.DataFrame(index = df.index)
            df_diff_runningmin = pd.DataFrame(index = df.index)
            df_diff_movingaverage = pd.DataFrame(index = df.index)
            df_diff_stdev = pd.DataFrame(index = df.index)
            
            print 'setclassdictionaries',column
            df_diff_prices = df[columns].sub(df[column], axis=0)
            #df_diff_prices = df_diff_prices.abs()
            #df_diff_prices = df_diff #df[columns].sub(df[column], axis=0)
            i3 = 0
            for column1 in columns:
                df_diff_prices1 = df_diff_prices[column1].to_frame(column1)
                df_diff_runningmax[column1] = df_diff_prices1.rolling(window=movingaveragewindow).max() #df_diff1[column1].cummax().to_frame(column1)
                df_diff_runningmin[column1] = df_diff_prices1.rolling(window=movingaveragewindow).min() #df_diff1[column1].cummin().to_frame(column1) #ssss

                #df_diff_runningmax[column1] = df_diff1[column1].cummax().to_frame(column1)
                #df_diff_runningmin[column1] = df_diff1[column1].cummin().to_frame(column1) #ssss
                df_diff_movingaverage[column1] = df_diff_prices1.rolling(window=movingaveragewindow).mean()
                df_diff_stdev[column1] = df_diff_prices1.rolling(window=movingaveragewindow).std()
                i3 += 1
            
            df_diff_betweenmaxmin = df_diff_runningmax[columns].sub(df_diff_runningmin[columns], axis=0)
            df_diff_runningpct = ( df_diff_prices - df_diff_runningmin ) / ( df_diff_runningmax - df_diff_runningmin)             
            
            

            dict_pairdiff_prices[column] = df_diff_prices
            
            dict_pairdiff_runningmax[column] = df_diff_runningmax
            dict_pairdiff_runningmin[column] = df_diff_runningmin
            dict_pairdiff_betweenmaxmin[column] = df_diff_betweenmaxmin
            dict_pairdiff_runningpct[column] = df_diff_runningpct
            
            dict_pairdiff_movingaverage[column] = df_diff_movingaverage
            dict_pairdiff_standarddeviation[column] = df_diff_stdev
            i2 +=1
            #if i2 >= 6:
            #    break
        print 'finished creating class dictionaries...'
        self.PairPricesDiffDictionary = dict_pairdiff_prices
        self.PairRunningMaxDiffDictionary = dict_pairdiff_runningmax
        self.PairRunningMinDiffDictionary = dict_pairdiff_runningmin
        self.PairBetweenMaxMinDiffDictionary = dict_pairdiff_betweenmaxmin
        self.PairRunningPctDiffDictionary = dict_pairdiff_runningpct
        
        self.PairMovingAverageDiffDictionary = dict_pairdiff_movingaverage
        self.PairMovingStdevDiffDictionary = dict_pairdiff_standarddeviation
        self.SymbolsList = columns

        return True

##if __name__=='__main__':
##
##    #symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL', ]
##    symbols = ['GOOG', 'GOOGL', ]
##    print symbols
##    import pullstackedprices as psp
##    df = psp.stockpricesstacked(symbols,'2013-07-01','2017-08-05')
##    o = build(pairdataframe=df, movingaveragewindow = 50)
##    #o.setclassdictionaries(pairdataframe=df, movingaveragewindow = 50)
##    for k,v in o.PairPricesDiffDictionary.items():
##        print k,v

if __name__=='__main__':
    
    list_of_tickersigns1 = [
         ['MS',1,1.0]
        ,['BAC',1,1.0]
        ,['C',-1,1.0]
        ,['JPM',-1,1.0]
        ]

    list_of_tickersigns2 = [
        ['AAL',-1,1.0]
        ,['DAL',-1,1.0]
        ,['JBLU',1,1.0]
        ,['LUV',1,1.0]     
        ]
    fromdate, todate='2014-01-01','2017-12-31'
    parvalue=1000.0

    import calculateportfoliopnl as ccp
    
    o1 = ccp.find(list_of_tickersigns=list_of_tickersigns1,fromdate=fromdate, todate=todate,parvalue=parvalue)
    df1 = o1.runmyportfoliopnl(portfolioname='port1',showplot=False)

    o2 = ccp.find(list_of_tickersigns=list_of_tickersigns2,fromdate=fromdate, todate=todate,parvalue=parvalue)
    df2 = o2.runmyportfoliopnl(portfolioname='port2',showplot=False)

    df3 = pd.concat([df1, df2], axis=1)
    o3 = build(pairdataframe=df3, movingaveragewindow = 50)

    for k,v in o3.PairPricesDiffDictionary.items():
        print k,v.round(3)
    
