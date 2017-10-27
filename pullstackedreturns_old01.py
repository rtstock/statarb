# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:40:39 2015

@author: justin.malinchak
"""


import datetime
import pandas as pd
import numpy as np
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return False
        

def is_number(s):
    try:
        if np.isnan(s) == True:
            return False
        float(s)
        return True
    except ValueError:
        return False
        
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



class perform:
    def set_SymbolsList(self,SymbolsList):
        self._SymbolsList = SymbolsList
    def get_SymbolsList(self):
        return self._SymbolsList
    SymbolsList = property(get_SymbolsList, set_SymbolsList)

    def set_StartDateString(self,StartDateString):
        self._StartDateString = StartDateString
    def get_StartDateString(self):
        return self._StartDateString
    StartDateString = property(get_StartDateString, set_StartDateString)

    def set_EndDateString(self,EndDateString):
        self._EndDateString = EndDateString
    def get_EndDateString(self):
        return self._EndDateString
    EndDateString = property(get_EndDateString, set_EndDateString)

    def set_HistoryOfAdjClosePricesDataframe(self,HistoryOfAdjClosePricesDataframe):
        self._HistoryOfAdjClosePricesDataframe = HistoryOfAdjClosePricesDataframe
    def get_HistoryOfAdjClosePricesDataframe(self):
        return self._HistoryOfAdjClosePricesDataframe
    HistoryOfAdjClosePricesDataframe = property(get_HistoryOfAdjClosePricesDataframe, set_HistoryOfAdjClosePricesDataframe)

    def set_HistoryOfClosePricesDataframe(self,HistoryOfClosePricesDataframe):
        self._HistoryOfClosePricesDataframe = HistoryOfClosePricesDataframe
    def get_HistoryOfClosePricesDataframe(self):
        return self._HistoryOfClosePricesDataframe
    HistoryOfClosePricesDataframe = property(get_HistoryOfClosePricesDataframe, set_HistoryOfClosePricesDataframe)

    def __init__(self
                    , symbols
                    , startdate = '2004-12-31'
                    , enddate = '2005-12-31'
                ):
        
        print('Initialized class pullreturns.perform')
        
        self.SymbolsList = symbols
        self.StartDateString = startdate
        self.EndDateString = enddate
        
        import datetime
        import numpy as np
        
        yesterday_date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
        import pullprices as pp1
        df_good,df_missing = pp1.pull().stockhistoryasdataframe(symbols,startdate,enddate)
        list_of_good_symbols = np.unique(df_good[['Ticker']])
        print 'count of symbols returned from pullprices', len(list_of_good_symbols)
        print 'list_of_good_symbols', list_of_good_symbols
        if len(df_missing) > 0:
            list_of_missing_symbols =  np.unique(df_missing[['Ticker']])
            print 'list_of_missing_symbols', list_of_missing_symbols
        self.SymbolsList = list_of_good_symbols

        df_pivotadjclose = df_good.pivot(index='Date', columns='Ticker', values='Adj Close')
        df_pivotclose = df_good.pivot(index='Date', columns='Ticker', values='Close')
        self.HistoryOfAdjClosePricesDataframe = df_pivotadjclose
        self.HistoryOfClosePricesDataframe = df_pivotclose

    def dailystackedreturns(self,totalorpricechange='PriceChange',logorarithmetic='log'):

        symbols = self.SymbolsList 
        import datetime
        today_date = datetime.date.today()
        #import pullpricesusingpandas as pp
        if totalorpricechange == 'PriceChange':
            df_00 = self.HistoryOfClosePricesDataframe
        else:
            df_00 = self.HistoryOfAdjClosePricesDataframe
        #print '--- df_00 ---  pullreturns.dailyreturns()'
        #print df_00
        
        df_01 = pd.DataFrame(index=df_00.index.copy())
        for s in self.SymbolsList:
            if not logorarithmetic == 'log':
                df_01[s] = df_00[s].pct_change()
            else:
                df_01[s] = np.log(1.0 + df_00[s].pct_change())        
        return df_01

    
if __name__=='__main__':

    #symbols = ['LAZ', 'LMT', 'RTN', 'MAS', 'AMAT', 'INTC', 'LPX', 'GRMN', 'PCLN', 'KSS', 'JWN', 'M', 'GPS', 'LOW', 'PEP', 'CVS', 'CL', 'KMB', 'MO', 'PM', 'CVX', 'BAC', 'BEN', 'MS', 'AXP', 'CELG', 'AMGN', 'JNJ', 'LLY', 'MMM', 'UNP', 'CSCO', 'SWKS', 'CA', 'STX', 'LYB', 'APD', 'T', 'TGT', 'HD', 'ETR', 'AES', 'HOG', 'F', 'GPC', 'LEG', 'WHR', 'NWL', 'TRIP', 'HAS', 'BC', 'CMCSA', 'DIS', 'VIA', 'DISH', 'NWS', 'PAG', 'CRI', 'COLM', 'SKX', 'NKE', 'TAP', 'CASY', 'HRL', 'HAIN', 'SJM', 'ADM', 'KHC', 'MDLZ', 'FTI', 'SLB', 'NFX', 'KMI', 'CXO', 'MUR', 'WPX', 'EGN', 'XOM', 'LNG', 'FCNCA', 'LUK', 'Y', 'WTM', 'AXS', 'ALKS', 'MDT', 'XRAY', 'CAH', 'MD', 'PDCO', 'UHS', 'AGN', 'ARNC', 'UAL', 'AAL', 'GE', 'SNA', 'WAB', 'FLS', 'VRSK', 'GWR', 'GWW', 'VSAT', 'AVT', 'TWTR', 'AMD', 'QCOM', 'FSLR', 'OTEX', 'NUAN', 'HPE', 'RPM', 'MLM', 'VMC', 'SEE', 'SON', 'HHC', 'LVLT', 'LVLT', 'S', 'JLL']
    #symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT', 'AMD', 'AME', 'AMG', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANDV', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APC', 'APD', 'APH', 'ARE', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AYI', 'AZO', 'BA', 'BAC', 'BAX', 'BBT', 'BBY', 'BCR', 'BDX', 'BEN', 'BF.B', 'BHF', 'BHGE', 'BIIB', 'BK', 'BLK', 'BLL', 'BMY', 'BRK.B', 'BSX', 'BWA', 'BXP', 'C', 'CA', 'CAG', 'CAH', 'CAT', 'CB', 'CBG', 'CBOE', 'CBS', 'CCI', 'CCL', 'CDNS', 'CELG', 'CERN', 'CF', 'CFG', 'CHD', 'CHK', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COG', 'COH', 'COL', 'COO', 'COP', 'COST', 'COTY', 'CPB', 'CRM', 'CSCO', 'CSRA', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'D', 'DAL', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLPH', 'DLR', 'DLTR', 'DOV', 'DPS', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DWDP', 'DXC', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'EQT', 'ES', 'ESRX', 'ESS', 'ETFC', 'ETN', 'ETR', 'EVHC', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FL', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOX', 'FOXA', 'FRT', 'FTI', 'FTV', 'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HLT', 'HOG', 'HOLX', 'HON', 'HP', 'HPE', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KEY', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH', 'LKQ', 'LLL', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MA', 'MAA', 'MAC', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'MYL', 'NAVI', 'NBL', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWS', 'NWSA', 'O', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PCAR', 'PCG', 'PCLN', 'PDCO', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'PYPL', 'Q', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RHT', 'RJF', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCG', 'SCHW', 'SEE', 'SHW', 'SIG', 'SJM', 'SLB', 'SLG', 'SNA', 'SNI', 'SNPS', 'SO', 'SPG', 'SPGI', 'SPLS', 'SRCL', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDG', 'TEL', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSS', 'TWX', 'TXN', 'TXT', 'UA', 'UAA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT', 'WBA', 'WDC', 'WEC', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRK', 'WU', 'WY', 'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']
    symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL',]
    startdate = '2017-07-01'
    enddate = '2017-08-05'
    o = perform(symbols,startdate,enddate)
    
    df = o.dailystackedreturns(totalorpricechange='PriceChange',logorarithmetic='log')
    print '------ dailystackedreturns ------'
    print df

