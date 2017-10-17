#C:\Batches\GitStuff\$work\correlation_sample.csv

def look_using_generator(df, value):
    return [(row[0], df.columns[row.index(value)-1]) for row in df.itertuples() if value in row[1:]]

def findcorrelatedpairs():
    import numpy as np
    import pandas as pd
    myfile = 'C:\Batches\GitStuff\$work\correlation_sample.csv'
    df = pd.read_csv(myfile)
    df.set_index("Unnamed: 0", drop=True, inplace=True)
    #print df
    columns = list(df.columns.values)
    mylist = []
    alreadydonelist = []
    b = True
    df[df==1] = -10000
    while b == True:
        maxvalue = df.values.max()
        rx = look_using_generator(df,maxvalue)
        dict1 = {'s1':rx[0][0], 's2':rx[0][1], 'correlation':maxvalue}
        mylist.append(dict1)
        
        if maxvalue == -10000:
            print len(mylist)
            b = False
        if len(mylist) > 300:
            b = False
        if len(mylist)%100 == 1:
            print len(mylist),rx[0],maxvalue
        df[df==maxvalue] = -10000
    print 'printing results...'
    df_result = pd.DataFrame(mylist)
    df_result.to_csv('C:\\Batches\\GitStuff\\$work\\top_correlations.csv', sep=',')
    return df_result

##        print df

##        print 'maxvalue',maxvalue
##        #rx = df.loc[[maxvalue,columns]]
##        #rx = df.loc[df == maxvalue]
##        
##        #m = df == maxvalue
##        #rx = df.where(m, -df) == np.where(m, df, -df)
##        #rx = df.where(maxvalue)
##        valuelist = [maxvalue]
##        rx = df[df.isin(valuelist)]
##        print '--- rx ---'
##        print rx
##        print rx.dropna(axis=1)
##        stop
##        idx = df[df[columns] == maxvalue]
##        print df[df==maxvalue]
##        #print idx
##        stop

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
        #if float(len(mylist))%100.0 == 1.0:
        #    print len(mylist), maxvalue
        #if len(mylist) >= 2000:
        #    b = False
        #df[df==maxvalue] = -10000
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
         
    #return mylist
    
    #print mydict
    
listofdicts = findcorrelatedpairs()


