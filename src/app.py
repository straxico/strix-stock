import os
from flask import Flask, render_template
import bursData

app = Flask(__name__)

@app.route("/")
def hello():
    market=bursData.market_pd
    return render_template("index.html",market=market,strix='Flask Bootstrap Table')

@app.route('/stock/<int:id>')
def stosk_view(id):
    market=bursData.market_pd
    symbol=market.loc[market['id'] == str(id)]['symbol'].values[0]
    name=market.loc[market['id'] == str(id)]['name'].values[0]
    groupid=market.loc[market['id'] == str(id)]['group_id'].values[0]
    group_list=market.loc[market['group_id'] == groupid ]
    day_price_list=bursData.dayprice_pd(int(id))
    general=bursData.general_dayinfo_pd(id)
    saf=bursData.saf_pd(id)
    return render_template("stock.html", id=id,name=name ,symbol=symbol,group_list=group_list,saf=saf,general=general,day_price_list=day_price_list)

@app.route('/history/<int:id>')
def history_view(id):
    hist=bursData.history_pd(int(id))
    market=bursData.market_pd
    symbol=market.loc[market['id'] == str(id)]['symbol'].values[0]
    name=market.loc[market['id'] == str(id)]['name'].values[0]
    return render_template("history.html", hist=hist,symbol=symbol,name=name)

@app.route('/client_history/<int:id>')
def client_history_view(id):
    hist=bursData.client_history_pd(int(id))
    market=bursData.market_pd
    symbol=market.loc[market['id'] == str(id)]['symbol'].values[0]
    name=market.loc[market['id'] == str(id)]['name'].values[0]
    return render_template("client_history.html", hist=hist,symbol=symbol,name=name)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
