#C:\Batches\GitStuff\$work\correlation_sample.csv
def importcsv():
    print 'x'
def findpairstdev():
    s1 = 'JPM'
    s2 = 'BAC'
    import pandas as pd
    myfile = 'C:\Batches\GitStuff\$work\closeprices_sample.csv'
    df = pd.read_csv(myfile)
    df.set_index("Date", drop=True, inplace=True)
    #print df
    columns = list(df.columns.values)
    mylist = []
    alreadydonelist = []
    b = True
    mean1 = df[s1].mean()
    mean2 = df[s1].mean()
    quantity1 = 10000.0 / df[s1].iloc[0]
    quantity2 = 10000.0 / df[s2].iloc[0]
    #print df[s2].iloc[0]
    #print df[s1]
    dollarized1 = df[s1].apply(lambda x: x*quantity1)
    dollarized2 = df[s2].apply(lambda x: x*quantity2)
    print dollarized1
    print dollarized2
    dollarized0 = pd.concat([dollarized1, dollarized2], axis=1, join_axes=[dollarized1.index])
    dollarized0['diff'] = dollarized0[s1] - dollarized0[s2]
    #dollarized0['rollingstd'] = dollarized0['diff'].rolling_std()
    print dollarized0
    print 'max',dollarized0['diff'].max()
    print 'min',dollarized0['diff'].min()
    print 'mean',dollarized0['diff'].mean()
    print 'std',dollarized0['diff'].std()
    
##    while b == True:
##        maxvalue = df.values.max()
##        
##        if not maxvalue == 1:
##            for column in columns:
##                row = df[column].idxmax()
##                if df.loc[row,column] == maxvalue:
##                    list1 = [row,column]
##                    listsorted = sorted(list1)
##                    listsortedstring = listsorted[0]+listsorted[1]
##                    #print 'listsortedstring',listsortedstring
##                    if not listsortedstring in alreadydonelist:
##                        dict1 = {'pair':listsorted, 'value':df.loc[row][column]}
##                        alreadydonelist.append(listsortedstring)
##                        mylist.append(dict1)
##                    #dict1 = {'row':row,'column':column, 'value':df.loc[row][column]}
##                    #print dict1
##                    
##        if len(mylist) >= 1000:
##            b = False
##        df[df==maxvalue] = -10000
##        print x
##        for column in columns:
##            #df.loc[df['Value'].idxmax()]
##            row = df[column].idxmax()
##            maxval = df[column].max()
##            print row,column, maxval, df.loc[row][column]
##            if not maxval == 1:
##                mylist.append({'row':row,'column':column, 'value':df.loc[row][column]})
##            df.loc[row,column] = float(-10000)
##
####            for i, row in df.iterrows():
####                if row[column] == maxval:
####                    mylist.append({
####                    df.loc[row,column] = float(-10000)
         
    return mylist
    
    #print mydict
    
pairs = findpairstdev()
for p in pairs:
    print p
