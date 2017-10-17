#C:\Batches\GitStuff\$work\correlation_sample.csv
def importcsv():
    print 'x'
def findcorrelatedpairs():
    import pandas as pd
    myfile = 'C:\Batches\GitStuff\$work\correlation_sample.csv'
    df = pd.read_csv(myfile)
    df.set_index("Unnamed: 0", drop=True, inplace=True)
    print df
    columns = list(df.columns.values)
    mylist = []
    alreadydonelist = []
    b = True
    while b == True:
        maxvalue = df.values.max()
        maxrow = max(df.idxmax())
        s = df.max()[df.max() == df.max(index=1).max()].index
        print s
        s = str(s[0])
        maxcol = df.idxmax()[s]
        print maxcol
        df[df==maxvalue] = -10000
        
        if not maxvalue == 1:
            print maxvalue,maxrow,maxcol
            list1 = [maxrow,maxcol]
            listsorted = sorted(list1)
            listsortedstring = listsorted[0]+listsorted[1]
            if not listsortedstring in alreadydonelist:
                dict1 = {'pair':listsorted, 'value':maxvalue}
                alreadydonelist.append(listsortedstring)
                mylist.append(dict1)
                
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
                    
        if len(mylist) >= 100:
            b = False
        df[df==maxvalue] = -10000
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
    
pairs = findcorrelatedpairs()
for p in pairs:
    print p
