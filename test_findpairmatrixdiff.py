#C:\Batches\GitStuff\$work\correlation_sample.csv
def importcsv():
    print 'x'
def findpairstdev():
    print 'started def findpairstdev'
    s1 = 'JPM'
    s2 = 'BAC'
    import pandas as pd
    myfile = 'C:\Batches\GitStuff\$work\closeprices_sample.csv'
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
    #print df_shares3
    #stop
    #index_full = list(df.index)
    #print df_shares2
    #print index_full
    #df_shares3 = df_shares2.set_index(index_full)
    
    #print df_shares3
    #stop
    #import numpy as np
    #print df
    #print df_shares1
    
    df_dollarized = df.multiply(df_shares3, axis=1)
    #print df_dollarized
    dict_of_difference_dataframes = {}
    print 'started analysis...'
    for column in columns:
        df_diff = df_dollarized[columns].sub(df_dollarized[column], axis=0)
        dict_of_difference_dataframes[column] = df_diff
    print 'finished.'
    return dict_of_difference_dataframes

    
    #print mydict
import pandas as pd
import numpy as np
dict_of_difference_dataframes = findpairstdev()
ticker1 = 'AAPL'
df = dict_of_difference_dataframes[ticker1]
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
print df_final1.sort_values('crosscount')
    #for idx,v in df1.iterrows():
    #    print idx,v['value1'], v['value2'], v['value31'], v['value32'], v['value4']
    #if i >= 3:
    #    stop                        


