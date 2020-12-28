#!/usr/bin/python3

from papirus import PapirusTextPos
from papirus import Papirus
import time
import requests
import datetime

myBuyLimit = 25595  # Adjust to desired value. Will Change "Wait" or "Buy" status
myBTC= 2.5        # Adjust tto your hodled BTC

text=PapirusTextPos(False, rotation = 180)

text.AddText("BTC", 160,5 , Id="cur")
text.AddText("1", 0,5 , Id="date")
text.AddText("2", 0,30 ,Id="usd")
text.AddText("3", 0,50 , Id="eur")
text.AddText("4",150,75 , Id="action")
text.AddText("5",0,75 , Id="wallet")


def getBTC():
    btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    USD = (btc.json()['bpi']['USD']['rate'])
    EUR = (btc.json()['bpi']['EUR']['rate'])
    Date= (btc.json()['time']['updatedISO'])
    Date = datetime.datetime.strptime(Date, "%Y-%m-%dT%H:%M:%S%z")
    Date = time.strftime("%d.%m. %H:%M")
    update_date=(Date)
    
    USD = USD.replace(',','')
    EUR = EUR.replace(',','')
    USD=round(float(USD),2)
    EUR=round(float(EUR),2)
	
    calc_value= myBTC*float(EUR)
    calc_value=round(calc_value,2)


    USD_price=("USD:%s" % (str(USD)))
    EUR_price=("EUR:%s" % (str(EUR)))
    
    text.UpdateText("date", update_date)
    text.UpdateText("usd",USD_price)
    text.UpdateText("eur",EUR_price)
    text.UpdateText("wallet",str(calc_value))
    

    if float(USD) <= myBuyLimit:        
        text.UpdateText("action", "Buy")
    else:
        text.UpdateText("action", "Wait")
    text.WriteAll()

    return USD,EUR,Date

data=getBTC()

