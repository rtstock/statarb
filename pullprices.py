#import sys
import pandas as pd
import numpy as np
import config
import os
import mytools
class pull:
    
    def set_StockHistoryDataframe(self,StockHistoryDataframe):
        self._StockHistoryDataframe = StockHistoryDataframe
    def get_StockHistoryDataframe(self):
        return self._StockHistoryDataframe
    StockHistoryDataframe = property(get_StockHistoryDataframe, set_StockHistoryDataframe)

    def set_ClosePricesDataframe(self,ClosePricesDataframe):
        self._ClosePricesDataframe = ClosePricesDataframe
    def get_ClosePricesDataframe(self):
        return self._ClosePricesDataframe
    ClosePricesDataframe = property(get_ClosePricesDataframe, set_ClosePricesDataframe)

    def set_AdjClosePricesDataframe(self,AdjClosePricesDataframe):
        self._AdjClosePricesDataframe = AdjClosePricesDataframe
    def get_AdjClosePricesDataframe(self):
        return self._AdjClosePricesDataframe
    AdjClosePricesDataframe = property(get_AdjClosePricesDataframe, set_AdjClosePricesDataframe)

    def set_SaveCSVPathName(self,SaveCSVPathName):
        self._SaveCSVPathName = SaveCSVPathName
    def get_SaveCSVPathName(self):
        return self._SaveCSVPathName
    SaveCSVPathName = property(get_SaveCSVPathName, set_SaveCSVPathName)


    def __init__(self,
                 ):
        print 'initialized pullprices'

    def setclassdataframes(self,symbols,fromdate,todate):
        print 'setting class dataframes'
        df_good,df_missing = self.stockhistoryasdataframe(symbols,fromdate,todate)
        self.StockHistoryDataframe = df_good
        #retval = o.savetocsv(df_good)
        #print 'save location:',retval
        #df_good = stockhistorynobackfilltodataframeusingcache('AAPL','2017-07-01','2017-08-05')
        #print df_good
        df_closeprices, df_adjcloseprices = self.getpricesasdataframes()
        self.ClosePricesDataframe = df_closeprices
        self.AdjClosePricesDataframe = df_adjcloseprices
        retval = self.savetocsv(df_closeprices,'closeprices')
        print 'save location closeprices :',retval
        retval = self.savetocsv(df_adjcloseprices,'adjcloseprices')
        self.SaveCSVPathName = retval
        print 'save location adjcloseprices :',retval

        #for index, row in df_good.iterrows():
        #    print row['Ticker'], row['
        
    def make_sure_path_exists(self,path):
        import errno
        import os
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def stockhistory_bad(self,symbols,fromdate,todate):
        from pandas_datareader import data, wb
        chunks = [symbols[x:x+100] for x in xrange(0, len(symbols), 100)]
        #chunks = [symbols[x:x+5] for x in xrange(0, len(symbols), 5)]
        print 'chunks', chunks[0]
        df_result = data.DataReader(chunks[0],  "yahoo", fromdate,todate)
        on = False
        for c in chunks:
            print 'chunks', c
            if on == True:
                hist = data.DataReader(c,  "yahoo", fromdate,todate)
                df_result.append(hist, ignore_index=True)
                
            on = True
        return df_result
        #print(hist["Adj Close"])


    def stockhistory(self,symbols,fromdate,todate):
        from pandas_datareader import data, wb

        try:
            hist = data.DataReader(symbols,  "yahoo", fromdate, todate)
            print hist
            return hist
        except Exception as e: 
            print 'there was an error:', e
            return None
        #print(hist["Adj Close"])

    def stockhistoryasdataframe(self,symbols,fromdate,todate):
        import numpy as np
        import pandas as pd
        chunks = [symbols[x:x+100] for x in xrange(0, len(symbols), 100)]
        #chunks = [symbols[x:x+5] for x in xrange(0, len(symbols), 5)]
        print 'pulling prices for chunk', 0, chunks[0]
        df_good,df_missing = self.stockhistoryasdataframeindividual(chunks[0],fromdate,todate)
        df_good.reindex()

        on = False
        i = 0
        for c in chunks:
            i +=1
            if on == True:
                print 'pulling prices for chunk',i, 'total of', len(c), 'symbol'
                h_good,h_missing = self.stockhistoryasdataframeindividual(c,fromdate,todate)
                #print 'h_good',h_good
                df_good = df_good.append(h_good, ignore_index=True)
                df_missing = df_missing.append(h_missing, ignore_index=True)
            on = True
        print '--- df_good ----'
        print 'length of pricespulled',len(df_good)
        print 'length of pricespulled missing',len(df_missing)
        return df_good,df_missing
    
    def getpricesasdataframes(self,):
        df0 =self.StockHistoryDataframe
        lst_a= df0['Date'].unique()
        lst_a_sorted = sorted(lst_a)
        df1_close = pd.DataFrame({'date':lst_a_sorted})
        df1_close.set_index(['date'],inplace=True,drop=True)

        df1_adjclose = pd.DataFrame({'date':lst_a_sorted})
        df1_adjclose.set_index(['date'],inplace=True,drop=True)

        lst_b= df0['Ticker'].unique()
        for ticker in lst_b:
            df3 = df0[(df0['Ticker'] == ticker)]
            df3.set_index(['Date'],inplace=True,drop=True)
            df4_close = df3['Close'].to_frame(ticker)
            df4_adjclose = df3['Adj Close'].to_frame(ticker)
            #print df3
            df1_close = pd.concat([df1_close, df4_close], axis=1)
            df1_adjclose = pd.concat([df1_adjclose, df4_adjclose], axis=1)
            df1_close.index.rename('Date', inplace=True)
            df1_adjclose.index.rename('Date', inplace=True)
            #print df3
        return df1_close,df1_adjclose
    def savetocsv(self,mydataframe,rootforfilename = 'unnamed'):
        try:
            date14 = mytools.mystrings().ConvertDatetime14() 
            cachedfilepathname = os.path.join(config.mycachefolder,date14+' '+rootforfilename+'.csv')
            self.make_sure_path_exists(config.mycachefolder)
            mydataframe.to_csv(cachedfilepathname,columns=(list(mydataframe.columns.values)))
            return cachedfilepathname
        except Exception as e:
            print 'error in pullprices savetocsv', e
            return ''
    def stockhistoryasdataframeindividual(self,symbols,fromdate,todate):
        import numpy as np
        import pandas as pd
        p = self.stockhistory(symbols,fromdate,todate)
        list_of_dicts = []
        list_of_missing = []
        try:
            for d, item in p.swapaxes(0, 1).iteritems():
                for t,x in item.iteritems():
                    #print x
                    if np.isnan(x['Adj Close']) == True:
                        list_of_missing.append({'Date':d, 'Ticker':t,'Adj Close':x['Adj Close'],'Close':x['Close']})
                    else:
                        list_of_dicts.append({'Date':d, 'Ticker':t,'Adj Close':x['Adj Close'],'Close':x['Close']})
        except Exception as e:
            print(e)
        df_good = pd.DataFrame(list_of_dicts)
        df_missing = pd.DataFrame(list_of_missing)
        return df_good, df_missing

    def stockhistoryandmissingasdataframe_old(symbols,fromdate,todate):
        p = stockhistory(symbols,fromdate,todate)

        dict_prices = {}
        list_of_dicts = []
        list_of_missing = []
        import numpy as np
        for d, item in p.swapaxes(0, 1).iteritems():
            for t,x in item.iteritems():
                if np.isnan(x['Adj Close']) == True:
                    list_of_missing.append({'Date':d, 'Ticker':t,'Adj Close':x['Adj Close']})
                else:
                    list_of_dicts.append({'Date':d, 'Ticker':t,'Adj Close':x['Adj Close']})
        
        import pandas as pd
        df_good = pd.DataFrame(list_of_dicts)
        df_good.set_index(['Date','Ticker'],inplace=True,drop=False)
        print df_good
        df_missing = pd.DataFrame(list_of_missing)
        print df_missing
        df_missing.set_index(['Date','Ticker'],inplace=True,drop=False)
        array_missing = np.unique(df_missing[['Ticker']])
        return df_good, array_missing

        
    def stockhistoryasdataframe_old(symbols,fromdate,todate):
        import pandas as pd
        df_good1, ls_missing1 = stockhistoryandmissingasdataframe(symbols,fromdate,todate)
        
        print ls_missing1
        if len(ls_missing1) > 0:
            df_good2, ls_missing2 = stockhistoryandmissingasdataframe(ls_missing1,fromdate,todate)
            print df_good2
            result = pd.concat([df_good1, df_good2], ignore_index=True)
        else:
            result = df_good1
        return result

    def stockhistorybackfilledtodictionary(symbol,fromdate,todate):
        
        from pandas_datareader import data, wb
        from datetime import datetime, timedelta
        
        hist = data.DataReader(symbol,  "yahoo", fromdate,todate)

        date_format = "%Y-%m-%d"
        d = datetime.strptime(fromdate, date_format)
        delta = timedelta(days=1)
        last_adjclose = 'NaN'
        
        dictAdjClose = {}    
        
        while d <= datetime.strptime(todate, date_format):
            #print(d.strftime(date_format))
            d_string = d.strftime(date_format)
            if d_string in hist.index:
                last_adjclose = hist.ix[d_string]['Adj Close']
                print(d_string,last_adjclose)
            else:
                print(d_string,'nothing',last_adjclose)
            dictAdjClose[d_string] = [('AdjClose',last_adjclose)]
            d += delta

        return dictAdjClose

    def stockhistorybackfilledtodictionaryofstockhistoryinstances(symbol,fromdate,todate):
        
        from pandas_datareader import data, wb
        from datetime import datetime, timedelta
        import structureforstockhistoryinstance
        hist = data.DataReader(symbol,  "yahoo", fromdate,todate)
        #print(hist)
        date_format = "%Y-%m-%d"
        d = datetime.strptime(fromdate, date_format)
        delta = timedelta(days=1)


        last_open = 'NaN'
        last_high = 'NaN'
        last_low = 'NaN'
        last_close = 'NaN'
        last_adjclose = 'NaN'
        last_volume = 'NaN'
        backfilled = 'NaN'
        
        dictAdjClose = {}    
        
        while d <= datetime.strptime(todate, date_format):
            stockInstance = structureforstockhistoryinstance.Framework()
            
            stockInstance.symbol = symbol
            
            d_string = d.strftime(date_format)
            if d_string in hist.index:
                last_open = hist.ix[d_string]['Open']
                last_high = hist.ix[d_string]['High']
                last_low = hist.ix[d_string]['Low']
                last_close = hist.ix[d_string]['Close']
                last_adjclose = hist.ix[d_string]['Adj Close']
                last_volume = hist.ix[d_string]['Volume']
                backfilled = 0
                #print(d_string,last_adjclose)
            else:
                backfilled = 1
                #print(d_string,'nothing',last_adjclose)
                
                
            stockInstance.open = last_open
            stockInstance.high = last_high
            stockInstance.low = last_low
            stockInstance.close = last_close
            stockInstance.adjclose = last_adjclose
            stockInstance.volume = last_volume
            stockInstance.backfilled = backfilled
            
            dictAdjClose[d_string] = stockInstance
            d += delta

        return dictAdjClose



    def test_builddataframe():
        import pandas as pd
        import numpy as np
        
        df = pd.DataFrame({'a':np.random.randn(5),
                            'b':np.random.randn(5),
                            'c':np.random.randn(5),
                            'd':np.random.randn(5)})
        cols_to_keep = ['a', 'c', 'd']
        dummies = ['d']
        not_dummies = [x for x in cols_to_keep if x not in dummies]
        data = df[not_dummies]
        print(data)


    def test_builddataframe2(symbol,fromdate,todate):
        import pandas as pd
        import numpy as np
        #from pandas_datareader import data, wb
        from datetime import datetime, timedelta
        

        #print(hist)
        date_format = "%Y-%m-%d"
        d = datetime.strptime(fromdate, date_format)
        delta = timedelta(days=1)

        idates = 0
        while d <= datetime.strptime(todate, date_format):
            idates = idates + 1
            d += delta
        print(idates)
        dfnew = pd.DataFrame({'a':np.random.randn(idates),
                        'b':np.random.randn(idates),
                        'c':np.random.randn(idates),
                        'd':np.random.randn(idates)})
        print(dfnew)                 
    #    hist = data.DataReader(symbol,  "yahoo", fromdate,todate)
    #    
    #    last_open = 'NaN'
    #    last_high = 'NaN'
    #    last_low = 'NaN'
    #    last_close = 'NaN'
    #    last_adjclose = 'NaN'
    #    last_volume = 'NaN'
    #    backfilled = 'NaN'
    #    
    #    dictAdjClose = {}    

    def stockhistorybackfilledtodatframeofstockhistoryinstancesusingcache(symbol,fromdate,todate):
        print('initialized pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances')
        import pandas as pd
        #import numpy as np
        from pandas_datareader import data, wb
        from datetime import datetime, timedelta
        
        import config
        mycachefolder = config.mycachefolder
        import mytools
        mytools.general().make_sure_path_exists(mycachefolder)
        #dfnew.to_csv(mycachefolder + '\\stockhistorybackfilled '+ symbol '.csv',columns=(  'Open',   'High',    'Low',  'Close',    'Volume',  'Adj Close', 'Back Filled'))
        cachedfilepathname = mycachefolder + '\\stockhistorybackfilled '+ symbol + ' ' + fromdate+ ' ' + todate + '.csv'
        import os
        if os.path.isfile(cachedfilepathname):
            print('--------------------------')
            #print('pullprices.stockhistorybackfilledtodatframeofstockhistoryinstancesusingcache')
            print('   Found cached file:  '+cachedfilepathname)
            dfnew = pd.read_csv(cachedfilepathname,index_col=0)
        else:
            print('Getting new file:'+cachedfilepathname)
            date_format = "%Y-%m-%d"
        
            delta = timedelta(days=1)
        
            todate_date = datetime.strptime(todate, date_format)
            fromdate_date = datetime.strptime(fromdate, date_format)
            
            
        
            idates = 0
            d = datetime.strptime(fromdate, date_format)
            while d <= todate_date:
                idates = idates + 1
                d += delta
                
            # ##############
            # print(idates)
        
            #todays_date = datetime.datetime.now().date()
            index = pd.date_range(fromdate_date, periods=idates, freq='D')
            columns = [
             'Open',   'High',    'Low',  'Close',    'Volume',  'Adj Close', 'Back Filled',     
            ]
            dfnew = pd.DataFrame(index=index, columns=columns)
            dfnew = dfnew.fillna('NaN') # with 0s rather than NaNs
            
            # ############
            # print(dfnew)                 
            
            hist = data.DataReader(symbol,  "yahoo", fromdate,todate)
            
            # #########
            # print(hist)
            
            last_open = 'NaN'
            last_high = 'NaN'
            last_low = 'NaN'
            last_close = 'NaN'
            last_adjclose = 'NaN'
            last_volume = 'NaN'
            backfilled = 'NaN'
            
            d = datetime.strptime(fromdate, date_format)
            while d <= todate_date:
                d_string = d.strftime(date_format)
                
                #print(d_string)
                if d_string in hist.index:
                    last_open = hist.ix[d_string]['Open']
                    last_high = hist.ix[d_string]['High']
                    last_low = hist.ix[d_string]['Low']
                    last_close = hist.ix[d_string]['Close']
                    last_volume = hist.ix[d_string]['Volume']
                    last_adjclose = hist.ix[d_string]['Adj Close']
                    backfilled = 0
                    #print(d_string,last_adjclose)
                else:
                    backfilled = 1
                    #print(d_string,'nothing',last_adjclose)
                    
                
                dfnew.ix[d_string]['Open'] = last_open 
                dfnew.ix[d_string]['High'] = last_high 
                dfnew.ix[d_string]['Low'] = last_low
                dfnew.ix[d_string]['Close'] = last_close        
                dfnew.ix[d_string]['Volume'] = last_volume
                dfnew.ix[d_string]['Adj Close'] = last_adjclose
                dfnew.ix[d_string]['Back Filled'] = backfilled
                
                d += delta
            
                
            dfnew.to_csv(cachedfilepathname,columns=('Open',   'High',    'Low',  'Close',    'Volume',  'Adj Close', 'Back Filled'))
            
        
        #print(dfnew)
        return dfnew




    def stockhistorybackfilledtodatframeofstockhistoryinstances(symbol,fromdate,todate):
        print('initialized pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances')
        import pandas as pd
        #import numpy as np
        from pandas_datareader import data, wb
        from datetime import datetime, timedelta
        

        #print(hist)
        date_format = "%Y-%m-%d"

        delta = timedelta(days=1)

        todate_date = datetime.strptime(todate, date_format)
        fromdate_date = datetime.strptime(fromdate, date_format)
        
        

        idates = 0
        d = datetime.strptime(fromdate, date_format)
        while d <= todate_date:
            idates = idates + 1
            d += delta
            
        # ##############
        # print(idates)

        #todays_date = datetime.datetime.now().date()
        index = pd.date_range(fromdate_date, periods=idates, freq='D')
        columns = [
         'Open',   'High',    'Low',  'Close',    'Volume',  'Adj Close', 'Back Filled',     
        ]
        dfnew = pd.DataFrame(index=index, columns=columns)
        dfnew = dfnew.fillna('NaN') # with 0s rather than NaNs
        
        # ############
        # print(dfnew)                 
        
        hist = data.DataReader(symbol,  "yahoo", fromdate,todate)
        
        # #########
        # print(hist)
        
        last_open = 'NaN'
        last_high = 'NaN'
        last_low = 'NaN'
        last_close = 'NaN'
        last_adjclose = 'NaN'
        last_volume = 'NaN'
        backfilled = 'NaN'
        
        d = datetime.strptime(fromdate, date_format)
        while d <= todate_date:
            d_string = d.strftime(date_format)
            
            #print(d_string)
            if d_string in hist.index:
                last_open = hist.ix[d_string]['Open']
                last_high = hist.ix[d_string]['High']
                last_low = hist.ix[d_string]['Low']
                last_close = hist.ix[d_string]['Close']
                last_volume = hist.ix[d_string]['Volume']
                last_adjclose = hist.ix[d_string]['Adj Close']
                backfilled = 0
                #print(d_string,last_adjclose)
            else:
                backfilled = 1
                #print(d_string,'nothing',last_adjclose)
                
            
            dfnew.ix[d_string]['Open'] = last_open 
            dfnew.ix[d_string]['High'] = last_high 
            dfnew.ix[d_string]['Low'] = last_low
            dfnew.ix[d_string]['Close'] = last_close        
            dfnew.ix[d_string]['Volume'] = last_volume
            dfnew.ix[d_string]['Adj Close'] = last_adjclose
            dfnew.ix[d_string]['Back Filled'] = backfilled
            
            d += delta
        
        #print(dfnew)
        return dfnew
        
    def stock_dataframe(symbol):
        """ 
        gets last traded price from yahoo for given security
        """
        cols = ['PE', 'change_pct', 'last', 'short_ratio', 'time']
        try:
            import pandas.io.data as pd 
            
            df = pd.get_quote_yahoo(symbol)
            #print(df)
            result = pd.DataFrame(df, columns=cols)
            return result
        except:
            result = pd.DataFrame(columns=cols)
            return
    def stock(symbol):
        """ 
        gets last traded price from yahoo for given security
        """        
        import pandas.io.data as pd 
        
        df = pd.get_quote_yahoo(symbol)
        #print(df)
        
        cols = ['PE', 'change_pct', 'last', 'short_ratio', 'time']
        result = pd.DataFrame(df, columns=cols)
        return result.iloc[0]['last']
        
    def options(symbol,expirationdate,pathtoexportfile,showresults=0):
        import lxml.html
        import calendar
        #import os

        #################################
        try:
            outstrings = {}
            outstrings[len(outstrings)] = "pullprices: trying"

            #total = len(sys.argv)
            #cmdargs = str(sys.argv)
            #print ("The total numbers of args passed to the script: %d " % total)
            #print ("Args list: %s " % cmdargs)
            # Pharsing args one by one 
            #print ("Script name: %s" % str(sys.argv[0]))

            #import inspect
            from datetime import datetime            
        
            #root = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\data"
            import os
            root = os.path.join(pathtoexportfile,symbol)
            
            #print ("Root: %s" % root)
            outstrings[len(outstrings)] = "Symbol: %s" % str(symbol)
            outstrings[len(outstrings)] = "Expiration: %s" % str(expirationdate)
            
            s_symbol  = str(symbol)
            d_expiration  = str(expirationdate)
        
            dt      = datetime.strptime(d_expiration, '%Y-%m-%d')
            ym      = calendar.timegm(dt.utctimetuple())
            url     = 'http://finance.yahoo.com/q/op?s=%s&date=%s' % (s_symbol, ym,)
            doc     = lxml.html.parse(url)
            table   = doc.xpath('//table[@class="details-table quote-table Fz-m"]/tbody/tr')
            
            rows    = []        
            for tr in table:
                d = [td.text_content().strip().replace(',','') for td in tr.xpath('./td')]
                rows.append(d)
            
            import csv
            
            length = len(rows[0])
            
            import datetime
            i = datetime.datetime.now()
            
            #print ("Current date & time = %s" % i)
            #print ("Date and time in ISO format = %s" % i.isoformat() )
            
            dateString = i.strftime('%Y%m%d%H%M%S')
            
            ##############################################
    #        import shutil
    #        shutil.rmtree(root, ignore_errors=True)
            ##############################################
            
            wildcardstringforfilestodelete = os.path.join(root,"Options " + s_symbol + ' ' + d_expiration + '*')        
            #print('checking for the existence of: ' + wildcardstringforfilestodelete)
            import glob
            for filename in glob.glob(wildcardstringforfilestodelete) :
                print('removing....  ' + filename)
                os.remove( filename )        
            
            make_sure_path_exists(root)
            # make sure root is clear of all file
            output = os.path.join(root,"Options " + s_symbol + ' ' + d_expiration + ' ' + dateString + '.csv')
            #output = root + "\Options " + s_symbol + ' ' + d_expiration + ' ' + dateString + '.csv'
            
            outstrings[len(outstrings)] = 'Output File: ' + output
            
            stockprice=stock(symbol)        
            
            with open(output, 'w') as test_file:
                csv_writer = csv.writer(test_file, lineterminator = '\n')
                for y in range(length):
                    csv_writer.writerow([x[y] for x in rows])
                csv_writer.writerow([stockprice for x in rows])
        #################################
        except Exception as e:
            print("pullprices: There was a problem with this one......................................................pullprices")
            print("pullprices: ",str(e))
        else:
            outstrings = ("pullprices: Success")
        finally:
            if showresults == 1:
                for sout in outstrings:
                    print(sout)
            #print("pullprices: Finally")
        #################################

    def options_to_dataframe(symbol,expirationdate,showresults=0):
        import lxml.html
        import calendar
        #import os

        #################################
        try:
            outstrings = {}
            outstrings[len(outstrings)] = "pullprices: trying"

            #total = len(sys.argv)
            #cmdargs = str(sys.argv)
            #print ("The total numbers of args passed to the script: %d " % total)
            #print ("Args list: %s " % cmdargs)
            # Pharsing args one by one 
            #print ("Script name: %s" % str(sys.argv[0]))

            #import inspect
            from datetime import datetime            
        
            #root = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\data"
            #import os
            #root = os.path.join(pathtoexportfile,symbol)
            
            #print ("Root: %s" % root)
            outstrings[len(outstrings)] = "Symbol: %s" % str(symbol)
            outstrings[len(outstrings)] = "Expiration: %s" % str(expirationdate)
            
            s_symbol  = str(symbol)
            d_expiration  = str(expirationdate)
        
            dt      = datetime.strptime(d_expiration, '%Y-%m-%d')
            ym      = calendar.timegm(dt.utctimetuple())
            url     = 'http://finance.yahoo.com/q/op?s=%s&date=%s' % (s_symbol, ym,)
            doc     = lxml.html.parse(url)
            table   = doc.xpath('//table[@class="details-table quote-table Fz-m"]/tbody/tr')
            
            rows    = []        
            rows.append(['strike','optionsymbol','last','bid','ask','change','pctchange','volume','openinterest','impliedvolatility'])
            print('pullprices options_to_dataframe len of table',len(table))
            if len(table) > 0:
                for tr in table:
                    #print(tr)
                    d = [td.text_content().strip().replace(',','') for td in tr.xpath('./td')]
                    rows.append(d)
            
            stockprice=stock(symbol)
            headers = rows.pop(0)
            
            import pandas as pd
            try:
                df = pd.DataFrame(rows, columns=headers)
                #print('got here')
                #import numpy as np
                df['stockprice'] = stockprice
            except:
                import numpy as np
                #rows.append(['strike','optionsymbol','last','bid','ask','change','pctchange','volume','openinterest','impliedvolatility'])
                df=pd.DataFrame(np.zeros(0,dtype=[
                    ('strike', 'a50')
                    ,  ('optionsymbol', 'a50')
                    ,  ('last', 'f2')
                    ,  ('ask', 'f2')
                    ,  ('change', 'f2')
                    ,  ('pctchange', 'f2')
                    ,  ('volume', 'f2')
                    ,  ('openinterest', 'f2')
                    ,  ('impliedvolatility', 'a20')
                    ]))
                #df = pd.DataFrame(rows, columns=headers)            
                print('pullprices options_to_dataframe could not create df',symbol,expirationdate)

            return df        
            print(rows.count,rows[0],stockprice)
            
        #################################
        except Exception as e:
            print("pullprices: There was a problem with this one......................................................pullprices")
            print("pullprices: ",str(e))
        else:
            outstrings = ("pullprices: Success")
        finally:
            if showresults == 1:
                for sout in outstrings:
                    print(sout)
            #print("pullprices: Finally")
        #################################


    def stockhistorynobackfilltodataframeusingcache(symbol,fromdate,todate):
        print('--------------------------')
        print('Initialized pullprices.stockhistorydailytodataframeusingcache')
        import pandas as pd
        #import numpy as np
        from pandas_datareader import data, wb
        #from datetime import datetime, timedelta
        
        import config
        mycachefolder = config.mycachefolder
        import mytools
        mytools.general().make_sure_path_exists(mycachefolder)
        
        cachedfilepathname = mycachefolder + '\\stockhistorynobackfill '+ symbol + ' ' + fromdate+ ' ' + todate + '.csv'
        import os
        if os.path.isfile(cachedfilepathname):
            
            print('   Found cached file:  '+cachedfilepathname)
            df_hist = pd.read_csv(cachedfilepathname,index_col=0)
        else:
            print('   Getting new file:'+cachedfilepathname)
            df_hist = data.DataReader(symbol,  "yahoo", fromdate,todate)
            df_hist.to_csv(cachedfilepathname,columns=('Open',   'High',    'Low',  'Close',    'Volume',  'Adj Close'))

        
        return df_hist


if __name__=='__main__':
    #options(sys.argv[1],sys.argv[2],sys.argv[3])
    #df = stockhistorynobackfilltodataframeusingcache('AAPL','2014-01-01','2015-08-05')

##<<<<<<< HEAD
##    symbols = ['GOOGL',
##                            'FB',
##                            'MSFT',
##                            'LRCX',
##                            'EVR',
##                            'MASI',
##                            'CELG',
##                            'AOS',
##                            'LPX',
##                            'MRK',
##                            'EVR',
##                            'JNJ',
##                            'INTC',
##                            'GOLD',
##                            'LMT',
##                            'RTN',
##                            'BP',
##                            'T',
##                            'HSBC',
##                            'THO'
##                            ]

    #symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT', 'AMD', 'AME', 'AMG', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANDV', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APC', 'APD', 'APH', 'ARE', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AYI', 'AZO', 'BA', 'BAC', 'BAX', 'BBT', 'BBY', 'BCR', 'BDX', 'BEN', 'BF.B', 'BHF', 'BHGE', 'BIIB', 'BK', 'BLK', 'BLL', 'BMY', 'BRK.B', 'BSX', 'BWA', 'BXP', 'C', 'CA', 'CAG', 'CAH', 'CAT', 'CB', 'CBG', 'CBOE', 'CBS', 'CCI', 'CCL', 'CDNS', 'CELG', 'CERN', 'CF', 'CFG', 'CHD', 'CHK', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COG', 'COH', 'COL', 'COO', 'COP', 'COST', 'COTY', 'CPB', 'CRM', 'CSCO', 'CSRA', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'D', 'DAL', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLPH', 'DLR', 'DLTR', 'DOV', 'DPS', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DWDP', 'DXC', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'EQT', 'ES', 'ESRX', 'ESS', 'ETFC', 'ETN', 'ETR', 'EVHC', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FL', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOX', 'FOXA', 'FRT', 'FTI', 'FTV', 'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HLT', 'HOG', 'HOLX', 'HON', 'HP', 'HPE', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KEY', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH', 'LKQ', 'LLL', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MA', 'MAA', 'MAC', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'MYL', 'NAVI', 'NBL', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWS', 'NWSA', 'O', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PCAR', 'PCG', 'PCLN', 'PDCO', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'PYPL', 'Q', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RHT', 'RJF', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCG', 'SCHW', 'SEE', 'SHW', 'SIG', 'SJM', 'SLB', 'SLG', 'SNA', 'SNI', 'SNPS', 'SO', 'SPG', 'SPGI', 'SPLS', 'SRCL', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDG', 'TEL', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSS', 'TWX', 'TXN', 'TXT', 'UA', 'UAA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT', 'WBA', 'WDC', 'WEC', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRK', 'WU', 'WY', 'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']
    symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL', ]
    print 'number of symbols',len(symbols)

    o = pull()
    o.setclassdataframes(symbols,'2015-01-01','2017-12-31')
    print o.ClosePricesDataframe
##=======
##    symbols = ['GOOGL',
##                            'FB',
##                            'MSFT',
##                            'LRCX',
##                            'EVR',
##                            'MASI',
##                            'CELG',
##                            'AOS',
##                            'LPX',
##                            'MRK',
##                            'EVR',
##                            'JNJ',
##                            'INTC',
##                            'GOLD',
##                            'LMT',
##                            'RTN',
##                            'BP',
##                            'T',
##                            'HSBC',
##                            'THO'
##                            ]

    #symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT', 'AMD', 'AME', 'AMG', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANDV', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APC', 'APD', 'APH', 'ARE', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AYI', 'AZO', 'BA', 'BAC', 'BAX', 'BBT', 'BBY', 'BCR', 'BDX', 'BEN', 'BF.B', 'BHF', 'BHGE', 'BIIB', 'BK', 'BLK', 'BLL', 'BMY', 'BRK.B', 'BSX', 'BWA', 'BXP', 'C', 'CA', 'CAG', 'CAH', 'CAT', 'CB', 'CBG', 'CBOE', 'CBS', 'CCI', 'CCL', 'CDNS', 'CELG', 'CERN', 'CF', 'CFG', 'CHD', 'CHK', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COG', 'COH', 'COL', 'COO', 'COP', 'COST', 'COTY', 'CPB', 'CRM', 'CSCO', 'CSRA', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'D', 'DAL', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLPH', 'DLR', 'DLTR', 'DOV', 'DPS', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DWDP', 'DXC', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'EQT', 'ES', 'ESRX', 'ESS', 'ETFC', 'ETN', 'ETR', 'EVHC', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FL', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOX', 'FOXA', 'FRT', 'FTI', 'FTV', 'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HLT', 'HOG', 'HOLX', 'HON', 'HP', 'HPE', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KEY', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH', 'LKQ', 'LLL', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MA', 'MAA', 'MAC', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'MYL', 'NAVI', 'NBL', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWS', 'NWSA', 'O', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PCAR', 'PCG', 'PCLN', 'PDCO', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'PYPL', 'Q', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RHT', 'RJF', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCG', 'SCHW', 'SEE', 'SHW', 'SIG', 'SJM', 'SLB', 'SLG', 'SNA', 'SNI', 'SNPS', 'SO', 'SPG', 'SPGI', 'SPLS', 'SRCL', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDG', 'TEL', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSS', 'TWX', 'TXN', 'TXT', 'UA', 'UAA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT', 'WBA', 'WDC', 'WEC', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRK', 'WU', 'WY', 'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']
    #df_good,df_missing = o.stockhistoryasdataframe(symbols,'2017-07-01','2017-08-05')
#    print o.ClosePricesDataframe
    #df_good = stockhistorynobackfilltodataframeusingcache('AAPL','2017-07-01','2017-08-05')
    #print df_good
    #for index, row in df_good.iterrows():
    #    print row['Ticker'], row['
#>>>>>>> b7bf7cd6348fa615ea2080131e7e8c7b5e1dba54
                  
    
