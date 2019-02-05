import os
from flask import Flask, render_template, jsonify
import bu1,burs,root
from io import BytesIO
import base64
import json
import pandas as pd
import exir
import trade
token ="1111111111111111111"

app = Flask(__name__)

@app.route("/")
def hi():
    data=root.root()
    return render_template("root.html",data=data,strix='Flask Bootstrap Table')


@app.route("/change")
def ex():
    data=[]
    return render_template("exir.html",data=data,strix='Flask Bootstrap Table')



@app.route("/change/ticker")
def ex1():
    data=exir.ticker()
    return json.dumps(data)

@app.route("/change/orderbook")
def ex2():
    data=exir.orderbook()
    return json.dumps(data)

@app.route("/change/tradebook")
def ex3():
    data=exir.tradebook()
    return json.dumps(data)

@app.route("/change/user")
def ex4():
    data=exir.user(token)
    return json.dumps(data)

@app.route("/change/balance")
def ex5():
    data=exir.balance(token)
    return json.dumps(data)

@app.route("/change/mytrades")
def ex6():
    data=exir.mytrades(token)
    return json.dumps(data)

@app.route("/change/myorders")
def ex7():
    data=exir.myorders(token)
    return json.dumps(data)

@app.route("/change/root")
def ex8():
    data=root.root()
    return json.dumps(data)

@app.route("/change/buy/<int:price>")
def ex9(price):
    if (price<45000000 and price>35000000):
        data=exir.buybtc(token,0.0003,price)
    return json.dumps(data)

@app.route("/change/sell/<int:price>")
def ex10(price):
    if (price<45000000 and price>35000000):
        data=exir.sellbtc(token,0.0003,price)
    return json.dumps(data)

@app.route("/change/delbtc")
def ex11():
    data=exir.delbtc(token)
    return json.dumps(data)

@app.route("/change/trade")
def ex12():
    data=trade.trade(token)
    return str(data)



@app.route("/plot")
def hiplot():
    data=root.root()
    return render_template("plot.html",data=data,strix='Flask Bootstrap Table')

@app.route("/bitchart")
def go():
    data=root.bitchart()
    a=[data['time'].tolist(),data['exir'].tolist(),data['calc'].tolist()]
    return json.dumps(a)
@app.route("/savebitchart")
def gos():
    data=root.savebitchart()
    a=[data['time'].tolist(),data['exir'].tolist(),data['calc'].tolist()]
    return json.dumps(a)

@app.route("/market")
def hello():
    market=bu1.market_pd
    return render_template("index.html",market=market,strix='Flask Bootstrap Table')

@app.route('/stock/<int:id>')
def stosk_view(id):
    #c=bu1.dayinfo_pd(id)
    #.................................
    market=bu1.market_pd
    symbol=market.loc[market['id'] == str(id)]['symbol'].values[0]
    name=market.loc[market['id'] == str(id)]['name'].values[0]
    groupid=market.loc[market['id'] == str(id)]['group_id'].values[0]
    group_list=market.loc[market['group_id'] == groupid ]
    day_price_list=bu1.dayprice_pd(int(id))
    general=bu1.general_dayinfo_pd(id)
    saf=bu1.saf_pd(id)
    plt=bu1.dayprice_plot(int(id))
    bio = BytesIO()
    bio.name = 'image.png'
    plt.savefig(bio, format='png')
    bio.seek(0)
    day_plot = base64.b64encode(bio.getvalue()).decode()
    return render_template("stock.html", id=id,name=name ,symbol=symbol,group_list=group_list,saf=saf,general=general,day_price_list=day_price_list,day_plot=day_plot)

@app.route('/history/<int:id>')
def history_view(id):
    #c=bu1.dayinfo_pd(id)
    #.................................
    hist=bu1.history_pd(int(id))
    market=bu1.market_pd
    symbol=market.loc[market['id'] == str(id)]['symbol'].values[0]
    name=market.loc[market['id'] == str(id)]['name'].values[0]
    return render_template("history.html", hist=hist,symbol=symbol,name=name)

@app.route('/client_history/<int:id>')
def client_history_view(id):
    #c=bu1.dayinfo_pd(id)
    #.................................
    hist=bu1.client_history_pd(int(id))
    market=bu1.market_pd
    symbol=market.loc[market['id'] == str(id)]['symbol'].values[0]
    name=market.loc[market['id'] == str(id)]['name'].values[0]
    return render_template("client_history.html", hist=hist,symbol=symbol,name=name)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
