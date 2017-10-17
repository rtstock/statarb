#C:\Batches\GitStuff\$work\correlation_sample.csv
import pandas as pd
import numpy as np
class find:

    def set_SymbolsList(self,SymbolsList):
        self._SymbolsList = SymbolsList
    def get_SymbolsList(self):
        return self._SymbolsList
    SymbolsList = property(get_SymbolsList, set_SymbolsList)

    #PairPriceDiffsDictionary
    def set_PairPriceDiffsDictionary(self,PairPriceDiffsDictionary):
        self._PairPriceDiffsDictionary = PairPriceDiffsDictionary
    def get_PairPriceDiffsDictionary(self):
        return self._PairPriceDiffsDictionary
    PairPriceDiffsDictionary = property(get_PairPriceDiffsDictionary, set_PairPriceDiffsDictionary)
    
    def set_ClosePricesDataframe(self,ClosePricesDataframe):
        self._ClosePricesDataframe = ClosePricesDataframe
    def get_ClosePricesDataframe(self):
        return self._ClosePricesDataframe
    ClosePricesDataframe = property(get_ClosePricesDataframe, set_ClosePricesDataframe)
    
    def set_PairDollarizedDiffsDictionary(self,PairDollarizedDiffsDictionary):
        self._PairDollarizedDiffsDictionary = PairDollarizedDiffsDictionary
    def get_PairDollarizedDiffsDictionary(self):
        return self._PairDollarizedDiffsDictionary
    PairDollarizedDiffsDictionary = property(get_PairDollarizedDiffsDictionary, set_PairDollarizedDiffsDictionary)

    def set_PairAverageDiffsDictionary(self,PairAverageDiffsDictionary):
        self._PairAverageDiffsDictionary = PairAverageDiffsDictionary
    def get_PairAverageDiffsDictionary(self):
        return self._PairAverageDiffsDictionary
    PairAverageDiffsDictionary = property(get_PairAverageDiffsDictionary, set_PairAverageDiffsDictionary)

    def set_PairStdevDiffsDictionary(self,PairStdevDiffsDictionary):
        self._PairStdevDiffsDictionary = PairStdevDiffsDictionary
    def get_PairStdevDiffsDictionary(self):
        return self._PairStdevDiffsDictionary
    PairStdevDiffsDictionary = property(get_PairStdevDiffsDictionary, set_PairStdevDiffsDictionary)
    
    def __init__(self,
                 closepricesfilepath, movingaveragewindow):

        #self.PairAverageDiffsDictionary, columns = self.setclassdictionaries(closepricesfilepath)
        b = self.setclassdictionaries(closepricesfilepath = closepricesfilepath,movingaveragewindow = movingaveragewindow)
        
        #------- Testing
##        df_1a = self.PairPriceDiffsDictionary['A']
##        df_1b = self.PairAverageDiffsDictionary['A']
##        for idx,row in self.PairAverageDiffsDictionary['A']['AAL'].to_frame().iterrows():
##            print idx, row['AAL']
##            if idx > '2016-03-02':
##                stop
            
##        df_1c = self.PairStdevDiffsDictionary['A']
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
        
        #rowbegin = self.PairDollarizedDiffsDictionary.index[self.PairDollarizedDiffsDictionary.iloc[0]]
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
    def runbyticker(self,ticker):
        #print mydict
        import pandas as pd
        import numpy as np
        #dict_pairdiff = self.PairAverageDiffsDictionary
        
        ticker1 = ticker
        #df = self.PairAverageDiffsDictionary[ticker1]
        #print df
        df_close = self.ClosePricesDataframe
        df_pricediff = self.PairPriceDiffsDictionary[ticker1]
        df_ma = self.PairAverageDiffsDictionary[ticker1]
        df_stdev = self.PairStdevDiffsDictionary[ticker1]
        df_currdiffminusma = df_pricediff.sub(df_ma, axis=0)
        df_howmanystdevsout = df_currdiffminusma.div(df_stdev, axis=0)
        columns_ma = list(df_ma.columns.values)
        #print df_howmanystdevsout['AAL'].loc[df_howmanystdevsout['AAL'] >= 2.5]
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
                the_value = df_extreme.iloc[selected_opportunity][column]
                tradedate = df_extreme.iloc[selected_opportunity].name
                self.testone(ticker,column,tradedate,the_value)
                stop
##                df = df_close[ticker,column]
##                print df
##                df_shares1 = 10000.0 / df.iloc[[0]]
##                print 
        #df_found = df_howmanystdevsout.loc[df_howmanystdevsout >= 2.5]
        #print df_found
            
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
    def testone(self,tickerlong,tickershort,tradedate,the_value):
        print tickerlong,tickershort,tradedate,the_value
        df1a = self.ClosePricesDataframe
        df1a = df1a[(df1a.index >= tradedate)]
        df2 = pd.DataFrame(index=df1a.index.copy())
        print '----------------- ++++'
        df1a = df1a[[tickerlong,tickershort]]
        #print df
        
        columns = list(df1a.columns.values)
        print 'columns',columns
        df_shares1 = 10000.0 / df1a.iloc[[0]]
        print 'df_shares1',df_shares1
        print '--------------------------kkkk'
        df_blotter = df1a * df_shares1.loc[tradedate]
        if the_value < 0:
            sign_for_ticker_long = -1
            sign_for_ticker_short = 1
        else:
            sign_for_ticker_long = 1
            sign_for_ticker_short = -1
            
        for idx,row in df_blotter.iterrows():
            print 'a', idx, sign_for_ticker_long * row[tickerlong],sign_for_ticker_short * row[tickershort], ( sign_for_ticker_long * row[tickerlong] ) + ( sign_for_ticker_short * row[tickershort] )
            #if idx > '2016-03-02':
            #        break
        print '-------------------------------------------------'
##        for idx,row in df1a.iterrows():
##            print 'x',idx, row['A'],row['AAL']
##            #if idx > '2016-03-02':
##            #        break
        stop
        df_shares2 = df_shares1.append([df_shares1]*(len(df)-1),ignore_index=True)
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
        #dict_pairdiff = self.PairAverageDiffsDictionary
        
        ticker1 = ticker
        #df = self.PairAverageDiffsDictionary[ticker1]
        #print df
        df_close = self.ClosePricesDataframe
        df_pricediff = self.PairPriceDiffsDictionary[ticker1]
        df_ma = self.PairAverageDiffsDictionary[ticker1]
        df_stdev = self.PairStdevDiffsDictionary[ticker1]
        
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
            #for idx,v in df1.iterrows():
            #    print idx,v['value1'], v['value2'], v['value31'], v['value32'], v['value4']
            #if i >= 3:
            #    stop       

        #df = self.finddictionaryofpairdollarizeddiffs()
        #return df_final2

    def runbyticker_saved(self,ticker):
        #print mydict
        import pandas as pd
        import numpy as np
        dict_pairdiff_dollarized = self.PairDollarizedDiffsDictionary
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
            #for idx,v in df1.iterrows():
            #    print idx,v['value1'], v['value2'], v['value31'], v['value32'], v['value4']
            #if i >= 3:
            #    stop       

        #df = self.finddictionaryofpairdollarizeddiffs()
        #return df_final2
        
##    def finddictionaryofpairdollarizeddiffs(self,closepricesfilepath):
##        
##        print 'started def findpairstdev'
##        import pandas as pd
##        myfile = closepricesfilepath #'C:\Batches\GitStuff\$work\closeprices_sample.csv'
##        df = pd.read_csv(myfile)
##        df2 = df["Date"]
##        df.set_index("Date", drop=True, inplace=True)
##        
##        columns = list(df.columns.values)
##        
##        df_shares1 = 10000.0 / df.iloc[[0]]
##        
##        df_shares2 = df_shares1.append([df_shares1]*(len(df)-1),ignore_index=True)
##        df_shares3 = pd.concat([df2, df_shares2], axis=1)
##        df_shares3.set_index("Date", drop=True, inplace=True)
##
##        df_dollarized = df.multiply(df_shares3, axis=1)
##        
##        dict_pairdiff_dollarized = {}
##        
##        print 'started analysis...'
##
##        for column in columns:
##            df_diff = df_dollarized[columns].sub(df_dollarized[column], axis=0)
##            dict_pairdiff_dollarized[column] = df_diff
##        print 'finished.'
##        return dict_pairdiff_dollarized,columns

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
        columns = ['CA',     'CHD']
        df_shares1 = 10000.0 / df.iloc[[0]]
        #print df_shares1
        #stop
        df_shares2 = df_shares1.append([df_shares1]*(len(df)-1),ignore_index=True)
        df_shares3 = pd.concat([df2, df_shares2], axis=1)
        df_shares3.set_index("Date", drop=True, inplace=True)

        df_dollarized = df.multiply(df_shares3, axis=1)

        dict_pairdiff_prices = {}
        dict_pairdiff_dollarized = {}
        dict_pairdiff_movingaverage = {}
        dict_pairdiff_standarddeviation = {}
        #df['MA'] = df.rolling(window=5).mean()
        print 'started analysis...'
        
        
        
        i2 = 0
        for column in columns:
            df_diff_movingaverage = pd.DataFrame(index = df.index)
            df_diff_stdev = pd.DataFrame(index = df.index)
            print 'setclassdictionaries',column
            df_diff = df[columns].sub(df[column], axis=0)
            i3 = 0
            for column1 in columns:
                
                #if not column == column1:
                #print column,column1
                df_diff1 = df_diff[column1].to_frame(column1)
##                if df_diff_movingaverage == None:
##                    print 'got here 1'
##                    df_diff_movingaverage = df_diff1.rolling(window=10).mean()
##                    print df_diff_movingaverage
##                    print 'got here 2'
##                else:
##                    print 'got here 3'
                df_diff_movingaverage[column1] = df_diff1.rolling(window=movingaveragewindow).mean()
                
##                if column == 'A' and column1 == 'AAL':
##                    print 'A AAL xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
##                    #print df_diff1
##                    #print df_diff_movingaverage[column1]
##                    #stop
##                    df_x = pd.concat([df_diff1, df_diff_movingaverage[column1].to_frame('ma')], axis=1)
##                    #print df_x
##                    for idx,row in df_x.iterrows():
##                        print idx, row['AAL'],row['ma']
##                        if idx > '2016-03-02':
##                            break

##                if column1 == 'AAL':
##                    b = True
##                    i4 = 0
##                    for idx,row in df_diff.iterrows():
##                        print idx,row[column1],df_diff_movingaverage[column1].loc[idx]
##                        if idx >= '2016-03-02':
##                            print 'here'
##                            stop
##                        i4 += 1
##                    print df_diff1
##                    print df_diff_movingaverage[column1]
##                    stop

                df_diff_stdev[column1] = df_diff1.rolling(window=movingaveragewindow).std()
                #if i >= 3:
                #    print df_diff_movingaverage
                #    stop
                i3 += 1
            #print df_diff_movingaverage
            #print df_diff_stdev
            df_diff_prices = df[columns].sub(df[column], axis=0)
            df_diff_dollarized = df_dollarized[columns].sub(df_dollarized[column], axis=0)
            
            dict_pairdiff_prices[column] = df_diff_prices
            dict_pairdiff_dollarized[column] = df_diff_dollarized
            dict_pairdiff_movingaverage[column] = df_diff_movingaverage
##            print 'here?'
##            if column == 'A':
##                if 1 == 1:
##                    print 'A AAL YYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
##                    #print df_diff1
##                    #print df_diff_movingaverage[column1]
##                    #stop
##                    #df_x = pd.concat([df_diff1, df_diff_movingaverage[column1].to_frame('ma')], axis=1)
##                    #print df_x
##                    for idx,row in dict_pairdiff_movingaverage['A']['AAL'].to_frame().iterrows():
##                        print 'A', idx, row['AAL']
##                        if idx > '2016-03-02':
##                            break
##            
            
            dict_pairdiff_standarddeviation[column] = df_diff_stdev
            #print df_diff
            #stop
            i2 +=1
            if i2 >= 5:
                break
        print 'finished.'

        self.PairPriceDiffsDictionary = dict_pairdiff_prices
        self.PairDollarizedDiffsDictionary = dict_pairdiff_dollarized
        self.PairAverageDiffsDictionary = dict_pairdiff_movingaverage
        self.PairStdevDiffsDictionary = dict_pairdiff_standarddeviation
        self.SymbolsList = columns
##        if 1 == 1:
##            print 'here?'
##            if 2 == 2:
##                if 1 == 1:
##                    print 'A AAL zzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
##                    #print df_diff1
##                    #print df_diff_movingaverage[column1]
##                    #stop
##                    #df_x = pd.concat([df_diff1, df_diff_movingaverage[column1].to_frame('ma')], axis=1)
##                    #print df_x
##                    for idx,row in dict_pairdiff_movingaverage['A']['AAL'].to_frame().iterrows():
##                        print 'A', idx, row['AAL']
##                        if idx > '2016-03-02':
##                            break
        return True
    
if __name__=='__main__':
    o = find(closepricesfilepath = 'C:\\Batches\\GitStuff\\$work\\closeprices_sample.csv', movingaveragewindow = 50)


