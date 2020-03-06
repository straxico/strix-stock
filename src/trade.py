import requests

#read or save token
#you can get your token from exir.io


def trade(token):
    ans=["nothing"]
    myorders=exir.myorders(token)
    rootdata=root.root()
    orderbook=exir.orderbook()
    tricker=exir.ticker()
    tradebook=exir.tradebook()
    balance=exir.balance(token)
    mytrades=exir.mytrades(token)

    first_asks=orderbook['btc-tmn']['asks'][0][0]
    sec_asks=orderbook['btc-tmn']['asks'][1][0]
    first_bids=orderbook['btc-tmn']['bids'][0][0]
    sec_bids=orderbook['btc-tmn']['bids'][1][0]
    gap_p=(first_asks - first_bids)/first_asks *100
    gap_calc=(int(rootdata['calclast'].replace(",","")) - int(rootdata['exirlast'].replace(",","")))/int(rootdata['exirlast'].replace(",",""))
    last_trade=mytrades['data'][0]
    ans.append('fetched')
    if (len(myorders)==0):
        ans.append('order not found')
        if (last_trade['side']=='sell'):
            if(gap_p>0):
                ans.append("gap p uper 1")
                if (gap_calc>0):
                    ans.append("gap calc uper 1")
                    if(rootdata["btc1h"]> (-0.5) ):
                        ans.append("btc1h > 0")
                        price=sec_bids+50000
                        req=requests.get('http://bit.tyto.ir/change/buy/'+str(price))
                        ans.append(req)
                        ans.append("buy order at"+str(price))

        if (last_trade['side']=='buy'):
            price=max(first_asks-50000,mytrades['data'][1]['price']*1.01)
            req=requests.get('http://bit.tyto.ir/change/sell/'+str(price))
            ans.append(req)
            ans.append("sell order at"+str(price))

    if (len(myorders)>0):
        ans.append('order found')
        if (myorders[0]['side']=='buy'):
            ans.append('buy order found')
            if(rootdata["btc1h"]>(-0.5)):
                if(sec_bids>myorders[0]['price']):
                    req=requests.get('http://bit.tyto.ir/change/delbtc')
                    ans.append(req)
                    price=sec_bids+50000
                    req=requests.get('http://bit.tyto.ir/change/buy/'+str(price))
                    ans.append(req)
                    ans.append('del and set buy order at' +str(price))
                if(sec_bids+100000<myorders[0]['price']):
                    req=requests.get('http://bit.tyto.ir/change/delbtc')
                    ans.append(req)
                    price=sec_bids+50000
                    req=requests.get('http://bit.tyto.ir/change/buy/'+str(price))
                    ans.append(req)
                    ans.append('del and set buy order at' +str(price))
            else:
                req=requests.get('http://bit.tyto.ir/change/delbtc')
                ans.append(req)

        if (myorders[0]['side']=='sell'):
            print('sell order found')
            if(sec_asks-100000>myorders[0]['price']):
                price=max(sec_asks-50000,int((mytrades['data'][0]['price']*1.01)/50000+1)*50000)
                req=requests.get('http://bit.tyto.ir/change/delbtc')
                ans.append(req)
                req=requests.get('http://bit.tyto.ir/change/sell/'+str(price))
                ans.append(req)
                ans.append('del and set sell order at' +str(price))

            if(sec_asks<myorders[0]['price']):
                price=max(sec_asks-50000,int((mytrades['data'][0]['price']*1.01)/50000+1)*50000)
                req=requests.get('http://bit.tyto.ir/change/delbtc')
                ans.append(req)
                req=requests.get('http://bit.tyto.ir/change/sell/'+str(price))
                ans.append(req)
                ans.append('del and set sell order at' +str(price))
    return ans
