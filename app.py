from flask import Flask, render_template
import bu1,burs
from io import BytesIO
import base64
import pandas as pd

app = Flask(__name__)

@app.route("/")
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
    app.run(host='127.0.0.1', port=5001)