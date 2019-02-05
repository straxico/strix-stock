import requests
import json

#ticker
#last price of crypto
def ticker():
    ticker_btc = requests.get("https://api.exir.tech/v0/ticker?symbol=btc-tmn").json()
    ticker_eth = requests.get("https://api.exir.tech/v0/ticker?symbol=eth-tmn").json()
    ticker_bch = requests.get("https://api.exir.tech/v0/ticker?symbol=bch-tmn").json()
    ticker={"btc-tmn":ticker_btc,"eth-tmn":ticker_eth,"bch-tmn":ticker_bch}
    return ticker

#order book
#list of 10 last buy and sell order for simbols
def orderbook():
    orderbook = requests.get("https://api.exir.tech/v0/orderbooks").json()
    return orderbook

#trade book
#40 last trades of symbols
def tradebook():
    tradebook = requests.get("https://api.exir.tech/v0/trades").json()
    return tradebook



#user details
def user(tokenid):
    user = requests.get("https://api.exir.tech/v0/user", headers = {"Authorization": "Bearer " +  tokenid}).json()
    print("Hello " + str(user["full_name"]))
    print("Email: " + user["email"])
    return user

#balance
def balance(tokenid):
    balance = requests.get("https://api.exir.tech/v0/user/balance", headers = {"Authorization": "Bearer " +  tokenid}).json()
    return balance


#deposits
#list of add currency to your walet
def deposits(tokenid):
    deposits = requests.get("https://api.exir.tech/v0/user/deposits", headers = {"Authorization": "Bearer " +  tokenid}).json()
    return deposits

#withdrawals
#list of get currency from your walet
def withdrawals(tokenid):
    withdrawals = requests.get("https://api.exir.tech/v0/user/withdrawals", headers = {"Authorization": "Bearer " +  tokenid}).json()
    return withdrawals

#my trades
#list of my trades
def mytrades(tokenid):
    mytrades = requests.get("https://api.exir.tech/v0/user/trades", headers = {"Authorization": "Bearer " +  tokenid}).json()
    return mytrades

#my orders
#list of my active orders
def myorders(tokenid):
    myorders = requests.get("https://api.exir.tech/v0/user/orders", headers = {"Authorization": "Bearer " +  tokenid}).json()
    return myorders

#set buy order for btc
def buybtc(tokenid,size,price) :
    data = {"symbol":"btc-tmn","side":"buy","size":size,"type":"limit","price":price}
    buybtc = requests.post("https://api.exir.tech/v0/order", headers = {"Authorization": "Bearer " +  tokenid , 'Content-type': 'application/json'}, data=json.dumps(data)).json()
    print (buybtc)
    return buybtc

#set sell order for btc
def sellbtc(tokenid,size,price) :
    data = {"symbol":"btc-tmn","side":"sell","size":size,"type":"limit","price":price}
    sellbtc = requests.post("https://api.exir.tech/v0/order", headers = {"Authorization": "Bearer " +  tokenid , 'Content-type': 'application/json'}, data=json.dumps(data)).json()
    print (sellbtc)
    return sellbtc

#delete all btc orders
def delbtc(tokenid) :
    data = {"symbol":"btc-tmn"}
    delete= requests.delete("https://api.exir.tech/v0/user/orders", headers = {"Authorization": "Bearer " +  tokenid , 'Content-type': 'application/json'}, data=data).json()
    print (delete)
    return delete
