import pandas as pd
import numpy as np
import bursApi

market=bursApi.market()
market_np=np.empty((0,22))
for i in market:
    market_np=np.concatenate((market_np,np.array([list(market[i].values())])))
market_pd=pd.DataFrame(market_np,columns=list(market[i].keys()))
def CCI(close, high, low, n, constant): 
     TP = (high + low + close) / 3 
     CCI = pd.Series((TP - TP.rolling(n).mean()) / (constant * TP.rolling(n).std()), name = 'CCI_' + str(n)) 
     return CCI

def all_data(id):
    all_data={}
    all_data['dayinfo']=bursApi.get_dayinfo(id)
    all_data['dayprice']=bursApi.get_dayprice(id)
    all_data['clienttype_history']=bursApi.get_clienttype_history(id)
    return all_data
def saf_pd(id):
    day=bursApi.get_dayinfo(int(id))
    saf_np=np.empty((0,6))
    for i in range(1,4):
        saf_np=np.concatenate((saf_np,np.array([list(day[i].values())])))
    saf_pd=pd.DataFrame(saf_np,columns=list(day[i].keys()))
    return saf_pd  
def general_dayinfo_pd(id):
    general=bursApi.get_day_general_info(int(id))
    general_dayinfo_np=np.empty((0,13))
    general_dayinfo_np=np.concatenate((general_dayinfo_np,np.array([list(general.values())])))
    general_dayinfo_pd=pd.DataFrame(general_dayinfo_np,columns=list(general.keys()))
    return general_dayinfo_pd

def dayprice_pd(id):
    day=bursApi.get_dayprice(int(id))
    dayprice_np=np.empty((0,6))
    for i in day:
        dayprice_np=np.concatenate((dayprice_np,np.array([list(i.values())])))
    dayprice_np[:,1:]=dayprice_np[:,1:].astype(int)
    dayprice_pd=pd.DataFrame(dayprice_np,columns=list(day[1].keys()))
    now=pd.datetime.now()
    for i in range(len(dayprice_pd.time)):
        s=dayprice_pd.time[i].split(':')
        dayprice_pd.time[i]=pd.datetime(now.year,now.month,now.day,int(s[0]),int(s[1]))
    dayprice_pd.iloc[:,1:]= dayprice_pd.iloc[:,1:].astype(np.int64)
    return dayprice_pd

def dayinfo_pd(id):    
    day=bursApi.get_dayinfo(int(id))
    dayinfo_np=np.empty((0,13))
    dayinfo_np=np.concatenate((dayinfo_np,np.array([list(day[0].values())])))
    dayinfo_pd=pd.DataFrame(dayinfo_np,columns=list(day[0].keys()))
    return dayinfo_pd

def history_pd(id): 
    hist=bursApi.get_history(int(id))
    history_np=np.empty((0,10))
    for i in hist:
        history_np=np.concatenate((history_np,np.array([list(i.values())])))
    history_np[:,1:]=history_np[:,1:].astype(float)
    history_pd=pd.DataFrame(history_np,columns=list(hist[1].keys()))
    history_pd.iloc[:,1:]= history_pd.iloc[:,1:].astype(float)
    history_pd.iloc[:,1:]= history_pd.iloc[:,1:].astype(np.int64)
    history_pd=history_pd.iloc[::-1]
    TP = (history_pd['max_price'] + history_pd['min_price'] + history_pd['close_price']) / 3 
    n=20
    constant=0.015
    history_pd['cci20'] = pd.Series((TP - TP.rolling(n).mean()) / (constant * TP.rolling(n).std()), name = 'CCI_' + str(n)) 
    history_pd=history_pd.iloc[::-1]
    return history_pd

def client_history_pd(id):
    client_hist=bursApi.get_clienttype_history(int(id))
    client_history_np=np.empty((0,13))
    for i in client_hist:
            client_history_np=np.concatenate((client_history_np,np.array([list(i.values())])))
    client_history_pd=pd.DataFrame(client_history_np,columns=list(client_hist[1].keys()))
    return client_history_pd

