#C:\Batches\GitStuff\$work\correlation_sample.csv
import pandas as pd
import numpy as np
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
    
    def __init__(self,
                 closepricesfilepath, movingaveragewindow):

        #self.PairMovingAverageDiffDictionary, columns = self.setclassdictionaries(closepricesfilepath)
        b = self.setclassdictionaries(closepricesfilepath = closepricesfilepath,movingaveragewindow = movingaveragewindow)
        df_extreme = self.PairRunningPctDiffDictionary['AAPL']['ABBV'].loc[self.PairRunningPctDiffDictionary['AAPL']['ABBV'].isin([0.0,1.0])].to_frame()
        print 'df_extreme',df_extreme
        
        my_tradedate = df_extreme.iloc[len(df_extreme)-2].name
        my_triggervalue  = df_extreme['ABBV'].iloc[len(df_extreme)-2]
        print 'latest opportunity', my_tradedate, my_triggervalue
        self.testone('AAPL','ABBV',my_tradedate,my_triggervalue)
        for idx ,row in self.PairRunningPctDiffDictionary['AAPL'].iterrows():
            print idx, row['ABBV'], self.PairPricesDiffDictionary['AAPL']['ABBV'][idx]
            #stop
                
        stop
        
        #------- Testing
##        df_1a = self.PairPricesDiffDictionary['A']
##        df_1b = self.PairMovingAverageDiffDictionary['A']
##        for idx,row in self.PairMovingAverageDiffDictionary['A']['AAL'].to_frame().iterrows():
##            print idx, row['AAL']
##            if idx > '2016-03-02':
##                stop
            
##        df_1c = self.PairMovingStdevDiffDictionary['A']
##        
##        df_2a = df_1a['AAL'].to_frame()
##        df_2a.columns.values[0]='diff'
##        #print df_2a
##        #stop
##        df_2b = df_1b['AAL'].to_frame()
##        df_2b.columns.values[0]='diff_ma'
##
##        df_2c = df_1c['AAL'].to_frame()
##        df_2c.columns.values[0]='diff_mstdev'
##        
##        df_x = pd.concat([df_2a, df_2b, df_2c], axis=1)
##        for idx,row in df_x.iterrows():
##            print idx, row['diff'],row['diff_ma'],row['diff_mstdev']
##            if idx > '2016-03-02':
##                stop
##        stop
        
        #rowbegin = self.PairDollarizedDiffDictionary.index[self.PairDollarizedDiffDictionary.iloc[0]]
        #print rowbegin
        #stop 
        i = 0
        for column in self.SymbolsList:
            print 'Doing',column, i, 'of',len(self.SymbolsList)
            if column == 'CA':
                df = self.runbyticker(column)
                if i == 0:
                    df1 = df.copy()
                else:
                    df1 = pd.concat([df1, df], ignore_index=True)
            i +=1
            #if i >= 6:
            #    df2 = df1.sort_values('crosscount')
            #    print df2
        #print df1
        df2 = df1.sort_values('crosscount')
        cachedfilepathname = 'C:\\Batches\\GitStuff\\$work\\paircrosscount_sample.csv'
        df1.to_csv(cachedfilepathname,columns=(list(df1.columns.values)))

    def testone(self,ticker1,ticker2,tradedate,triggervalue, maxgain=1000.0):
        print ticker1,ticker2,tradedate,triggervalue
        df1a = self.ClosePricesDataframe
        df1a = df1a[(df1a.index >= tradedate)]
        df2 = pd.DataFrame(index=df1a.index.copy())
        print '----------------- ++++'
        df1a = df1a[[ticker1,ticker2]]
        #print df
        
        columns = list(df1a.columns.values)
        print 'columns',columns
        df_openprices= df1a.iloc[[0]]
        print 'df_openprices', df_openprices
        df_openshares = 10000.0 / df1a.iloc[[0]]
        print 'df_openshares',df_openshares
        print '--------------------------kkkk'
        df_blotter = df1a * df_openshares.loc[tradedate]
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
                    'date':idx, '02_dollarized1':sign_for_ticker1 * row[ticker1], '02_dollarized2':sign_for_ticker2 * row[ticker2], '03_pl':( sign_for_ticker1 * row[ticker1] ) + ( sign_for_ticker2 * row[ticker2] ), '04_triggervalue':triggervalue, '05_pricediff':self.PairPricesDiffDictionary[ticker1][ticker2][idx],'06_ticker1':ticker1,'06_ticker2':ticker2,'07_openprice_ticker1':df_openprices.iloc[0][ticker1],'07_openprice_ticker2':df_openprices.iloc[0][ticker2],'08_openshares_ticker1':df_openshares.iloc[0][ticker1],'07_openshares_ticker2':df_openshares.iloc[0][ticker2]
                    }
            list_of_my_dicts.append(my_dict)
        df_final = pd.DataFrame(list_of_my_dicts)
        df_final.set_index("date", drop=True, inplace=True)
        print df_final
        print '-------------------------------------------------'
        print df_final.iloc[:1].iloc[0]
        
            #if idx > '2016-03-02':
            #        break
        print '-------------------------------------------------'
        print df_final[(df_final['03_pl'] >= maxgain)].iloc[:1].iloc[0]
        stop
##        for idx,row in df1a.iterrows():
##            print 'x',idx, row['A'],row['AAL']
##            #if idx > '2016-03-02':
##            #        break
##        stop
##        df_shares2 = df_openshares.append([df_openshares]*(len(df)-1),ignore_index=True)
##        df_shares3 = pd.concat([df2, df_shares2], axis=1)
##        print 'df_shares2',df_shares2
##        
##        df_shares3.set_index("Date", drop=True, inplace=True)
##        print df_shares3
##        stop
##        df_dollarized = df.multiply(df_shares3, axis=1)
##        print df_dollarized
##        stop
        
    def runbyticker_saved(self,ticker):
        #print mydict
        import pandas as pd
        import numpy as np
        dict_pairdiff_dollarized = self.PairDollarizedDiffDictionary
        ticker1 = ticker
        df = dict_pairdiff_dollarized[ticker1]
        i = 0
        mylist = []
        for column in df:
            i +=1
            #print df[column]
            df1 = pd.DataFrame({'value1':df[column]})
            #df1['ticker2'] = column
            df1['value2'] = df1.value1.shift(-1)
            df1['value31'] = df1.value1/abs(df1.value1)
            df1['value32'] = df1.value2/abs(df1.value2)
            df1['value4'] = df1['value31'] * df1['value32']
            #print df1
            #stop
            #df1['cross'] = np.where(  np.logical_or(np.logical_and(df1['value2']>0,df1['value1']<0), np.logical_and(df1['value1']>0,df1['value2']<0)),'yes', 'no')
            #df1['cross'] = np.where(  abs(df1['value1'])>0,df1['value1']<0), np.logical_and(df1['value1']>0,df1['value2']<0)),'yes', 'no')
            df2 = df1.loc[df1['value4'] == -1]
            prevvalue = -9999.99
            if len(df2) > 30 and len(df2) < 50 :
                #print df
                print 'Comparing',ticker1, column
                rowbegin = df1.iloc[0]
                #print 'rowbegin',rowbegin
                #print 'dataframeendx', df1.iloc[len(df)-1]['value1']
                dataframeend = df1.iloc[len(df)-1]
                dataframeendindex = dataframeend.name
                dataframeendvalue = df1.iloc[len(df)-1]['value1']
                #print 'dataframeend', df1.tail(1)
                #stop
                rowbeginindex = rowbegin.name
                #print 'rowbegin index', rowbeginindex
                j = 0
                for idx,rowend in df2.iterrows():
                    j += 1
                    rowendindex = rowend.name
                    #print 'rowend index', rowendindex
                    mask = (df1.index > rowbeginindex) & (df1.index <= rowendindex)
                    df3 = df1.loc[mask]
                    #print df3
                    
                    if df3.iloc[0]['value1'] > 0:
                        currvalue = df3.loc[df3['value1'].idxmax()]['value1']
                    else:
                        currvalue = df3.loc[df3['value1'].idxmin()]['value1']
                    if not prevvalue == -9999.99:
                        print ticker1, column, rowbeginindex,rowendindex,'diff', round(prevvalue,2), '-', round(currvalue,2) , '=', round(abs(prevvalue - currvalue),2)
                    prevvalue = currvalue
                    rowbeginindex = rowendindex
                    #if j >= 10:
                    #    stop
                mask = (df1.index > rowbeginindex) & (df1.index <= dataframeendindex)
                df3 = df1.loc[mask]
                print df3
                print 'check where investment got out of hand here'
                print 'add the sum of the inflexions to the crosscount, perhaps mean, average days between crosses?'
                #print 'lastvalues',prevvalue, valueend
                stop
            dict1 = {'ticker1':ticker1,'ticker2':column,'crosscount':len(df2)}
            mylist.append(dict1)
        df_final1 = pd.DataFrame(mylist)
        return df_final1

    
    def runbyticker(self,ticker):
        import pandas as pd
        import numpy as np
        
        ticker1 = ticker
        df_dollarized = self.PairDollarizedDiffDictionary[ticker1]
        df_runningmax = self.PairRunningMaxDiffDictionary[ticker]
        df_close = self.ClosePricesDataframe
        df_pricediff = self.PairPricesDiffDictionary[ticker1]
        df_ma = self.PairMovingAverageDiffDictionary[ticker1]
        df_stdev = self.PairMovingStdevDiffDictionary[ticker1]
        df_currdiffminusma = df_pricediff.sub(df_ma, axis=0)
        df_howmanystdevsout = df_currdiffminusma.div(df_stdev, axis=0)
        columns_ma = list(df_ma.columns.values)
        for column in columns_ma:
            if column == 'CHD':
                df_runningmax = df_pricediff[column].to_frame()
                
                    
        stop
        for column in columns_ma:
            if column == 'CHD':
                print ticker, column
                df_extreme = df_howmanystdevsout[column].loc[df_howmanystdevsout[column].abs() >= 2.9].to_frame()
                print '-------------------------------df_extreme'
                print df_extreme
                df_full = pd.concat([
                                       df_close[[ticker,column]]
                                     , df_ma[column].to_frame('ma')
                                     , df_pricediff[column].to_frame('pricediff')
                                     , df_currdiffminusma[column].to_frame('currdiffminusma')
                                     , df_howmanystdevsout[column].to_frame('howmanystdevsout')
                                     ], axis=1)
                print 'full!!!!!'
                #print df_full
                #stop
                for idx,row in df_full.iterrows():
                    print idx, round(row[ticker],2),round(row[column],2),'| ',round(row['ma'],2),' |',round(row['pricediff'],2),round(row['currdiffminusma'],2), round(row['howmanystdevsout'],2)
                                                    
                    #if idx > '2016-03-02':
                    #    break
                selected_opportunity = 4
                triggervalue = df_extreme.iloc[selected_opportunity][column]
                tradedate = df_extreme.iloc[selected_opportunity].name
                self.testone(ticker,column,tradedate,triggervalue)
                stop
            
        stop
        if 1 == 1: 
            print ' ---------------------------------------------------- df_pricediff'
            #print df_pricediff
            for idx,row in df_pricediff.iterrows():
                print idx, row['AAL']
                if idx > '2016-03-02':
                    break
            
            print ' ---------------------------------------------------- df_ma'
            #print df_ma
            for idx,row in df_ma.iterrows():
                print idx, row['AAL']
                if idx > '2016-03-02':
                    break
            print ' ---------------------------------------------------- df_currdiffminusma'
            #print df_currdiffminusma
            for idx,row in df_currdiffminusma.iterrows():
                print idx, row['AAL']
                if idx > '2016-03-02':
                    break
            #np.divide
            print ' ---------------------------------------------------- df_howmanystdevsout'
            #print df_currdiffminusma
            for idx,row in df_howmanystdevsout.iterrows():
                print idx, row['AAL']
                if idx > '2016-03-02':
                    break

        stop
        return columns_ma
    def testone_old(self,ticker1,ticker2,tradedate,triggervalue):
        print ticker1,ticker2,tradedate,triggervalue
        df1a = self.ClosePricesDataframe
        df1a = df1a[(df1a.index >= tradedate)]
        df2 = pd.DataFrame(index=df1a.index.copy())
        print '----------------- ++++'
        df1a = df1a[[ticker1,ticker2]]
        #print df
        
        columns = list(df1a.columns.values)
        print 'columns',columns
        df_openshares = 10000.0 / df1a.iloc[[0]]
        print 'df_openshares',df_openshares
        print '--------------------------kkkk'
        df_blotter = df1a * df_openshares.loc[tradedate]
        if triggervalue < 0:
            sign_for_ticker1 = -1
            sign_for_ticker2 = 1
        else:
            sign_for_ticker1 = 1
            sign_for_ticker2 = -1
            
        for idx,row in df_blotter.iterrows():
            print 'a', idx, sign_for_ticker1 * row[ticker1],sign_for_ticker2 * row[ticker2], ( sign_for_ticker1 * row[ticker1] ) + ( sign_for_ticker2 * row[ticker2] )
            #if idx > '2016-03-02':
            #        break
        print '-------------------------------------------------'
##        for idx,row in df1a.iterrows():
##            print 'x',idx, row['A'],row['AAL']
##            #if idx > '2016-03-02':
##            #        break
        stop
        df_shares2 = df_openshares.append([df_openshares]*(len(df)-1),ignore_index=True)
        df_shares3 = pd.concat([df2, df_shares2], axis=1)
        print 'df_shares2',df_shares2
        
        df_shares3.set_index("Date", drop=True, inplace=True)
        print df_shares3
        stop
        df_dollarized = df.multiply(df_shares3, axis=1)
        print df_dollarized
        stop
    def runbyticker_old2(self,ticker):
        #print mydict
        import pandas as pd
        import numpy as np
        #dict_pairdiff = self.PairMovingAverageDiffDictionary
        
        ticker1 = ticker
        #df = self.PairMovingAverageDiffDictionary[ticker1]
        #print df
        df_close = self.ClosePricesDataframe
        df_pricediff = self.PairPricesDiffDictionary[ticker1]
        df_ma = self.PairMovingAverageDiffDictionary[ticker1]
        df_stdev = self.PairMovingStdevDiffDictionary[ticker1]
        
        columns_ma = list(df_ma.columns.values)
        columns_stdev = list(df_stdev.columns.values)
        
        print ticker1, '--------------------------------------------------------------------------- ma'
        print df_ma
        print ticker1, '--------------------------------------------------------------------------- stdev'
        print df_stdev
        df_add = df_ma[columns_ma].add(df_stdev[columns_stdev], axis=0)
        print ticker1, '--------------------------------------------------------------------------- added'
        print df_add
        my_dictionary_of_list_of_dicts = {}
        for column in columns_ma:
            print 'calculating',column
            my_list_of_dicts = []
            for index, row in df_ma.iterrows():
                mydict = {'date':index,'ticker1':ticker,'ticker2':column,'a_date':index, 'b_ma':row[column], 'c_stdev':df_stdev[column].loc[index], 'd_currdiff':df_pricediff[column].loc[index], 'e_cdminusma':df_pricediff['AAPL'].loc[index] - row['AAPL'], 'g_close_1':df_close[ticker].loc[index], 'h_close_2':df_close[column].loc[index]}
                my_list_of_dicts.append(mydict)
            my_dictionary_of_list_of_dicts[column] = my_list_of_dicts
        df_result = pd.DataFrame(my_list_of_dicts)
        df_result['f_currstdaway'] = df_result['e_cdminusma'] / df_result['c_stdev']
        df_result.set_index('a_date', drop=True, inplace=True)
        
        for index, row in df_result.iterrows():
            print index, row
            #print index, row['g_close_1'],row['h_close_2'],row['b_ma'], row['c_stdev'],row['f_currstdaway'], 'AddTrade!!!'
        #print df_result
        
        stop

        i = 0
        mylist = []
        for column in df:
            i +=1
            #print df[column]
            df1 = pd.DataFrame({'value1':df[column]})
            #df1['ticker2'] = column
            df1['value2'] = df1.value1.shift(-1)
            df1['value31'] = df1.value1/abs(df1.value1)
            df1['value32'] = df1.value2/abs(df1.value2)
            df1['value4'] = df1['value31'] * df1['value32']
            #print df1
            #stop
            #df1['cross'] = np.where(  np.logical_or(np.logical_and(df1['value2']>0,df1['value1']<0), np.logical_and(df1['value1']>0,df1['value2']<0)),'yes', 'no')
            #df1['cross'] = np.where(  abs(df1['value1'])>0,df1['value1']<0), np.logical_and(df1['value1']>0,df1['value2']<0)),'yes', 'no')
            df2 = df1.loc[df1['value4'] == -1]
            prevvalue = -9999.99
            if len(df2) > 30 and len(df2) < 50 :
                #print df
                print 'Comparing',ticker1, column
                rowbegin = df1.iloc[0]
                #print 'rowbegin',rowbegin
                #print 'dataframeendx', df1.iloc[len(df)-1]['value1']
                dataframeend = df1.iloc[len(df)-1]
                dataframeendindex = dataframeend.name
                dataframeendvalue = df1.iloc[len(df)-1]['value1']
                #print 'dataframeend', df1.tail(1)
                #stop
                rowbeginindex = rowbegin.name
                #print 'rowbegin index', rowbeginindex
                j = 0
                for idx,rowend in df2.iterrows():
                    j += 1
                    rowendindex = rowend.name
                    #print 'rowend index', rowendindex
                    mask = (df1.index > rowbeginindex) & (df1.index <= rowendindex)
                    df3 = df1.loc[mask]
                    #print df3
                    
                    if df3.iloc[0]['value1'] > 0:
                        currvalue = df3.loc[df3['value1'].idxmax()]['value1']
                    else:
                        currvalue = df3.loc[df3['value1'].idxmin()]['value1']
                    if not prevvalue == -9999.99:
                        print ticker1, column, rowbeginindex,rowendindex,'diff', round(prevvalue,2), '-', round(currvalue,2) , '=', round(abs(prevvalue - currvalue),2)
                    prevvalue = currvalue
                    rowbeginindex = rowendindex
                    #if j >= 10:
                    #    stop
                mask = (df1.index > rowbeginindex) & (df1.index <= dataframeendindex)
                df3 = df1.loc[mask]
                print df3
                print 'check where investment got out of hand here'
                print 'add the sum of the inflexions to the crosscount, perhaps mean, average days between crosses?'
                #print 'lastvalues',prevvalue, valueend
                stop
            dict1 = {'ticker1':ticker1,'ticker2':column,'crosscount':len(df2)}
            mylist.append(dict1)
        df_final1 = pd.DataFrame(mylist)
        return df_final1

    def setclassdictionaries(self,closepricesfilepath,movingaveragewindow):
        
        print 'started def findpairstdev'
        import pandas as pd
        myfile = closepricesfilepath #'C:\Batches\GitStuff\$work\closeprices_sample.csv'
        df = pd.read_csv(myfile)
        #print df
        
        df2 = df["Date"]
        df.set_index("Date", drop=True, inplace=True)
        self.ClosePricesDataframe = df
        columns = list(df.columns.values)
        #columns = ['CA',     'CHD']
        df_openshares = 10000.0 / df.iloc[[0]]
        #print df_openshares
        #stop
        df_shares2 = df_openshares.append([df_openshares]*(len(df)-1),ignore_index=True)
        df_shares3 = pd.concat([df2, df_shares2], axis=1)
        df_shares3.set_index("Date", drop=True, inplace=True)

        df_dollarized = df.multiply(df_shares3, axis=1)
        dict_pairdiff_runningmax = {}
        dict_pairdiff_runningmin = {}
        dict_pairdiff_betweenmaxmin = {}
        dict_pairdiff_runningpct = {}
        dict_pairdiff_prices = {}
        dict_pairdiff_dollarized = {}
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
            df_diff = df[columns].sub(df[column], axis=0)
            i3 = 0
            for column1 in columns:
                df_diff1 = df_diff[column1].to_frame(column1)
                df_diff_runningmax[column1] = df_diff1[column1].cummax().to_frame(column1)
                df_diff_runningmin[column1] = df_diff1[column1].cummin().to_frame(column1)
                df_diff_movingaverage[column1] = df_diff1.rolling(window=movingaveragewindow).mean()
                df_diff_stdev[column1] = df_diff1.rolling(window=movingaveragewindow).std()
                i3 += 1
            df_diff_prices = df[columns].sub(df[column], axis=0)
            df_diff_betweenmaxmin = df_diff_runningmax[columns].sub(df_diff_runningmin[columns], axis=0)
            df_diff_runningpct = ( df_diff_prices - df_diff_runningmin ) / ( df_diff_runningmax - df_diff_runningmin)             
            
            df_diff_dollarized = df_dollarized[columns].sub(df_dollarized[column], axis=0)

            dict_pairdiff_prices[column] = df_diff_prices
            
            dict_pairdiff_runningmax[column] = df_diff_runningmax
            dict_pairdiff_runningmin[column] = df_diff_runningmin
            dict_pairdiff_betweenmaxmin[column] = df_diff_betweenmaxmin
            dict_pairdiff_runningpct[column] = df_diff_runningpct
            dict_pairdiff_dollarized[column] = df_diff_dollarized
            dict_pairdiff_movingaverage[column] = df_diff_movingaverage
            dict_pairdiff_standarddeviation[column] = df_diff_stdev
            i2 +=1
            if i2 >= 6:
                break
        print 'finished creating class dictionaries...'
        self.PairPricesDiffDictionary = dict_pairdiff_prices
        self.PairRunningMaxDiffDictionary = dict_pairdiff_runningmax
        self.PairRunningMinDiffDictionary = dict_pairdiff_runningmin
        self.PairBetweenMaxMinDiffDictionary = dict_pairdiff_betweenmaxmin
        self.PairRunningPctDiffDictionary = dict_pairdiff_runningpct
        self.PairDollarizedDiffDictionary = dict_pairdiff_dollarized
        self.PairMovingAverageDiffDictionary = dict_pairdiff_movingaverage
        self.PairMovingStdevDiffDictionary = dict_pairdiff_standarddeviation
        self.SymbolsList = columns

        return True
    
if __name__=='__main__':
    o = find(closepricesfilepath = 'C:\\Batches\\GitStuff\\$work\\closeprices_sample.csv', movingaveragewindow = 50)


