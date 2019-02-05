# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:55:57 2018

@author: strix
"""

import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

def root():
    bonbast=requests.get('https://www.bonbast.com').text
    cryptomarket = pd.DataFrame(requests.get('https://api.coinmarketcap.com/v2/global/?convert=BTC').json()['data']['quotes'])
    bitcoinmarket = pd.DataFrame(requests.get('https://api.coinmarketcap.com/v2/ticker/1/').json()['data']['quotes'])
    dolarsell=BeautifulSoup(bonbast ,features="html.parser").find(id="usd1").text
    dolarbuy=BeautifulSoup(bonbast ,features="html.parser").find(id="usd2").text
    Eurosell=BeautifulSoup(bonbast ,features="html.parser").find(id="eur1").text
    Eurobuy=BeautifulSoup(bonbast ,features="html.parser").find(id="eur2").text
    tsetmc= requests.get("http://tse.ir/json/HomePage/nazerMSG.json").json()['miniSlider']
    exirbtc = requests.get("https://api.exir.tech/v0/ticker?symbol=btc-tmn").json()
    rootdata={"dolarsell":format(int(dolarsell),',d'),
              "dolarbuy":format(int(dolarbuy), ',d'),
              "Eurosell":format(int(Eurosell),',d'),
              "Eurobuy":format(int(Eurobuy), ',d'),
              "exirlast":format(exirbtc["last"], ',d'),
              "exirvol": round(exirbtc["volume"],0),
              "btcprice": format(int(bitcoinmarket['USD']['price']), ',d'),
              "btc1h":bitcoinmarket['USD']['percent_change_1h'],
              "btc24h":bitcoinmarket['USD']['percent_change_24h'],
              "btc7d":bitcoinmarket['USD']['percent_change_7d'],
              "cryptocap":format(int(cryptomarket["USD"]["total_market_cap"] /1000000000), ',d'),
              "cryptovol":format(int(cryptomarket["USD"]["total_volume_24h"] /1000000000), ',d'),
              "shakhes":format(int(tsetmc[0]), ',d'),
              "calclast":format(int(dolarsell)*int(bitcoinmarket['USD']['price']),',d'),
              "strixold":(datetime.date.today() - datetime.date(1994, 3, 3)).days,
              }
    return rootdata



def savebitchart():
    tyto=requests.get('http://bit.tyto.ir').text
    now=datetime.datetime.now()
    exirlast=int(BeautifulSoup(tyto ,features="html.parser").find(id="exirlast").text.replace(",",""))
    calclast=int(BeautifulSoup(tyto ,features="html.parser").find(id="calclast").text.replace(",",""))
    data=[now,exirlast,calclast]
    file=open(r'/mnt/shared-volume/bitt.csv', 'a')
    writer = csv.writer(file)
    writer.writerow(data)
    file.close()
    data=pd.read_csv(r'/mnt/shared-volume/bitt.csv',header=None,names=['time','exir','calc'])
    return data

def bitchart():
    data=pd.read_csv(r'/mnt/shared-volume/bitt.csv',header=None,names=['time','exir','calc'])
    return data
