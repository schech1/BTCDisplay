#!/usr/bin/python3

from papirus import PapirusTextPos
from papirus import Papirus
import time
import requests
from datetime import datetime
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

myBTC= 2.5
myETH= 4

text=PapirusTextPos(False, rotation = 180)


text.AddText("1", 85,0 , Id="date", size =15)
text.AddText("EUR", 55,20 , Id="eurlabel", size =16)
text.AddText("|",  110,20 , Id="pipe1", size =16)
text.AddText("USD", 130,20 , Id="usdlabel", size =16)

text.AddText("BTC:", 0,35 , Id="btc", size =18)
text.AddText("2", 55,35 ,Id="btceur", size =18)
text.AddText("|", 110,35 , Id="pipe2", size =18)
text.AddText("2", 130,35 ,Id="btcusd", size =18)

text.AddText("ETH:", 0,55 , Id="eth", size =18)
text.AddText("3", 55,55 , Id="etheur", size =18)
text.AddText("|", 110,55 , Id="pipe3", size =18)
text.AddText("3", 130,55 , Id="ethusd", size =18)

text.AddText("5",130,80 , Id="wallet", size =17)
text.AddText("My Wallet:",0,80 , Id="mymoney", size =17)


def getBTC():

    prices = cg.get_price(ids='bitcoin,ethereum', vs_currencies='usd,eur')

    btc_eur= (prices["bitcoin"]['eur']) 
    btc_usd= (prices["bitcoin"]['usd'])
    eth_eur= (prices["ethereum"]['eur'])
    eth_usd= (prices["ethereum"]['usd'])


    print (btc_eur, btc_usd, eth_eur,eth_usd)

    myWallet = (myBTC*btc_eur)+(myETH*eth_eur)
    myWallet=int(myWallet)
    eth_eur=int(eth_eur)
    eth_usd=int(eth_usd)
    
    now = datetime.now()
    current_time = now.strftime("%d.%m. %H:%M")
 
    
    text.UpdateText("date", current_time)
    
    text.UpdateText("btceur",str(btc_eur))
    text.UpdateText("btcusd",str(btc_usd))

    text.UpdateText("etheur",str(eth_eur))
    text.UpdateText("ethusd",str(eth_usd))
    
    text.UpdateText("wallet",str(myWallet))
    


    text.WriteAll()

    return 

data=getBTC()

