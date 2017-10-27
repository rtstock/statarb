import pandas as pd
import numpy as np
def stockpricereturnsstacked(symbols,fromdate,todate,pricechangeortotal='pricechange',logorarithmetic='log'):
    import pullstackedprices as psp
    df_close,df_adjclose,df_missing = psp.stockpricehistorystacked(symbols,fromdate,todate)
    #print df_close
    if not pricechangeortotal=='pricechange':
        df_00 = df_adjclose
    else:
        df_00 = df_close
    df_01 = pd.DataFrame(index=df_00.index.copy())
    list_of_symbols_good = list(df_00.columns)
    print 'list_of_symbols_good',list_of_symbols_good
    for s in list_of_symbols_good:
        if not logorarithmetic == 'log':
            df_01[s] = df_00[s].pct_change()
        else:
            df_01[s] = np.log(1.0 + df_00[s].pct_change())        
    return df_01

if __name__=='__main__':
    symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL', ]
    print 'symbols',symbols
    df = stockpricereturnsstacked(symbols,'2017-07-01','2017-09-30')
    print df
