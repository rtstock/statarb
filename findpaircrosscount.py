#C:\Batches\GitStuff\$work\correlation_sample.csv
import pandas as pd
class find:
    
    def set_PairDollarizedDiffsDataframe(self,PairDollarizedDiffsDataframe):
        self._PairDollarizedDiffsDataframe = PairDollarizedDiffsDataframe
    def get_PairDollarizedDiffsDataframe(self):
        return self._PairDollarizedDiffsDataframe
    PairDollarizedDiffsDataframe = property(get_PairDollarizedDiffsDataframe, set_PairDollarizedDiffsDataframe)
    
    def __init__(self,
                 closepricesfilepath):
        
        self.PairDollarizedDiffsDataframe, columns = self.findpairdollarizeddiffsasdataframe(closepricesfilepath)
        i = 0
        for column in columns:
            print 'Doing',column, i, 'of',len(columns)
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
        df_pairdollarizeddiff = self.PairDollarizedDiffsDataframe
        ticker1 = ticker
        df = df_pairdollarizeddiff[ticker1]
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
            #df1['cross'] = np.where(  np.logical_or(np.logical_and(df1['value2']>0,df1['value1']<0), np.logical_and(df1['value1']>0,df1['value2']<0)),'yes', 'no')
            #df1['cross'] = np.where(  abs(df1['value1'])>0,df1['value1']<0), np.logical_and(df1['value1']>0,df1['value2']<0)),'yes', 'no')
            df2 = df1.loc[df1['value4'] == -1]
            #df2['ticker1'] = ticker1
            #df2['ticker2'] = column
            dict1 = {'ticker1':ticker1,'ticker2':column,'crosscount':len(df2)}
            mylist.append(dict1)
        df_final1 = pd.DataFrame(mylist)
        return df_final1
            #for idx,v in df1.iterrows():
            #    print idx,v['value1'], v['value2'], v['value31'], v['value32'], v['value4']
            #if i >= 3:
            #    stop       

        #df = self.findpairdollarizeddiffsasdataframe()
        #return df_final2
        
    def findpairdollarizeddiffsasdataframe(self,closepricesfilepath):
        print 'started def findpairstdev'
        import pandas as pd
        myfile = closepricesfilepath #'C:\Batches\GitStuff\$work\closeprices_sample.csv'
        df = pd.read_csv(myfile)
        df2 = df["Date"]
        df.set_index("Date", drop=True, inplace=True)
        columns = list(df.columns.values)
        #print df
        #print df2
        
        df_shares1 = 10000.0 / df.iloc[[0]]
        
        df_shares2 = df_shares1.append([df_shares1]*(len(df)-1),ignore_index=True)
        df_shares3 = pd.concat([df2, df_shares2], axis=1)
        df_shares3.set_index("Date", drop=True, inplace=True)

        df_dollarized = df.multiply(df_shares3, axis=1)
        #print df_dollarized
        df_pairdollarizeddiff = {}
        print 'started analysis...'
        for column in columns:
            df_diff = df_dollarized[columns].sub(df_dollarized[column], axis=0)
            df_pairdollarizeddiff[column] = df_diff
        print 'finished.'
        return df_pairdollarizeddiff,columns

    
if __name__=='__main__':
    o = find('C:\\Batches\\GitStuff\\$work\\closeprices_sample.csv')


