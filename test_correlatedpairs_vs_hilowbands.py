###C:\Batches\GitStuff\$work\correlation_sample.csv
def importcsv():
    print 'x'
def findpairstdev():
    import pandas as pd
    myfile = 'C:\Batches\GitStuff\$work\closeprices_sample.csv'
    df = pd.read_csv(myfile)
    df2 = df["Date"]
    df.set_index("Date", drop=True, inplace=True)
    columns = list(df.columns.values)
    
    df_shares1 = 10000.0 / df.iloc[[0]]
    
    df_shares2 = df_shares1.append([df_shares1]*(len(df)-1),ignore_index=True)
    df_shares3 = pd.concat([df2, df_shares2], axis=1)
    df_shares3.set_index("Date", drop=True, inplace=True)

    
    df_dollarized = df.multiply(df_shares3, axis=1)
    print df_dollarized
    dict_of_difference_matrixes = {}
    for column in columns:
        df_diff = df_dollarized[columns].sub(df_dollarized[column], axis=0)
        dict_of_difference_matrixes[column] = df_diff
        print 'finished', column
    return dict_of_difference_matrixes
    
def applytopcorrelations():
    print 'running',applytopcorrelations
    dict_of_matrixes = findpairstdev()
    import pandas as pd
    myfile = 'C:\\Batches\\GitStuff\\$work\\top_correlations.csv'
    df = pd.read_csv(myfile)
    df.set_index("Unnamed: 0", drop=True, inplace=True)
    #print df
    for row in df.iterrows():
        print 'xxxx',row[1]['s1'],row[1]['s2'],row[1]['correlation']
        print dict_of_matrixes[row[1]['s1']]
applytopcorrelations()
