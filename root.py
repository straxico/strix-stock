# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:55:57 2018

@author: strix
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
def root():
    cryptomarket = pd.DataFrame(requests.get('https://api.coinmarketcap.com/v2/global/?convert=BTC').json()['data']['quotes'])
    bitcoinmarket = pd.DataFrame(requests.get('https://api.coinmarketcap.com/v2/ticker/1/').json()['data']['quotes'])
    dolarsell=BeautifulSoup(requests.get('https://www.bonbast.com').text ,features="html.parser").find(id="usd1").text
    dolarbuy=BeautifulSoup(requests.get('https://www.bonbast.com').text ,features="html.parser").find(id="usd2").text

    exirbtc = requests.get("https://api.exir.tech/v0/ticker?symbol=btc-tmn").json()
    rootdata={"dolarsell":format(int(dolarsell),',d'),
              "dolarbuy":format(int(dolarbuy), ',d'),
              "exirlast":format(exirbtc["last"], ',d'),
              "exirvol": round(exirbtc["volume"],0),
              "btcprice": format(int(bitcoinmarket['USD']['price']), ',d'),
              "btc1h":bitcoinmarket['USD']['percent_change_1h'],
              "btc24h":bitcoinmarket['USD']['percent_change_24h'],
              "btc7d":bitcoinmarket['USD']['percent_change_7d'],
              "cryptocap":format(int(cryptomarket["BTC"]["total_market_cap"]), ',d'),
              "cryptovol":format(int(cryptomarket["BTC"]["total_volume_24h"]), ',d'),
              }
    return rootdata

print(root())
